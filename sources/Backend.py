import json
import re

from PySide6.QtCore import QObject, Signal, Slot, QStandardPaths

class Backend(QObject):
	fileNotFoundSignal = Signal(str)
	openningFileErrorSignal = Signal(str)
	opennedFileSignal = Signal()
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
		path = re.sub("file://", "", path)
		try:
			tmpData = json.load(open(path, "r"))
		except FileNotFoundError as error:
			self.fileNotFoundSignal.emit(error.strerror)
			return False
		except Exception as error:
			self.openningFileErrorSignal.emit(error.strerror)

		self.__selectedPath = path
		self.__data = tmpData
		self.loadedAnnotations.emit(self.__data[self.__currentIdx])

		self.opennedFileSignal.emit()

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
