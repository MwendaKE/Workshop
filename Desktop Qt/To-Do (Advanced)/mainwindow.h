#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QWidget>
#include <QPushButton>
#include <QLineEdit>
#include <QListWidget>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QLabel>
#include <QDateEdit>
#include <QtSql>  // For SQLite

// Main window class
class MainWindow : public QWidget {
    Q_OBJECT  // Enables signals & slots

public:
    explicit MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void addTask();      // Add task to DB
    void removeTask();   // Remove selected task from DB
    void removeAllTasks(); // Delete all tasks from DB
    void toggleTaskDone(QListWidgetItem *item); // Mark done/undone

private:
    QLineEdit *taskInput;      // Input box
    QDateEdit *dueDateInput;   // Input due date
    QListWidget *taskList;     // Shows tasks
    QPushButton *addButton;
    QPushButton *removeButton;
    QPushButton *deleteAllButton;

    QSqlDatabase db;           // SQLite database

    void setupDatabase();       // Initialize DB
    void loadTasksFromDB();     // Load all tasks
};

#endif // MAINWINDOW_H

