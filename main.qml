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

        Rectangle {
            id: leftArrow
            width: parent.width * 0.05
            height: parent.height
            anchors {
                left: parent.left
            }
            color: "transparent"

            MouseArea {
                id: leftArrowMouseArea
                hoverEnabled: true
                onEntered: {
                    leftArrowIconContainer.border.color = "#9c9c9c"
                    leftArrowIconContainer.border.width = 2
                }
                onExited: leftArrowIconContainer.border.color = "transparent"
                onClicked: backend.previousAnnotation()
                anchors.fill: parent
            }

            Rectangle {
                id: leftArrowIconContainer
                width: parent.width
                height: width
                anchors {
                    verticalCenter: parent.verticalCenter
                    horizontalCenter: parent.horizontalCenter
                    // margins: 5
                }
                radius: 50

                Image {
                    id: leftArrowIcon
                    source: "media/icons/left-arrow.png"
                    anchors {
                        fill: parent
                        centerIn: parent
                        margins: 10
                    }
                    fillMode: Image.PreserveAspectFit
                }
            }
        }

        Rectangle {
            id: rightArrow
            width: parent.width * 0.05
            height: parent.height
            anchors {
                right: parent.right
            }
            color: "transparent"

            MouseArea {
                id: rightArrowMouseArea
                hoverEnabled: true
                onEntered: {
                    rightArrowIconContainer.border.color = "#9c9c9c"
                    rightArrowIconContainer.border.width = 2
                }
                onExited: rightArrowIconContainer.border.color = "transparent"
                onClicked: backend.nextAnnotation()
                anchors.fill: parent
            }

            Rectangle {
                id: rightArrowIconContainer
                width: parent.width
                height: width
                radius: 50
                anchors {
                    verticalCenter: parent.verticalCenter
                    horizontalCenter: parent.horizontalCenter
                    // margins: 5
                }

                Image {
                    id: rightArrowIcon
                    source: "media/icons/right-arrow.png"
                    anchors {
                        fill: parent
                        centerIn: parent
                        margins: 10
                    }
                    fillMode: Image.PreserveAspectFit
                }
            }
        }

        ScrollView {
            id: scrollView
            width: parent.width * 0.9
            height: parent.height
            ScrollBar.vertical.policy: ScrollBar.AlwaysOff
            anchors {
                horizontalCenter: parent.horizontalCenter
            }

            ListView {
                model: annotationModel
                anchors {
                    fill: parent
                    centerIn: parent
                }
                delegate: AnnotationItem {
                    parentWidth: scrollView.width

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
}
