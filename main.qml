import QtQuick
import QtQuick.Controls

import "components"

ApplicationWindow {
    id: mainWindow
    visible: true
    title: "Annotation Tool"
    width: Screen.width
    height: Screen.height
    color: "white"

    menuBar: MainMenuBar {

    }

    header: MainToolBar {
        
    }

    Row {
        id: contentContainer

        anchors {
            fill: parent
            centerIn: parent
            topMargin: 10
        }

        PassageContainer {
            width: (parent.width / 2) - 10
            height: parent.height

        }

        Rectangle {
            property int selectedIndex: 0
            
            id: annotationContainer
            color: "white"
            width: (parent.width / 2) - 10
            height: parent.height

            ListView {
                model: 5
                anchors {
                    fill: parent
                    centerIn: parent
                }
                delegate: AnnotationItem {
                    parentWidth: annotationContainer.width
                    index: modelData
                    selectedIndex: selectedIndex
                }
                spacing: 10
            }
        }

        spacing: 5
    }

}