import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ToolBar {
    property var openFileDialog

    function activateFeatures() {
        saveAction.enabled = true
        undoAction.enabled = true
        redoAction.enabled = true
        cutAction.enabled = true
        copyAction.enabled = true
        pasteAction.enabled = true
    }

    RowLayout {
        ToolButton {
            id: openButton
            icon {
                source: "../media/icons/open-icon.png"
            }
            onClicked: openFileDialog.open()
        }

        ToolButton {
            id: saveButton
            icon {
                source: "../media/icons/save-icon.png"
            }
            enabled: false
            onClicked: {
                backend.saveData()
                saveButton.enabled = false
                undoButton.enabled = false
                redoButton.enabled = false
                cutButton.enabled = false
                copyButton.enabled = false
                pasteButton.enabled = false
            }
        }

        ToolButton {
            id: undoButton
            icon {
                source: "../media/icons/undo-icon.png"
            }
            enabled: false
            onClicked: {

            }
        }

        ToolButton {
            id: redoButton
            icon {
                source: "../media/icons/redo-icon.png"
            }
            enabled: false
            onClicked: {

            }
        }

        ToolButton {
            id: cutButton
            icon {
                source: "../media/icons/cut-icon.png"
            }
            enabled: false
            onClicked: {

            }
        }

        ToolButton {
            id: copyButton
            icon {
                source: "../media/icons/copy-icon.png"
            }
            enabled: false
            onClicked: {

            }
        }

        ToolButton {
            id: pasteButton
            icon {
                source: "../media/icons/paste-icon.png"
            }
            enabled: false
            onClicked: {

            }
        }

        ToolButton {
            id: closeButton
            icon {
                source: "../media/icons/close-icon.png"
            }
            onClicked: {
                mainWindow.close()
            }
        }
    }

    Connections {
        target: annotationModel

        function onAnnotationUpdated() {
            saveButton.enabled = true
            undoButton.enabled = true
            redoButton.enabled = true
            cutButton.enabled = true
            copyButton.enabled = true
            pasteButton.enabled = true
        }
    }
}
