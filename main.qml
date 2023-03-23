import QtQuick
import QtQuick.Controls

import "components"

ApplicationWindow {
    id: mainWindow
    visible: true
    title: "Annotation Tool"
    width: Screen.width
    height: Screen.height

    menuBar: MainMenuBar {

    }

    header: MainToolBar {
        
    }

    Row {
        id: contentContainer

        anchors {
            fill: parent
            centerIn: parent
        }

        PassageContainer {
            width: parent.width / 2 - 10
            height: parent.height

        }

        AnnotationContainer {
            width: (parent.width / 2) - 10
            height: parent.height
        }
    }

}