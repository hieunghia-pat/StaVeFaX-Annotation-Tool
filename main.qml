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

    MouseArea {
        id: mainMouseArea
        anchors {
            fill: parent
            centerIn: parent
        }

        cursorShape: Qt.ArrowCursor
    }

    FileDialog {
        id: openFileDialog
        onAccepted: {
            backend.loadData(selectedFile)
        }

        nameFilters: [ "Json files (*.json)"]
    }

    NotificationDialog {
        id: notificationDialog
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

                    Connections {
                        target: MainMenuBar

                        function onCutSignal() {

                        }
                    }
                }
                spacing: 10
            }
        }
    }

    Connections {
        target: backend

        function onFileNotFoundSignal(error: str) {
            notificationDialog.title = "Error"
            notificationDialog.text = error
            notificationDialog.open()
        }

        function onOpeningFileErrorSignal(error: str) {
            notificationDialog.title = "Error"
            notificationDialog.text = error
            notificationDialog.open()
        }
    }

    Connections {
        target: annotationModel

        function onStartedLoadingAnnotation() {
            mainMouseArea.cursorShape = Qt.WaitCursor
        }

        function onFinishedLoadingAnnotation() {
            mainMouseArea.cursorShape = Qt.ArrowCursor
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
