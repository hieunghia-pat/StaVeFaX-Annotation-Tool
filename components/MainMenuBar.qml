import QtQuick
import QtQuick.Controls

MenuBar {
    property var openFileDialog

    Menu {
        title: qsTr("&File")

        Action {
            id: openAction
            text: qsTr("&Open")
            shortcut: StandardKey.Open
            icon {
                source: "../media/icons/open-icon.png"
            }
            onTriggered: openFileDialog.open()
        }

        Action {
            id: saveAction
            text: qsTr("&Save")
            shortcut: StandardKey.Save
            icon {
                source: "../media/icons/save-icon.png"
            }
            enabled: false
            onTriggered: {
                backend.saveData()
                saveAction.enabled = false
                undoAction.enabled = false
                redoAction.enabled = false
                cutAction.enabled = false
                copyAction.enabled = false
                pasteAction.enabled = false
            }
        }

        Action {
            id: closeAction
            text: qsTr("&Close")
            shortcut: StandardKey.Close
            icon {
                source: "../media/icons/close-icon.png"
            }
            onTriggered: {
                mainWindow.close()
            }
        }
    }

    Menu {
        title: qsTr("&Edit")

        Action {
            id: undoAction
            text: qsTr("&Undo")
            shortcut: StandardKey.Undo
            enabled: false
            icon {
                source: "../media/icons/undo-icon.png"
            }
            onTriggered: {

            }
        }

        Action {
            id: redoAction
            text: qsTr("&Redo")
            shortcut: StandardKey.Redo
            enabled: false
            icon {
                source: "../media/icons/redo-icon.png"
            }
            onTriggered: {

            }
        }

        Action {
            id: cutAction
            text: qsTr("&Cut")
            shortcut: StandardKey.Cut
            enabled: false
            icon {
                source: "../media/icons/cut-icon.png"
            }
            onTriggered: {

            }
        }

        Action {
            id: copyAction
            text: qsTr("&Copy")
            shortcut: StandardKey.Copy
            enabled: false
            icon {
                source: "../media/icons/copy-icon.png"
            }
            onTriggered: {

            }
        }

        Action {
            id: pasteAction
            text: qsTr("&Paste")
            shortcut: StandardKey.Paste
            enabled: false
            icon {
                source: "../media/icons/paste-icon.png"
            }
            onTriggered: {

            }
        }
    }

    Connections {
        target: annotationModel

        function onAnnotationUpdated() {
            saveAction.enabled = true
            undoAction.enabled = true
            redoAction.enabled = true
            cutAction.enabled = true
            copyAction.enabled = true
            pasteAction.enabled = true
        }
    }
}
