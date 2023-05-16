import QtQuick
import QtQuick.Controls

Rectangle {
    id: passageContainer

    border {
        width: 2
        color: "red"
    }

    TextArea {
        id: contextTextArea
        anchors {
            fill: parent
            centerIn: parent
        }
        readOnly: true
        selectByMouse: true
        mouseSelectionMode: TextEdit.SelectWords
        wrapMode: TextEdit.WordWrap
        horizontalAlignment: TextEdit.AlignJustify
        text: annotationModel.context
        textFormat: TextEdit.PlainText
        padding: 5
        font {
            pointSize: 23
        }
        
        onSelectedTextChanged: {
            annotationModel.setSelectionIndices(selectionStart, selectionEnd)
            annotationModel.setEvidence(selectedText)
        }

        Connections {
            target: annotationModel
            
            function onContextChanged() {
                contextTextArea.text = annotationModel.context
            }

            function onSelectionChanged() {
                contextTextArea.text = annotationModel.context
            }
        }
    }
}