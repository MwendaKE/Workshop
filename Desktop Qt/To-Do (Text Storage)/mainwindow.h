#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QWidget>
#include <QPushButton>
#include <QLineEdit>
#include <QListWidget>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QLabel>
#include <QString>
#include <QFile>      // To work with files
#include <QTextStream> // To read/write text

class MainWindow : public QWidget {
    Q_OBJECT // Required for signals and slots

public:
    explicit MainWindow(QWidget *parent = nullptr); // Constructor

private slots:
    void addTask();      // Add a task to the list
    void removeTask();   // Remove the selected task

private:
    QLineEdit *taskInput;      // Input for new tasks
    QListWidget *taskList;     // List to display tasks
    QPushButton *addButton;    // Add button
    QPushButton *removeButton; // Remove button

    void loadTasks();   // Load tasks from file at startup
    void saveTasks();   // Save tasks to file whenever modified
};

#endif // MAINWINDOW_H

