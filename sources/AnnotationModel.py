from typing import Optional, Union, Any, Dict

from PySide6.QtCore import Qt, QObject, QAbstractListModel, QModelIndex, QPersistentModelIndex, Signal, Slot, Property, QByteArray

from sources.Annotation import Annotation

class AnnotationModel(QAbstractListModel):
    # defined the roles
    STATEMENT = Qt.UserRole
    VERDICT = Qt.UserRole + 1
    EVIDENCE = Qt.UserRole + 2

    # signals
    rowInsertErrorSignal = Signal(str)
    setStatementErrorSignal = Signal(str)
    setVerdictErrorSignal = Signal(str)
    setEvidenceErrorSignal = Signal(str)
    contextChanged = Signal()
    selectionChanged = Signal()

    def __init__(self, parent: Optional[QObject] = ...) -> None:
        super().__init__()

        self.__context = "Context is unavailable"
        self.__data = [Annotation({
            "statement": "Statement is unavailable",
            "verdict": 0,
            "evidence": "Evidence is unavailable",
            "selectionStart": 0,
            "selectionEnd": 0
        })]
        self.__selectedIndex = 0

    def __len__(self):
        return len(self.__data)

    def rowCount(self, parent: Union[QModelIndex, QPersistentModelIndex] = ...) -> int:
        return len(self.__data)
    
    @Property(str)
    def context(self) -> str:
        return self.__context
    
    def data(self, index: Union[QModelIndex, QPersistentModelIndex], role: int = ...) -> Any:
        if not index.isValid():
            return None
        
        if role == self.STATEMENT:
            return self.__data[index.row()].statement
        
        if role == self.VERDICT:
            return self.__data[index.row()].verdict
        
        if role == self.EVIDENCE:
            return self.__data[index.row()].evidence
        
        return None
    
    def setData(self, index: Union[QModelIndex, QPersistentModelIndex], value: Any, role: int = ...) -> bool:
        if not index.isValid():
            return False

        if role == self.STATEMENT:
            self.__data[index.row()].setStatement(str(value))
            self.dataChanged.emit(index, index)
            return True
        
        if role == self.VERDICT:
            self.__data[index.row()].setVerdict(int(value))
            self.dataChanged.emit(index, index)
            return True
        
        if role == self.EVIDENCE:
            self.__data[index.row()].setEvidence(str(value))
            self.dataChanged.emit(index, index)
            return True
        
        return False
    
    def insertRow(self, row: int, parent: QModelIndex=QModelIndex()) -> bool:
        if row < 0 or row >= len(self):
            return False
        
        self.beginInsertRows(parent, row, row)
        self.__data.insert(row, Annotation())
        self.endInsertRows()

        return True

    def removeRow(self, row: int, parent: QModelIndex=QModelIndex()) -> bool:
        if row < 0 or row >= len(self):
            return False
        
        self.beginRemoveRows(parent, row, row)
        self.__data.pop(row)
        self.endRemoveRows()

        return True
    
    def roleNames(self) -> Dict[int, QByteArray]:
        return {
            self.STATEMENT: b"statement",
            self.VERDICT: b"verdict",
            self.EVIDENCE: b"evidence"
        }
    
    def flags(self, index: Union[QModelIndex, QPersistentModelIndex]) -> Qt.ItemFlag:
        if not index.isValid():
            return Qt.NoItemFlags
        
        return super().flags(index) | Qt.ItemIsEditable
    
    @property
    def annotations(self):
        return [annotation.annotation for annotation in self.__data]

    @Property(int)
    def selectedIndex(self):
        return self.__selectedIndex
    
    @selectedIndex.setter
    def selectedIndex(self, value: int):
        self.__selectedIndex = value

    @Slot(str)
    def setEvidence(self, evidence: str):
        if evidence == "": # skip updating when evidence is an empty string
            return
        index = self.createIndex(self.__selectedIndex, 0)
        self.setData(index, evidence, self.EVIDENCE)

    @Slot(int, int)
    def setSelectionIndices(self, selectionStart: int, selectionEnd: int) -> None:
        if selectionStart == selectionEnd:
            return None
        
        self.__data[self.__selectedIndex].setSelectionStart(selectionStart)
        self.__data[self.__selectedIndex].setSelectionEnd(selectionEnd)

        self.selectionChanged.emit()
    
    @Slot(dict)
    def setAnnotations(self, annotation: dict):
        # clear all previous annotations
        while self.rowCount() > 0:
            self.removeRow(0)

        # reset the annotations
        self.__context = annotation["context"]
        self.contextChanged.emit()
        self.__data = []
        if len(annotation["information"]) == 0:
            self.__data = [{
                "statement": "",
                "verdict": 0,
                "evidence": ""
            }] * 10
        else:
            self.__data = annotation["information"]

        for idx in range(len(self.__data)):
            item = self.__data[idx]
            insertedRow = self.insertRow(idx)
            if not insertedRow:
                self.rowInsertErrorSignal.emit(f"Cannot insert row at index {idx}th")

            setStatement = self.setData(self.index(idx, 0, QModelIndex()),
                                      item["statement"], self.STATEMENT)
            if not setStatement:
                self.setStatementErrorSignal.emit(f"Cannot set statement for information {idx}th")

            setVerdict = self.setData(self.index(idx, 0, QModelIndex()),
                                      item["verdict"], self.VERDICT)
            if not setVerdict:
                self.setStatementErrorSignal.emit(f"Cannot set verdict for information {idx}th")

            setEvidence = self.setData(self.index(idx, 0, QModelIndex()),
                                      item["evidence"], self.EVIDENCE)
            if not setEvidence:
                self.setStatementErrorSignal.emit(f"Cannot set evidence for information {idx}th")

        self.__selectedIndex = 0
    
    @Slot(int)
    def addAnnotation(self, idx: int) -> bool:
        return self.insertRow(idx+1)
    
    @Slot(int)
    def removeAnnotation(self, idx: int) -> bool:
        return self.removeRow(idx)
