import QtQuick
import QtQuick.Controls

TextArea {
    id: passageContainer

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