#include <QApplication>
#include "mainwindow.h"

// Entry point of the app
int main(int argc, char *argv[]) {
    QApplication app(argc, argv);

    MainWindow window;   // Create main window
    window.show();       // Display it

    return app.exec();   // Run the Qt event loop
}

