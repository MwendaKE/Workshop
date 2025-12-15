#include "mainwindow.h"
#include "../dialogs/contactdialog.h"
#include <QHeaderView>
#include <QMessageBox>
#include <QFile>
#include <QTextStream>
#include <QIcon>

MainWindow::MainWindow(QWidget *parent) : QWidget(parent) {
    setupUI();
    refreshTable();
}

void MainWindow::setupUI() {
    table = new QTableWidget;
    table->setColumnCount(4);
    table->setHorizontalHeaderLabels({"Name", "Phone", "Email", "Address"});
    table->horizontalHeader()->setStretchLastSection(true);
    table->setSelectionBehavior(QAbstractItemView::SelectRows);
    table->setAlternatingRowColors(true); // Zebra rows
    table->setStyleSheet(
        "QTableWidget { background-color: #fefefe; font-family: 'Segoe UI', Arial; font-size: 14px; gridline-color: #d3d3d3; }"
        "QHeaderView::section { background-color: #007ACC; color: white; padding: 4px; font-weight: bold; }"
        "QTableWidget::item { padding: 5px; }"
        "QTableWidget::item:selected { background-color: #FFD966; color: black; }"
        "QTableWidget::item:hover { background-color: #FFF2CC; }"
    );

    searchEdit = new QLineEdit;
    searchEdit->setPlaceholderText("Search...");

    addBtn = new QPushButton("Add");
    editBtn = new QPushButton("Edit");
    deleteBtn = new QPushButton("Delete");
    exportBtn = new QPushButton("Export CSV");
    
    addBtn->setIcon(QIcon("resources/add.png"));
    editBtn->setIcon(QIcon("resources/edit.png"));
    deleteBtn->setIcon(QIcon("resources/delete.png"));
    exportBtn->setIcon(QIcon("resources/export.png"));

    addBtn->setIconSize(QSize(24,24));
    editBtn->setIconSize(QSize(24,24));
    deleteBtn->setIconSize(QSize(24,24));
    exportBtn->setIconSize(QSize(24,24));

    QString btnStyle = 
        "QPushButton { background-color: #007ACC; color: white; border-radius: 5px; padding: 6px 12px; font-weight: bold; }"
        "QPushButton:hover { background-color: #005F99; }";
    addBtn->setStyleSheet(btnStyle);
    editBtn->setStyleSheet(btnStyle);
    deleteBtn->setStyleSheet(btnStyle);
    exportBtn->setStyleSheet(btnStyle);

    QHBoxLayout *btnLayout = new QHBoxLayout;
    btnLayout->addWidget(addBtn);
    btnLayout->addWidget(editBtn);
    btnLayout->addWidget(deleteBtn);
    btnLayout->addWidget(exportBtn);

    QVBoxLayout *mainLayout = new QVBoxLayout;
    mainLayout->addWidget(searchEdit);
    mainLayout->addWidget(table);
    mainLayout->addLayout(btnLayout);

    setLayout(mainLayout);
    setWindowTitle("Address Book");

    connect(addBtn, &QPushButton::clicked, this, &MainWindow::addContact);
    connect(editBtn, &QPushButton::clicked, this, &MainWindow::editContact);
    connect(deleteBtn, &QPushButton::clicked, this, &MainWindow::deleteContact);
    connect(searchEdit, &QLineEdit::textChanged, this, &MainWindow::searchContacts);
    connect(exportBtn, &QPushButton::clicked, this, &MainWindow::exportContacts);
}

void MainWindow::refreshTable() {
    contacts = db.getAllContacts(); // get fresh data
    table->setRowCount(contacts.size());

    for (int i = 0; i < contacts.size(); ++i) {
        const Contact &c = contacts[i];
        table->setItem(i, 0, new QTableWidgetItem(c.name));
        table->setItem(i, 1, new QTableWidgetItem(c.phone));
        table->setItem(i, 2, new QTableWidgetItem(c.email));
        table->setItem(i, 3, new QTableWidgetItem(c.address));
    }
}

void MainWindow::addContact() {
    ContactDialog dialog(this);
    if (dialog.exec() == QDialog::Accepted) {
        Contact c = dialog.getContact();
        db.addContact(c);
        refreshTable();
    }
}

void MainWindow::editContact() {
    int row = table->currentRow();
    if (row < 0 || row >= contacts.size()) return; // safety check

    ContactDialog dialog(this);
    dialog.setContact(contacts[row]);
    if (dialog.exec() == QDialog::Accepted) {
        Contact c = dialog.getContact();
        db.updateContact(contacts[row].id, c); // use actual ID
        refreshTable();
    }
}

void MainWindow::deleteContact() {
    int row = table->currentRow();
    if (row < 0 || row >= contacts.size()) return; // safety check

    int ret = QMessageBox::question(this, "Confirm Delete", 
                                    "Are you sure you want to delete this contact?");
    if (ret == QMessageBox::Yes) {
        db.deleteContact(contacts[row].id); // use actual ID
        refreshTable();
    }
}

void MainWindow::searchContacts(const QString &text) {
    for (int i = 0; i < table->rowCount(); ++i) {
        bool visible = table->item(i,0)->text().contains(text, Qt::CaseInsensitive)
                    || table->item(i,1)->text().contains(text, Qt::CaseInsensitive)
                    || table->item(i,2)->text().contains(text, Qt::CaseInsensitive)
                    || table->item(i,3)->text().contains(text, Qt::CaseInsensitive);
        table->setRowHidden(i, !visible);
    }
}

void MainWindow::exportContacts() {
    QFile file("contacts.csv");
    if (file.open(QIODevice::WriteOnly | QIODevice::Text)) {
        QTextStream out(&file);
        for (const Contact &c : contacts) {
            out << c.name << "," << c.phone << "," << c.email << "," << c.address << "\n";
        }
        file.close();
        QMessageBox::information(this, "Exported", "Contacts exported successfully!");
    }
}

