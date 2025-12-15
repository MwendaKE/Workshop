#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QWidget>
#include <QTableWidget>
#include <QPushButton>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QSqlDatabase>
#include <QSqlQuery>
#include <QMessageBox>
#include "contact.h"          // Add this at the top
#include "contactdialog.h"


// Main window class
class MainWindow : public QWidget {
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = nullptr); // Constructor

private slots:
    void addContact();     // Slot to add contact
    void editContact();    // Slot to edit contact
    void deleteContact();  // Slot to delete contact

private:
    // UI elements
    QTableWidget *table;
    QPushButton *addButton;
    QPushButton *editButton;
    QPushButton *deleteButton;

    // Database
    QSqlDatabase db;

    // Methods
    void setupUI();               // Setup GUI
    void setupDatabase();         // Setup SQLite database
    void updateTable();           // Load data from DB into table
    void saveContactToDB(const Contact &c);
    void updateContactInDB(int row, const Contact &c);
    void deleteContactFromDB(int row);
};

#endif // MAINWINDOW_H

