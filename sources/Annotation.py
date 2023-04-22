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
            "evidence": ""
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
