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

        // text: annotationModel.context
        text: "This is a sample paragraph"
        padding: 5
        font {
            pointSize: 23
        }
    }
}