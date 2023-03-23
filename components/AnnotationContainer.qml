import QtQuick
import QtQuick.Controls

GroupBox {
    property int index

    id: annotationContainer
    title: "Annotation " + index
    height: implicitHeight

    anchors.margins: 5

    Column {
        GroupBox {
            title: "Statement"
            width: implicitWidth
            height: implicitHeight
            anchors.margins: 5
            TextField {
                id: statementTextLine
                width: annotationContainer.width - 10
                height: implicitHeight

                // text: annotationModel.statement
                text: "statement"
                placeholderText: "Enter appropriate statement"
                font {
                    pointSize: 13
                }

                onTextChanged: {

                }
            }
        }

        GroupBox {
            title: "Verdict"
            height: implicitHeight
            anchors.margins: 5
            ComboBox {
                width: parent.width
                model: ["SUPPORTED", "NEI", "REFUTED"]

                onCurrentIndexChanged: {
                    
                }
            }
        }

        GroupBox {
            title: "Evidence"
            anchors.margins: 5
            TextField {
                id: evidenceTextLine
                width: annotationContainer.width - 10
                height: implicitHeight
                readOnly: true
                text: "This is the evidence"
                font {
                    pointSize: 13
                }
            }
        }
    }
    
}