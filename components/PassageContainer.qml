import QtQuick
import QtQuick.Controls

Rectangle {
    property string context

    id: passageContainer

    TextArea {
        anchors {
            fill: parent
            centerIn: parent
        }
        readOnly: true
        selectByMouse: true
        mouseSelectionMode: TextEdit.SelectWords

        text: context
        padding: 5
        font {
            pointSize: 23
        }
        onSelectedTextChanged: {
            annotationModel.setEvidence(selectedText)
        }
    }
}