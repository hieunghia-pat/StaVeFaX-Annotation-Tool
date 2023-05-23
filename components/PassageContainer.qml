import QtQuick
import QtQuick.Controls
import QtQml

Rectangle {
    id: passageContainer

    width: (parent.width / 2) - 5
    height: parent.height - 10
    anchors {
        left: parent.left
        top: parent.top
        margins: 5
    }

    ScrollView {
        id: scrollView
        anchors {
            fill: parent
            centerIn: parent
        }
        ScrollBar.vertical.policy: ScrollBar.AlwaysOff

        TextArea {
            id: contextText
            width: parent.width - 10
            height: parent.height
            implicitWidth: contentWidth
            implicitHeight: contentHeight + 10
            readOnly: true
            selectByMouse: true
            mouseSelectionMode: TextEdit.SelectWords
            wrapMode: TextEdit.WordWrap
            horizontalAlignment: TextEdit.AlignJustify
            text: annotationModel.context
            textFormat: TextEdit.PlainText
            font {
                pointSize: 23
            }

            padding: 5
            onSelectedTextChanged: annotationModel.setEvidence(selectedText)

            Connections {
                target: annotationModel
                
                function onContextChanged() {
                    contextText.text = annotationModel.context
                }
            }
        }
    }
}
