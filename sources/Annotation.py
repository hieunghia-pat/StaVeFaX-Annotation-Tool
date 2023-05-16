from PySide6.QtCore import QObject

class Annotation(QObject):
    label2idx = {
        "REFUTED": -1,
        "NEI": 0,
        "SUPPORTED": 1
    }
    idx2label = {value: key for key, value in label2idx.items()}

    def __init__(self, annotation: dict=None):
        super().__init__()

        self.__annotation = annotation if annotation is not None else {
            "statement": "",
            "verdict": 1,
            "evidence": "",
            "selectionStart": 0,
            "selectionEnd": 0
        }

    @property
    def annotation(self):
        return self.__annotation

    @property
    def statement(self) -> str:
        return self.__annotation["statement"]
    
    def setStatement(self, value: str) -> None:
        self.__annotation["statement"] = value

    @property
    def verdict(self) -> int:
        return self.label[self.__annotation["verdict"]] if self.__annotation is not None else 0
    
    def setVerdict(self, value: int) -> None:
        self.__annotation["verdict"] = self.idx2label[value]

    @property
    def evidence(self) -> str:
        return self.__annotation["evidence"] if self.__annotation is not None else ""

    def setEvidence(self, value: str) -> None:
        self.__annotation["evidence"] = value

    @property
    def selectionStart(self) -> int:
        return self.__annotation["selectionStart"]

    def setSelectionStart(self, value: int) -> None:
        self.__annotation["selectionStart"] = value

    @property
    def selectionEnd(self) -> int:
        return self.__annotation["selectionEnd"]
    
    def setSelectionEnd(self, value: int) -> None:
        self.__annotation["selectionEnd"] = value
