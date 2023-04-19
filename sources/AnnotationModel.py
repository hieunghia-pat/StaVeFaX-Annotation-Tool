from typing import Optional, Union, Any, List, Dict

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

    def __init__(self, parent: Optional[QObject] = ...) -> None:
        super().__init__()

        self.__context = "Context is unavailable"
        self.__data = [Annotation({
            "statement": "Statement is unavailable",
            "verdict": 1,
            "evidence": "Evidence is unavailable"
        })]
        self.__selectedIndex = 0

    def __len__(self):
        return len(self.__data)

    def rowCount(self, parent: Union[QModelIndex, QPersistentModelIndex] = ...) -> int:
        return len(self.__data)
    
    @Property(str)
    def context(self) -> str:
        return self.__context
    
    @context.setter
    def context(self, value: str):
        self.__context = value
    
    def data(self, index: Union[QModelIndex, QPersistentModelIndex], role: int = ...) -> Any:
        if not index.isValid():
            return None
        
        if role == self.STATEMENT:
            return self.__data[index.row()].statement
        
        if role == self.VERDICT:
            return self.__data[index.row()].verdict
        
        if role == self.EVIDENCE:
            return self.__data[self.__selectedIndex].evidence
        
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
    
    def insertRow(self, row: int, parent: Union[QModelIndex, QPersistentModelIndex] = ...) -> bool:
        if row < 0 or row == len(self):
            return False
        
        self.beginInsertRows(parent, row, row)
        self.__data[row].insert(row, Annotation())
        self.endInsertRows()

        return True

    def removeRow(self, row: int, parent: Union[QModelIndex, QPersistentModelIndex] = ...) -> bool:
        if row < 0 or row == len(self):
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
    def index(self):
        return self.__selectedIndex
    
    @index.setter
    def index(self, value: int):
        self.__selectedIndex = value

    @Slot(str)
    def setEvidence(self, evidence: str):
        if evidence == "": # skip updating when evidence is an empty string
            return
        index = self.createIndex(self.__selectedIndex, 0)
        self.setData(index, evidence, self.EVIDENCE)
    
    @Slot(list)
    def setAnnotations(self, annotations: List[Dict]):
        assert len(annotations) > 0
        # clear all previous annotations
        while self.rowCount() > 0:
            self.removeRow(self.rowCount()-1)

        # reset the annotations
        self.__data = []
        for idx, annotation in enumerate(annotations):
            insertedRow = self.insertRow(idx)
            if not insertedRow:
                self.rowInsertErrorSignal(f"Cannot insert row at index {idx}th")

            setStatement = self.setData(self.index(idx, 0, QModelIndex()),
                                      annotation["statement"], self.STATEMENT)
            if not setStatement:
                self.setContextErrorSignal.emit(f"Cannot set statement for annotation {idx}th")

            setVerdict = self.setData(self.index(idx, 0, QModelIndex()),
                                      annotation["verdict"], self.VERDICT)
            if not setVerdict:
                self.setContextErrorSignal.emit(f"Cannot set verdict for annotation {idx}th")

            setEvidence = self.setData(self.index(idx, 0, QModelIndex()),
                                      annotation["evidence"], self.EVIDENCE)
            if not setEvidence:
                self.setContextErrorSignal.emit(f"Cannot set evidence for annotation {idx}th")
    
    @Slot(int)
    def addAnnotation(self, idx: int) -> bool:
        return self.insertRow(idx+1)
    
    @Slot(int)
    def removeAnnotation(self, idx: int) -> bool:
        return self.removeRow(idx)
