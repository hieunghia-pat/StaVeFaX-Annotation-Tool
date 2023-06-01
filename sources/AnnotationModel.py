from typing import Optional, Union, Any, Dict

from PySide6.QtCore import Qt, QObject, QAbstractListModel, QModelIndex, QPersistentModelIndex, Signal, Slot, Property, QByteArray

from sources.Annotation import Annotation

class AnnotationModel(QAbstractListModel):
	# defined the roles
	STATEMENT = Qt.UserRole
	VERDICT = Qt.UserRole + 1
	EVIDENCE = Qt.UserRole + 2
	START = Qt.UserRole + 3
	END = Qt.UserRole + 4

	# signals
	rowInsertErrorSignal = Signal(str)
	setStatementErrorSignal = Signal(str)
	setVerdictErrorSignal = Signal(str)
	setEvidenceErrorSignal = Signal(str)
	contextChanged = Signal()
	annotationUpdated = Signal(list)
	selectedIndexChanged = Signal()
	startedLoadingAnnotation = Signal()
	finishedLoadingAnnotation = Signal()

	def __init__(self, parent: Optional[QObject] = ...) -> None:
		super().__init__()

		self.__context = "Context is unavailable"
		self.__data = [Annotation({
			"statement": "",
			"verdict": 1,
			"evidence": "Evidence is unavailable",
			"start": 0,
			"end": 0
		})]
		self.__selectedIndex = 0

	@Property(int)
	def selectedIndex(self) -> int:
		return self.__selectedIndex

	@selectedIndex.setter
	def selectedIndex(self, index: int) -> None:
		self.__selectedIndex = index
		self.selectedIndexChanged.emit()

	def __len__(self):
		return len(self.__data)

	def rowCount(self, parent: Union[QModelIndex, QPersistentModelIndex] = ...) -> int:
		return len(self.__data)

	@Property(str)
	def context(self) -> str:
		start_index = self.__data[self.__selectedIndex].startIndex
		end_index = self.__data[self.__selectedIndex].endIndex
		if start_index == end_index:
			return self.__context
		context = list(self.__context)
		context.insert(start_index, "<strong>")
		context.insert(end_index+1, "</strong>")

		context = "".join(context)
		passages = context.split("\n\n")
		passages = [f"<p>{passage}</p>" for passage in passages]
		passages = "".join(passages)

		return passages

	def data(self, index: Union[QModelIndex, QPersistentModelIndex], role: int = ...) -> Any:
		if not index.isValid():
			return None

		if role == self.STATEMENT:
			return self.__data[index.row()].statement

		if role == self.VERDICT:
			return self.__data[index.row()].verdict

		if role == self.EVIDENCE:
			return self.__data[index.row()].evidence

		if role == self.START:
			return self.__data[index.row()].startIndex

		if role == self.END:
			return self.__data[index.row()].endIndex

		return None

	def setData(self, index: Union[QModelIndex, QPersistentModelIndex], value: Any, role: int = ...) -> bool:
		if not index.isValid():
			return False

		if role == self.STATEMENT:
			self.__data[index.row()].setStatement(str(value))
			self.dataChanged.emit(index, index, (Qt.EditRole, Qt.DisplayRole))
			self.annotationUpdated.emit(self.__data)
			return True

		if role == self.VERDICT:
			self.__data[index.row()].setVerdict(int(value))
			self.dataChanged.emit(index, index, (Qt.EditRole, Qt.DisplayRole))
			self.annotationUpdated.emit(self.__data)
			return True

		if role == self.EVIDENCE:
			self.__data[index.row()].setEvidence(str(value))
			self.dataChanged.emit(index, index, Qt.DisplayRole)
			self.annotationUpdated.emit(self.__data)
			return True

		if role == self.START:
			self.__data[index.row()].setStartIndex(int(value))
			self.dataChanged.emit(index, index, Qt.DisplayRole)
			self.annotationUpdated.emit(self.__data)
			return True

		if role == self.END:
			self.__data[index.row()].setEndIndex(int(value))
			self.dataChanged.emit(index, index, Qt.DisplayRole)
			self.annotationUpdated.emit(self.__data)
			return True

		return False

	def insertRow(self, row: int, parent: QModelIndex=QModelIndex()) -> bool:
		if row < 0 or row > len(self):
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
			self.EVIDENCE: b"evidence",
			self.START: b"start",
			self.END: b"end"
		}

	def flags(self, index: Union[QModelIndex, QPersistentModelIndex]) -> Qt.ItemFlag:
		if not index.isValid():
			return Qt.NoItemFlags

		return super().flags(index) | Qt.ItemIsEditable

	@property
	def annotations(self):
		return [annotation.annotation for annotation in self.__data]

	@Slot(dict)
	def setAnnotations(self, annotation: dict) -> bool:
		self.startedLoadingAnnotation.emit()
		# clear all previous annotations
		while self.rowCount() > 0:
			self.removeRow(0)

		# reset the annotations
		self.__context = annotation["context"]
		self.contextChanged.emit()

		for idx, item in enumerate(annotation["information"]):
			insertedRow = self.insertRow(idx)
			if not insertedRow:
				self.rowInsertErrorSignal.emit(f"Cannot insert row at index {idx}th")
				raise Exception(f"Cannot insert row at index {idx}th")
				return False

			setStatement = self.setData(self.index(idx, 0, QModelIndex()), item["statement"], self.STATEMENT)
			if not setStatement:
				self.setStatementErrorSignal.emit(f"Cannot set statement for information {idx}th")
				raise Exception(f"Cannot set statement for information {idx}th")
				return False

			setVerdict = self.setData(self.index(idx, 0, QModelIndex()), item["verdict"], self.VERDICT)
			if not setVerdict:
				self.setStatementErrorSignal.emit(f"Cannot set verdict for information {idx}th")
				raise Exception(f"Cannot set verdict for information {idx}th")
				return False

			setEvidence = self.setData(self.index(idx, 0, QModelIndex()), item["evidence"], self.EVIDENCE)
			if not setEvidence:
				self.setStatementErrorSignal.emit(f"Cannot set evidence for information {idx}th")
				raise Exception(f"Cannot set evidence for information {idx}th")
				return False

			setStartIndex = self.setData(self.index(idx, 0, QModelIndex()), item["start"], self.START)
			if not setStartIndex:
				raise Exception(f"Cannot set starting index for information {idx}th")
				return False

			setEndIndex = self.setData(self.index(idx, 0, QModelIndex()), item["end"], self.END)
			if not setEndIndex:
				raise Exception(f"Cannot set ending index for information {idx}th")
				return False

		self.finishedLoadingAnnotation.emit()

		return True

	@Slot(int)
	def addAnnotation(self, idx: int) -> bool:
		return self.insertRow(idx+1)

	@Slot(int)
	def removeAnnotation(self, idx: int) -> bool:
		return self.removeRow(idx)
