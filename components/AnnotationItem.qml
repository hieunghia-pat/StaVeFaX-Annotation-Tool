import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Rectangle {
    property int parentWidth

    signal updateFocus(isFocus: bool)

    id: annotationItemContainer
    width: parentWidth
    height: 200
    border {
        width: 1
        color: "#d6d6d6"
    }
    radius: 23

    Connections {
        target: annotationItemContainer
        function onUpdateFocus(isFocus) {
            if (isFocus) {
                annotationItemContainer.border.color = "#c2c2c2"
                annotationItemContainer.border.width = 2
                annotationModel.selectedIndex = index
            }
            else {
                annotationItemContainer.border.color = "#d6d6d6"
                annotationItemContainer.border.width = 1
            }
        }
    }

    MouseArea {
        id: mouseArea
        anchors.fill: parent
        hoverEnabled: true
        propagateComposedEvents: true
    }

    Column {
        id: columnLayout
        anchors {
            fill: parent
            centerIn: parent
        }
        spacing: 15

        Rectangle {
            id: labelContainer
            width: parent.width
            height: label.implicitHeight
            color: "transparent"
            Label {
                id: label
                anchors {
                    fill: parent
                    centerIn: parent
                }
                text: "Annotation " + (index+1)
                topPadding: 7
                leftPadding: 15
            }
        }

        Rectangle {
            id: statementContainer
            width: annotationItemContainer.width
            height: 30
            color: "transparent"
            
            Rectangle {
                width: parent.width - 20
                height: parent.height
                anchors {
                    centerIn: parent
                    horizontalCenter: parent.horizontalCenter
                }
                border {
                    color: "#cbccca"
                    width: 1
                }
                radius: 23
                anchors {
                    horizontalCenter: parent.horizontalCenter
                }

                TextEdit {
                    id: statementTextLine
                    width: parent.width
                    height: parent.height
                    leftPadding: 10
                    verticalAlignment: TextEdit.AlignVCenter
                    anchors {
                        fill: parent
                        centerIn: parent
                    }

                    text: statement
                    font {
                        pointSize: 13
                    }

                    onFocusChanged: isFocus => updateFocus(isFocus)
                    onTextChanged: {
                        statement = text
                    }
                }
            }
        }

        Rectangle {
            id: verdictContainer
            width: verdict.width
            height: verdict.height
            color: "transparent"

            ComboBox {
                id: verdict
                width: implicitWidth
                height: implicitHeight
                anchors {
                    horizontalCenter: parent.horizontalCenter
                }
                model: ["SUPPORTED", "NEI", "REFUTED"]
                currentIndex: 1
                onFocusChanged: isFocus => updateFocus(isFocus)
            }
        }

        Rectangle {
            id: evidenceContainer
            width: annotationItemContainer.width
            height: 30
            color: "transparent"
            
            Rectangle {
                width: parent.width - 20
                height: parent.height
                border {
                    color: "#cbccca"
                    width: 1
                }
                radius: 23
                anchors {
                    horizontalCenter: parent.horizontalCenter
                    verticalCenter: parent.verticalCenter
                }
                border {
                    width: 1
                    color: "blue"
                }

                ScrollView {
                    anchors {
                        fill: parent
                        centerIn: parent
                    }
                    ScrollBar.horizontal.policy: ScrollBar.AlwaysOff
                    ScrollBar.vertical.policy: ScrollBar.AlwaysOff
                    ScrollBar.horizontal.interactive: true
                    ScrollBar.vertical.interactive: true

                    TextEdit {
                        id: evidenceText
                        text: evidence
                        font {
                            pointSize: 13
                        }
                        readOnly: true
                        enabled: true
                        wrapMode: TextEdit.WrapAnywhere
                        horizontalAlignment: TextEdit.AlignJustify
                        verticalAlignment: TextEdit.AlignVCenter
                        topPadding: 7
                        leftPadding: 10
                        anchors {
                            fill: parent
                            centerIn: parent
                        }
                    }
                }
            }
        }
    }
}