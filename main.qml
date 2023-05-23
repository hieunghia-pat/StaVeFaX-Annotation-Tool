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
    minimumWidth: 500
    minimumHeight: 500
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

    PassageContainer {

    }

    Rectangle {
        property int selectedIndex: 0
        
        id: annotationContainer
        color: "transparent"
        width: (parent.width / 2) - 5
        height: parent.height - 10
        anchors {
            right: parent.right
            top: parent.top
            margins: 5
        }

        ScrollView {
            anchors {
                fill: parent
                centerIn: parent
            }
            ScrollBar.vertical.policy: ScrollBar.AlwaysOff

            ListView {
                model: annotationModel
                anchors {
                    fill: parent
                    centerIn: parent
                }
                delegate: AnnotationItem {
                    parentWidth: annotationContainer.width
                }
                spacing: 10
            }
        }
    }

    Shortcut {
        id: nextAnnotationShortcut
        sequence: "Ctrl+Right"
        onActivated: backend.nextAnnotation()
        context: Qt.ApplicationShortcut
    }

    Shortcut {
        id: previousAnnotationShorcut
        sequence: "Ctrl+Left"
        onActivated: backend.previousAnnotation()
        context: Qt.ApplicationShortcut
    }

}
