import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Rectangle {
    property int parentWidth

    signal updateFocus(isFocus: bool)

    id: annotationItemContainer
    width: parentWidth
    height: columnLayout.height + 30
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
        width: parent.width
        height: implicitHeight
        anchors {
            centerIn: parent
        }
        spacing: 15

        Rectangle {
            id: labelContainer
            width: parent.width
            height: label.height + 10
            color: "transparent"
            Label {
                id: label
                width: parent.width
                height: implicitHeight
                text: "Annotation " + (index+1)
                leftPadding: 7
                anchors {
                    verticalCenter: parent.verticalCenter
                }
                font {
                    pointSize: 17
                }
            }
        }

        Rectangle {
            id: statementContainer
            width: annotationItemContainer.width
            height: statementWrapper.height
            color: "transparent"
            
            Rectangle {
                id: statementWrapper
                width: parent.width - 20
                height: statementTextLine.height + 10
                anchors {
                    centerIn: parent
                    horizontalCenter: parent.horizontalCenter
                }
                border {
                    color: "#cbccca"
                    width: 1
                }
                radius: 17
                anchors {
                    horizontalCenter: parent.horizontalCenter
                }

                TextInput {
                    id: statementTextLine
                    width: parent.width
                    height: implicitHeight
                    leftPadding: 10
                    verticalAlignment: TextEdit.AlignVCenter
                    anchors {
                        horizontalCenter: parent.horizontalCenter
                        verticalCenter: parent.verticalCenter
                    }

                    text: statement
                    font {
                        pointSize: 17
                    }

                    onFocusChanged: isFocus => updateFocus(isFocus)
                    onTextChanged: annotationModel.setStatement(text)
                }
            }
        }

        Rectangle {
            id: verdictContainer
            width: parent.width
            height: verdict.height
            color: "transparent"

            Rectangle {
                id: verdictWrapper
                anchors {
                    fill: parent
                    centerIn: parent
                    verticalCenter: parent.verticalCenter
                    horizontalCenter: parent.horizontalCenter
                    margins: 7
                }

                ComboBox {
                    id: verdict
                    width: implicitWidth
                    height: implicitHeight
                    anchors {
                        verticalCenter: parent.verticalCenter
                        margins: 50
                    }
                    model: ["SUPPORTED", "NEI", "REFUTED"]
                    currentIndex: 1
                    onFocusChanged: isFocus => updateFocus(isFocus)
                }
            }
        }

        Rectangle {
            id: evidenceContainer
            width: annotationItemContainer.width
            height: evidenceTextContainer.height
            color: "transparent"
            
            Rectangle {
                id: evidenceTextContainer
                width: parent.width - 20
                height: evidenceText.height + 20
                border {
                    color: "#cbccca"
                    width: 1
                }
                radius: 17
                anchors {
                    horizontalCenter: parent.horizontalCenter
                }

                Text {
                    id: evidenceText
                    text: evidence
                    font {
                        pointSize: 17
                    }
                    width: parent.width - 5
                    height: implicitHeight
                    wrapMode: TextEdit.WrapAnywhere
                    horizontalAlignment: TextEdit.AlignJustify
                    verticalAlignment: TextEdit.AlignVCenter
                    anchors.centerIn: parent
                    leftPadding: 7
                }
            }
        }
    }
}