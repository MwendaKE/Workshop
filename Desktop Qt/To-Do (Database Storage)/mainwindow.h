#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QWidget>
#include <QPushButton>
#include <QLineEdit>
#include <QListWidget>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QLabel>

#include <QtSql>  // For database classes: QSqlDatabase, QSqlQuery

class MainWindow : public QWidget {
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void addTask();      // Add task to DB
    void removeTask();   // Remove selected task from DB

private:
    QLineEdit *taskInput;
    QListWidget *taskList;
    QPushButton *addButton;
    QPushButton *removeButton;

    QSqlDatabase db;  // Database connection

    void setupDatabase();    // Initialize DB and table
    void loadTasksFromDB();  // Load all tasks from DB into the list
};

#endif // MAINWINDOW_H

