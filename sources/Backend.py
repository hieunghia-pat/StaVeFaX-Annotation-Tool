import json
from typing import Dict

from PySide6.QtCore import QObject, Signal, Slot

class Backend(QObject):
    fileNotFoundSignal = Signal(str)
    loadedAnnotations = Signal(Dict)

    def __init__(self, parent: QObject = QObject()) -> None:
        super().__init__(parent)

        # internal properties
        self.__data = []
        self.__currentIdx = 0

    def __len__(self) -> int:
        return len(self.__data)
    
    def annotations(self, idx: int = None):
        if idx is None:
            return self.__data[self.__currentIdx]

        return self.__data[idx]

    @Slot(str)
    def loadData(self, path: str) -> bool:
        try:
            tmpData = json.load(open(path, "r"))
        except FileNotFoundError as error:
            self.fileNotFoundSignal.emit(error.strerror)
            return False

        self.__data = tmpData
        self.loadedAnnotations.emit(self.__data[self.__currentIdx])

        return True

    @Slot()
    def nextAnnotation(self) -> None:
        if self.__currentIdx == len(self) - 1:
            return
        
        self.__currentIdx += 1
        self.loadedAnnotation(self.__data[self.__currentIdx])

    @Slot()
    def previousAnnotation(self) -> None:
        if self.__currentIdx < 0:
            self.__currentIdx = 0
            return

        self.__currentIdx -= 1
        self.loadedAnnotations(self.__data[self.__currentIdx])