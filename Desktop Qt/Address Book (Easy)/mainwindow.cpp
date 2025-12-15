#include <QHeaderView> 
#include "mainwindow.h"

MainWindow::MainWindow(QWidget *parent) : QWidget(parent) {
    setupUI();       // Setup GUI layout
    setupDatabase(); // Setup SQLite database
    updateTable();   // Load contacts from DB into table
}

// Setup UI elements
void MainWindow::setupUI() {
    table = new QTableWidget(this);
    table->setColumnCount(4);
    table->setHorizontalHeaderLabels({"Name", "Phone", "Email", "Address"});
    table->horizontalHeader()->setStretchLastSection(true);

    addButton = new QPushButton("Add");
    editButton = new QPushButton("Edit");
    deleteButton = new QPushButton("Delete");

    connect(addButton, &QPushButton::clicked, this, &MainWindow::addContact);
    connect(editButton, &QPushButton::clicked, this, &MainWindow::editContact);
    connect(deleteButton, &QPushButton::clicked, this, &MainWindow::deleteContact);

    QVBoxLayout *mainLayout = new QVBoxLayout(this);
    mainLayout->addWidget(table);

    QHBoxLayout *buttonLayout = new QHBoxLayout();
    buttonLayout->addWidget(addButton);
    buttonLayout->addWidget(editButton);
    buttonLayout->addWidget(deleteButton);

    mainLayout->addLayout(buttonLayout);
}

// Setup SQLite database
void MainWindow::setupDatabase() {
    db = QSqlDatabase::addDatabase("QSQLITE");
    db.setDatabaseName("contacts.db");
    if (!db.open()) {
        QMessageBox::critical(this, "Error", "Cannot open database");
    }

    QSqlQuery query;
    query.exec("CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT, address TEXT)");
}

// Load contacts from database
void MainWindow::updateTable() {
    table->setRowCount(0);

    QSqlQuery query("SELECT * FROM contacts");
    while (query.next()) {
        int row = table->rowCount();
        table->insertRow(row);
        table->setItem(row, 0, new QTableWidgetItem(query.value("name").toString()));
        table->setItem(row, 1, new QTableWidgetItem(query.value("phone").toString()));
        table->setItem(row, 2, new QTableWidgetItem(query.value("email").toString()));
        table->setItem(row, 3, new QTableWidgetItem(query.value("address").toString()));
    }
}

// Database actions
void MainWindow::saveContactToDB(const Contact &c) {
    QSqlQuery query;
    query.prepare("INSERT INTO contacts (name, phone, email, address) VALUES (?, ?, ?, ?)");
    query.addBindValue(c.name);
    query.addBindValue(c.phone);
    query.addBindValue(c.email);
    query.addBindValue(c.address);
    query.exec();
}

void MainWindow::updateContactInDB(int row, const Contact &c) {
    QSqlQuery query;
    query.exec(QString("SELECT id FROM contacts LIMIT 1 OFFSET %1").arg(row));
    if (query.next()) {
        int id = query.value("id").toInt();
        query.prepare("UPDATE contacts SET name=?, phone=?, email=?, address=? WHERE id=?");
        query.addBindValue(c.name);
        query.addBindValue(c.phone);
        query.addBindValue(c.email);
        query.addBindValue(c.address);
        query.addBindValue(id);
        query.exec();
    }
}

void MainWindow::deleteContactFromDB(int row) {
    QSqlQuery query;
    query.exec(QString("SELECT id FROM contacts LIMIT 1 OFFSET %1").arg(row));
    if (query.next()) {
        int id = query.value("id").toInt();
        query.prepare("DELETE FROM contacts WHERE id=?");
        query.addBindValue(id);
        query.exec();
    }
}

// Slots
void MainWindow::addContact() {
    ContactDialog dialog(this);
    if (dialog.exec() == QDialog::Accepted) {
        Contact c = dialog.getContact();
        saveContactToDB(c);
        updateTable();
    }
}

void MainWindow::editContact() {
    auto items = table->selectedItems();
    if (items.isEmpty()) return;
    int row = items[0]->row();

    ContactDialog dialog(this);
    dialog.setContact(Contact(
        table->item(row,0)->text(),
        table->item(row,1)->text(),
        table->item(row,2)->text(),
        table->item(row,3)->text()
    ));

    if (dialog.exec() == QDialog::Accepted) {
        Contact c = dialog.getContact();
        updateContactInDB(row, c);
        updateTable();
    }
}

void MainWindow::deleteContact() {
    auto items = table->selectedItems();
    if (items.isEmpty()) return;
    int row = items[0]->row();
    deleteContactFromDB(row);
    updateTable();
}

