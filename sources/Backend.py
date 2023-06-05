import json

from PySide6.QtCore import QObject, Signal, Slot, QStandardPaths, QUrl

class Backend(QObject):
	fileNotFoundSignal = Signal(str)
	openingFileErrorSignal = Signal(str)
	openedFileSignal = Signal()
	loadedAnnotations = Signal(dict)

	def __init__(self, parent: QObject = QObject()) -> None:
		super().__init__(parent)

		# internal properties
		self.__data = [{
			"context": "Context is not available",
			"information": [{
				"statement": "",
				"verdict": 1,
				"evidence": "Evidence is not available",
				"start": 0,
				"end": 0
			}]
		}]
		self.__currentIdx = 0
		self.__selectedPath: str = QStandardPaths.standardLocations(QStandardPaths.DocumentsLocation)[0]

	def __len__(self) -> int:
		return len(self.__data)

	def annotation(self, idx: int = None):
		if idx is None:
			return self.__data[self.__currentIdx]

		return self.__data[idx]

	@Slot(str)
	def loadData(self, path: str) -> bool:
		path = QUrl(path).toLocalFile()
		try:
			tmpData = json.load(open(path, "r", encoding="utf8"))
		except FileNotFoundError as error:
			error_message = f"Cannot find file or directory {path}"
			self.fileNotFoundSignal.emit(error_message)
			return False
		except Exception as error:
			error_message = f"Cannot open {path} because of {error}"
			self.openingFileErrorSignal.emit(error_message)
			return False

		self.__selectedPath = path
		self.__data = tmpData
		self.loadedAnnotations.emit(self.__data[self.__currentIdx])

		self.openedFileSignal.emit()

		return True

	@Slot(list)
	def updateAnnotation(self, annotations: list) -> None:
		self.__data[self.__currentIdx]["information"] = [annotation.annotation for annotation in annotations]

	@Slot()
	def saveData(self):
		json.dump(self.__data, open(self.__selectedPath, "w+"),
					ensure_ascii=False, indent=4)

	@Slot()
	def nextAnnotation(self) -> None:
		if self.__currentIdx == len(self) - 1:
			return

		self.saveData()

		self.__currentIdx += 1
		self.loadedAnnotations.emit(self.__data[self.__currentIdx])

	@Slot()
	def previousAnnotation(self) -> None:
		if self.__currentIdx == 0:
			return

		self.saveData()

		self.__currentIdx -= 1
		self.loadedAnnotations.emit(self.__data[self.__currentIdx])
