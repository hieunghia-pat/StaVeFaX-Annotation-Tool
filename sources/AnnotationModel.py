from typing import Optional, Union, Any, List, Dict

from PySide6.QtCore import Qt, QObject, QAbstractListModel, QModelIndex, QPersistentModelIndex, Signal, Slot, Property, QByteArray

from sources.Annotation import Annotation

class AnnotationModel(QAbstractListModel):
    # defined the roles
    CONTEXT = Qt.UserRole
    STATEMENT = Qt.UserRole + 1
    VERDICT = Qt.UserRole + 2
    EVIDENCE = Qt.UserRole + 3

    # signals
    rowInsertErrorSignal = Signal(str)
    setContextErrorSignal = Signal(str)
    setStatementErrorSignal = Signal(str)
    setVerdictErrorSignal = Signal(str)
    setEvidenceErrorSignal = Signal(str)

    def __init__(self, parent: Optional[QObject] = ...) -> None:
        super().__init__()

        self.__data = [Annotation()]
        self.__selectedIndex = 0

    def __len__(self):
        return len(self.__data)

    def rowCount(self, parent: Union[QModelIndex, QPersistentModelIndex] = ...) -> int:
        return len(self.__data)
    
    def data(self, index: Union[QModelIndex, QPersistentModelIndex], role: int = ...) -> Any:
        if not index.isValid():
            return None
        
        if role == self.CONTEXT:
            return self.__data[index.row()].context
        
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
        
        if role == self.CONTEXT:
            self.__data[index.row()].context(str(value))
            self.dataChanged.emit(index, index)
            return True

        if role == self.STATEMENT:
            self.__data[index.row()].statement(str(value))
            self.dataChanged.emit(index, index)
            return True
        
        if role == self.VERDICT:
            self.__data[index.row()].verdict(int(value))
            self.dataChanged.emit(index, index)
            return True
        
        if role == self.EVIDENCE:
            self.__data[index.row()].evidence(str(value))
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
            self.CONTEXT: "context",
            self.STATEMENT: "statement",
            self.VERDICT: "verdict",
            self.EVIDENCE: "evidence"

        }
    
    def flags(self, index: Union[QModelIndex, QPersistentModelIndex]) -> Qt.ItemFlag:
        if not index.isValid():
            return Qt.NoItemFlags
        
        return super().flags(index) | Qt.ItemIsEditable
    
    @property
    def annotations(self):
        return [annotation.annotation for annotation in self.__data]

    @Property
    def selectedIndex(self):
        return self.__selectedIndex
    
    @selectedIndex.setter
    def selectedIndex(self, value: int):
        self.__selectedIndex = value
    
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

            setContext = self.setData(self.index(idx, 0, QModelIndex()),
                                      annotation["context"], self.CONTEXT)
            if not setContext:
                self.setContextErrorSignal.emit(f"Cannot set context for annotation {idx}th")

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
