#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QWidget>
#include <QTableWidget>
#include <QPushButton>
#include <QLineEdit>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QLabel>
#include <QtSql>         // ✅ For database
#include "contact.h"

class MainWindow : public QWidget {
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = nullptr);
    ~MainWindow();  // Destructor closes DB

private slots:
    void addContact();
    void editContact();
    void deleteContact();
    void searchContact();

private:
    QLineEdit *nameInput;
    QLineEdit *phoneInput;
    QLineEdit *emailInput;
    QLineEdit *addressInput;
    QLineEdit *searchInput;

    QPushButton *addButton;
    QPushButton *editButton;
    QPushButton *deleteButton;
    QPushButton *searchButton;

    QTableWidget *table;

    QList<Contact> contacts;

    // ✅ Database object
    QSqlDatabase db;

    void setupDatabase();  // Initialize SQLite
    void loadContacts();   // Load contacts from DB
    void updateTable();    // Refresh table
    void saveContactToDB(const Contact &c); // Save one contact
    void updateContactInDB(int row, const Contact &c); // Update contact
    void deleteContactFromDB(int row);  // Delete contact from DB
};

#endif // MAINWINDOW_H

