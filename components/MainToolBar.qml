import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ToolBar {
    property var openFileDialog

    RowLayout {
        ToolButton {
            icon {
                source: "../media/icons/open-icon.png"
            }
            onClicked: openFileDialog.open()
        }

        ToolButton {
            icon {
                source: "../media/icons/save-icon.png"
            }
            onClicked: backend.saveData()
        }

        ToolButton {
            icon {
                source: "../media/icons/undo-icon.png"
            }
            onClicked: {

            }
        }

        ToolButton {
            icon {
                source: "../media/icons/redo-icon.png"
            }
            onClicked: {

            }
        }

        ToolButton {
            icon {
                source: "../media/icons/cut-icon.png"
            }
            onClicked: {

            }
        }

        ToolButton {
            icon {
                source: "../media/icons/copy-icon.png"
            }
            onClicked: {

            }
        }

        ToolButton {
            icon {
                source: "../media/icons/paste-icon.png"
            }
            onClicked: {

            }
        }

        ToolButton {
            icon {
                source: "../media/icons/close-icon.png"
            }
            onClicked: {
                mainWindow.close()
            }
        }
    }
}