#include "mainwindow.h"
#include <QHeaderView>
#include <QMessageBox>

MainWindow::MainWindow(QWidget *parent) : QWidget(parent) {
    // 1️⃣ Setup DB
    setupDatabase();
    loadContacts();

    // 2️⃣ Create input fields
    nameInput = new QLineEdit();
    phoneInput = new QLineEdit();
    emailInput = new QLineEdit();
    addressInput = new QLineEdit();
    searchInput = new QLineEdit();

    // 3️⃣ Buttons
    addButton = new QPushButton("Add");
    editButton = new QPushButton("Edit");
    deleteButton = new QPushButton("Delete");
    searchButton = new QPushButton("Search");

    // 4️⃣ Table
    table = new QTableWidget();
    table->setColumnCount(4);
    table->setHorizontalHeaderLabels(QStringList() << "Name" << "Phone" << "Email" << "Address");
    table->horizontalHeader()->setSectionResizeMode(QHeaderView::Stretch);

    // 5️⃣ Layouts
    QVBoxLayout *mainLayout = new QVBoxLayout(this);
    QHBoxLayout *formLayout = new QHBoxLayout();
    QHBoxLayout *buttonLayout = new QHBoxLayout();

    formLayout->addWidget(new QLabel("Name:")); formLayout->addWidget(nameInput);
    formLayout->addWidget(new QLabel("Phone:")); formLayout->addWidget(phoneInput);
    formLayout->addWidget(new QLabel("Email:")); formLayout->addWidget(emailInput);
    formLayout->addWidget(new QLabel("Address:")); formLayout->addWidget(addressInput);

    buttonLayout->addWidget(addButton);
    buttonLayout->addWidget(editButton);
    buttonLayout->addWidget(deleteButton);
    buttonLayout->addWidget(new QLabel("Search:")); buttonLayout->addWidget(searchInput);
    buttonLayout->addWidget(searchButton);

    mainLayout->addLayout(formLayout);
    mainLayout->addLayout(buttonLayout);
    mainLayout->addWidget(table);

    // 6️⃣ Connect signals
    connect(addButton, &QPushButton::clicked, this, &MainWindow::addContact);
    connect(editButton, &QPushButton::clicked, this, &MainWindow::editContact);
    connect(deleteButton, &QPushButton::clicked, this, &MainWindow::deleteContact);
    connect(searchButton, &QPushButton::clicked, this, &MainWindow::searchContact);

    setWindowTitle("SQLite Address Book");
    resize(800, 400);
}

// Destructor closes DB
MainWindow::~MainWindow() {
    if (db.isOpen()) db.close();
}

// Setup SQLite database
void MainWindow::setupDatabase() {
    db = QSqlDatabase::addDatabase("QSQLITE");
    db.setDatabaseName("contacts.db");
    if (!db.open()) {
        QMessageBox::critical(this, "Error", "Cannot open database!");
    }

    QSqlQuery query;
    // Create table if it doesn't exist
    query.exec("CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, phone TEXT, email TEXT, address TEXT)");
}

// Load all contacts from DB into memory
void MainWindow::loadContacts() {
    contacts.clear();
    QSqlQuery query("SELECT name, phone, email, address FROM contacts");
    while (query.next()) {
        Contact c(query.value(0).toString(),
                  query.value(1).toString(),
                  query.value(2).toString(),
                  query.value(3).toString());
        contacts.append(c);
    }
    updateTable();
}

// Save one contact to DB
void MainWindow::saveContactToDB(const Contact &c) {
    QSqlQuery query;
    query.prepare("INSERT INTO contacts (name, phone, email, address) VALUES (?, ?, ?, ?)");
    query.addBindValue(c.name);
    query.addBindValue(c.phone);
    query.addBindValue(c.email);
    query.addBindValue(c.address);
    query.exec();
}

// Update contact in DB
void MainWindow::updateContactInDB(int row, const Contact &c) {
    QSqlQuery query;
    query.prepare("UPDATE contacts SET name=?, phone=?, email=?, address=? WHERE rowid=?");
    query.addBindValue(c.name);
    query.addBindValue(c.phone);
    query.addBindValue(c.email);
    query.addBindValue(c.address);
    query.addBindValue(row + 1); // SQLite rowid starts at 1
    query.exec();
}

// Delete contact from DB
void MainWindow::deleteContactFromDB(int row) {
    QSqlQuery query;
    query.prepare("DELETE FROM contacts WHERE rowid=?");
    query.addBindValue(row + 1);
    query.exec();
}

// Update table display
void MainWindow::updateTable() {
    table->setRowCount(contacts.size());
    for (int i = 0; i < contacts.size(); ++i) {
        table->setItem(i, 0, new QTableWidgetItem(contacts[i].name));
        table->setItem(i, 1, new QTableWidgetItem(contacts[i].phone));
        table->setItem(i, 2, new QTableWidgetItem(contacts[i].email));
        table->setItem(i, 3, new QTableWidgetItem(contacts[i].address));
    }
}

// Add new contact
void MainWindow::addContact() {
    Contact c(nameInput->text(), phoneInput->text(), emailInput->text(), addressInput->text());
    contacts.append(c);
    saveContactToDB(c); // save in SQLite
    updateTable();
}

// Edit selected contact
void MainWindow::editContact() {
    auto items = table->selectedItems();
    if (items.isEmpty()) return;
    int row = items[0]->row();
    contacts[row].name = nameInput->text();
    contacts[row].phone = phoneInput->text();
    contacts[row].email = emailInput->text();
    contacts[row].address = addressInput->text();
    updateContactInDB(row, contacts[row]); // update DB
    updateTable();
}

// Delete selected contact
void MainWindow::deleteContact() {
    auto items = table->selectedItems();
    if (items.isEmpty()) return;
    int row = items[0]->row();
    deleteContactFromDB(row); // remove from DB
    contacts.removeAt(row);    // remove from memory
    updateTable();
}

// Search contacts by name or phone
void MainWindow::searchContact() {
    QString queryText = searchInput->text().toLower();
    for (int i = 0; i < table->rowCount(); ++i) {
        bool match = contacts[i].name.toLower().contains(queryText) ||
                     contacts[i].phone.contains(queryText);
        table->setRowHidden(i, !match);
    }
}

