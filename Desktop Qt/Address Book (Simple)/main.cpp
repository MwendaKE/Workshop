#include <QApplication>
#include "mainwindow.h"

int main(int argc, char *argv[]) {
    QApplication app(argc, argv); // Qt main application
    MainWindow window;             // Create main window
    window.show();                 // Display the window
    return app.exec();             // Start event loop
}

