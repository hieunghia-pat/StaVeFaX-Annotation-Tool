pyinstaller main.py --windowed ^
    --add-data="sources\*;." ^
    --add-data="components\*;." ^
    --add-data="media\*;." ^
    --add-data="main.py;." ^
    --add-data="main.qml;." ^
    --icon=media\logo-uit.ico