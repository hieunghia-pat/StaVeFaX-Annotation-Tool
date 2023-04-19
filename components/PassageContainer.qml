import QtQuick
import QtQuick.Controls

Rectangle {
    id: passageContainer

    TextArea {
        anchors {
            fill: parent
            centerIn: parent
        }
        readOnly: true
        selectByMouse: true
        mouseSelectionMode: TextEdit.SelectWords

        text: annotationModel.context
        padding: 5
        font {
            pointSize: 23
        }
        onSelectedTextChanged: {
            annotationModel.context = selectedText
        }
    }
}