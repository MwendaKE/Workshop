#include <QApplication>
#include "mainwindow.h"

// Entry point of the application
int main(int argc, char *argv[]) {
    QApplication app(argc, argv);   // Create Qt application
    MainWindow window;              // Create main window object
    window.show();                  // Display the main window
    return app.exec();              // Start the event loop
}

