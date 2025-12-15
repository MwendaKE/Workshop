#include <QApplication>   // Core application class
#include <QWidget>        // Base class for all windows
#include <QPushButton>    // Button widget
#include <QMessageBox>    // Simple popup message box

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);  // Initialize the Qt application

    QWidget window;                // Create a main window
    window.setWindowTitle("Hello Qt Button");  // Set the window title
    window.resize(300, 200);      // Set window size

    QPushButton button("Click Me!", &window);  // Create a button inside the window
    button.setGeometry(80, 80, 140, 40);       // Set button position and size

    // Connect button click to a popup message
    QObject::connect(&button, &QPushButton::clicked, [&](){
        QMessageBox::information(&window, "Message", "Hello, Qt5!");
    });

    window.show();   // Show the window

    return app.exec();  // Run the application event loop
}
