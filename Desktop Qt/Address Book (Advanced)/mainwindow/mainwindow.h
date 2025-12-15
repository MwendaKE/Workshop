#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QWidget>
#include <QTableWidget>
#include <QLineEdit>
#include <QPushButton>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include "../models/contact.h"
#include "../database/database.h"

class MainWindow : public QWidget {
    Q_OBJECT
public:
    MainWindow(QWidget *parent = nullptr);

private:
    QTableWidget *table;
    QLineEdit *searchEdit;
    QPushButton *addBtn;
    QPushButton *editBtn;
    QPushButton *deleteBtn;
    QPushButton *exportBtn;

    Database db;
    QList<Contact> contacts;

    void setupUI();
    void refreshTable();

private slots:
    void addContact();
    void editContact();
    void deleteContact();
    void searchContacts(const QString &text);
    void exportContacts();
};

#endif // MAINWINDOW_H

