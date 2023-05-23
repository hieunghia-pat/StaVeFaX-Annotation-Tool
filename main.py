import sys
from pathlib import Path

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

from sources.AnnotationModel import AnnotationModel
from sources.Backend import Backend

if __name__ == "__main__":
	app = QGuiApplication(sys.argv)

	backend = Backend(app)
	annotationModel = AnnotationModel()

	engine = QQmlApplicationEngine()

	engine.rootContext().setContextProperty("backend", backend)
	engine.rootContext().setContextProperty("annotationModel", annotationModel)
	
	backend.loadedAnnotations.connect(annotationModel.setAnnotations)
	annotationModel.annotationUpdated.connect(backend.updateAnnotation)

	qml_file = Path(__file__).resolve().parent / "main.qml"
	engine.load(qml_file)

	if not engine.rootObjects():
		sys.exit(-1)

	sys.exit(app.exec())
