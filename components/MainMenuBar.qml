import QtQuick
import QtQuick.Controls

MenuBar {
    property var openFileDialog

    Menu {
        title: qsTr("&File")
        
        Action {
            text: qsTr("&Open")
            shortcut: StandardKey.Open
            icon {
                source: "../media/icons/open-icon.png"
            }
            onTriggered: openFileDialog.open()
        }

        Action {
            text: qsTr("&Save")
            shortcut: StandardKey.Save
            icon {
                source: "../media/icons/save-icon.png"
            }
            onTriggered: {
                console.log("Saving file ...")
                backend.saveData()
            }
        }

        Action {
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
            text: qsTr("&Undo")
            shortcut: StandardKey.Undo
            icon {
                source: "../media/icons/undo-icon.png"
            }
            onTriggered: {

            }
        }

        Action {
            text: qsTr("&Redo")
            shortcut: StandardKey.Redo
            icon {
                source: "../media/icons/redo-icon.png"
            }
            onTriggered: {

            }
        }
        
        Action {
            text: qsTr("&Cut")
            shortcut: StandardKey.Cut
            icon {
                source: "../media/icons/cut-icon.png"
            }
            onTriggered: {
                
            }
        }

        Action {
            text: qsTr("&Copy")
            shortcut: StandardKey.Copy
            icon {
                source: "../media/icons/copy-icon.png"
            }
            onTriggered: {

            }
        }

        Action {
            text: qsTr("&Paste")
            shortcut: StandardKey.Paste
            icon {
                source: "../media/icons/paste-icon.png"
            }
            onTriggered: {

            }
        }
    }
}
