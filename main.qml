import QtQuick
import QtQuick.Controls
import QtQuick.Dialogs

import "components"

ApplicationWindow {
    id: mainWindow
    visible: true
    title: "Annotation Tool"
    width: Screen.width
    height: Screen.height
    color: "white"

    FileDialog {
        id: openFileDialog
        onAccepted: {
            backend.loadData(selectedFile)
        }
    }

    menuBar: MainMenuBar {
        openFileDialog: openFileDialog
    }

    header: MainToolBar {
        openFileDialog: openFileDialog
    }

    Row {
        id: contentContainer

        anchors {
            fill: parent
            centerIn: parent
            topMargin: 10
        }

        PassageContainer {
            width: (parent.width / 2) - 10
            height: parent.height
            context: annotationModel.context
        }

        Rectangle {
            property int selectedIndex: 0
            
            id: annotationContainer
            color: "white"
            width: (parent.width / 2) - 10
            height: parent.height

            ListView {
                model: annotationModel
                anchors {
                    fill: parent
                    centerIn: parent
                }
                delegate: AnnotationItem {
                    parentWidth: annotationContainer.width
                    index: index
                }
                spacing: 10
            }
        }

        spacing: 5
    }

}