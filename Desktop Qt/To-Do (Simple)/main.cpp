// Include the QApplication class — every Qt GUI app must have one
#include <QApplication>

// Include our custom window class definition
#include "mainwindow.h"

// The main function — this is where every C++ program begins
int main(int argc, char *argv[]) {
    // Create a QApplication object
    // This object manages app-wide settings, event handling, and GUI control
    QApplication app(argc, argv);

    // Create an instance of our main window (the To-Do list window)
    MainWindow window;

    // Show the window on the screen
    window.show();

    // Start the app's event loop — this keeps the window responsive
    // The app will keep running until the user closes it
    return app.exec();
}

