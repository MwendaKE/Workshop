#include <QApplication>   // Required for all Qt GUI apps
#include "mainwindow.h"   // Include our MainWindow class

int main(int argc, char *argv[]) {
    QApplication app(argc, argv); // Create the application object

    MainWindow window;  // Create our main window
    window.show();      // Show the window on the screen

    return app.exec();  // Start the Qt event loop
}

