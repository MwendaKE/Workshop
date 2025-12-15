#ifndef MAINWINDOW_H
#define MAINWINDOW_H

// Include all the Qt widgets and layout classes we’ll use
#include <QWidget>       // Base class for all visible UI components
#include <QPushButton>   // For buttons (Add / Remove)
#include <QLineEdit>     // For text input (enter task)
#include <QListWidget>   // For showing the list of tasks
#include <QVBoxLayout>   // Vertical layout manager
#include <QHBoxLayout>   // Horizontal layout manager
#include <QLabel>        // For showing simple text (like “To-Do List”)

// Declare our main class — the main window of the app
class MainWindow : public QWidget {
    Q_OBJECT  // This macro enables Qt’s "signal and slot" system

public:
    // Constructor — called when we create a MainWindow object
    // `explicit` prevents unwanted type conversions
    explicit MainWindow(QWidget *parent = nullptr);

private slots:
    // "Slots" are special functions that respond to events (like button clicks)
    void addTask();      // Called when the user clicks "Add Task"
    void removeTask();   // Called when the user clicks "Remove Task"

private:
    // Declare the widgets used in this window
    QLineEdit *taskInput;      // Input box for typing new tasks
    QListWidget *taskList;     // Widget showing list of added tasks
    QPushButton *addButton;    // Button to add a new task
    QPushButton *removeButton; // Button to remove selected task
};

#endif // MAINWINDOW_H

