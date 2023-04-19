from PySide6.QtCore import QObject, Property

class Annotation(QObject):
    label2idx = {
        "REFUTED": -1,
        "NEI": 0,
        "SUPPORTED": 1
    }
    idx2label = {value: key for key, value in label2idx.items()}

    def __init__(self, annotation: dict):
        super().__init__()

        self.__annotation = annotation

    @property
    def annotation(self):
        return self.__annotation

    @Property(str)
    def context(self) -> str:
        print("In Annotation::context")
        return self.__annotation["context"]
    
    @context.setter
    def context(self, value: str) -> None:
        self.__annotation["context"] = value

    @Property(str)
    def statement(self) -> str:
        print("In Annotation::statement")
        return self.__annotation["statement"]
    
    @statement.setter
    def statement(self, value: str) -> None:
        self.__annotation["statement"] = value

    @Property(int)
    def verdict(self) -> int:
        return self.label[self.__annotation["verdict"]] if self.__annotation is not None else 0
    
    @verdict.setter
    def verdict(self, value: int) -> None:
        self.__annotation["verdict"] = self.idx2label[value]

    @Property(str)
    def evidence(self) -> str:
        return self.__annotation["evidence"] if self.__annotation is not None else ""
    
    @evidence.setter
    def evidence(self, value: str) -> None:
        self.__annotation["evidence"] = value
