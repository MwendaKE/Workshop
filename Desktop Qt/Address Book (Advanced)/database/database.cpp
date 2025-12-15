#include "database.h"
#include <QDebug>

Database::Database() {
    // Open or create database
    db = QSqlDatabase::addDatabase("QSQLITE");
    db.setDatabaseName("addressbook.db");

    if (!db.open()) {
        qDebug() << "Failed to open database!";
        return;
    }

    initializeDatabase();
}

Database::~Database() {
    if (db.isOpen()) {
        db.close();
    }
}

void Database::initializeDatabase() {
    QSqlQuery query;

    // Create table if it doesn't exist
    query.exec("CREATE TABLE IF NOT EXISTS contacts ("
               "id INTEGER PRIMARY KEY AUTOINCREMENT, "
               "name TEXT NOT NULL, "
               "phone TEXT NOT NULL, "
               "email TEXT, "
               "address TEXT)");

    // Insert initial data if table is empty
    query.exec("SELECT COUNT(*) FROM contacts");
    if (query.next() && query.value(0).toInt() == 0) {
        insertInitialData();
    }
}

void Database::insertInitialData() {
    QSqlQuery query;
    QStringList names = {
        "John Doe","Jane Smith","Michael Johnson","Emily Davis","William Brown",
        "Olivia Wilson","James Taylor","Sophia Anderson","Benjamin Thomas","Mia Martinez",
        "Alexander Lee","Charlotte White","Daniel Harris","Amelia Clark","Matthew Lewis",
        "Harper Robinson","Joseph Walker","Evelyn Hall","David Allen","Abigail Young",
        "Christopher King","Elizabeth Wright","Anthony Scott","Sofia Green","Joshua Baker",
        "Ella Adams","Andrew Nelson","Victoria Carter","Ryan Mitchell","Grace Perez",
        "Nathan Roberts","Chloe Turner","Samuel Phillips","Lily Campbell","Ethan Parker",
        "Hannah Evans","Alexander Edwards","Avery Collins","Caleb Stewart","Scarlett Morris",
        "Joshua Rogers","Zoe Reed","Logan Cook","Victoria Morgan","Jackson Bell",
        "Mia Murphy","Liam Bailey","Ella Rivera","Benjamin Cooper"
    };

    QStringList phones;
    for (int i = 0; i < 50; i++) {
        phones << QString("07%1%2%3%4%5%6%7%8").arg(rand()%10).arg(rand()%10)
                  .arg(rand()%10).arg(rand()%10).arg(rand()%10).arg(rand()%10)
                  .arg(rand()%10).arg(rand()%10);
    }

    for (int i = 0; i < 50; i++) {
        query.prepare("INSERT INTO contacts (name, phone, email, address) "
                      "VALUES (?, ?, ?, ?)");
        query.addBindValue(names[i]);
        query.addBindValue(phones[i]);
        query.addBindValue(names[i].toLower().replace(" ", "") + "@example.com");
        query.addBindValue(QString("%1 Street, City %2").arg(i+1).arg(i+1));
        if (!query.exec()) {
            qDebug() << "Failed to insert initial data:" << query.lastError();
        }
    }
}

void Database::addContact(const Contact &c) {
    QSqlQuery query;
    query.prepare("INSERT INTO contacts (name, phone, email, address) VALUES (?, ?, ?, ?)");
    query.addBindValue(c.name);
    query.addBindValue(c.phone);
    query.addBindValue(c.email);
    query.addBindValue(c.address);
    query.exec();
}

QList<Contact> Database::getAllContacts() {
    QList<Contact> list;
    QSqlQuery query("SELECT * FROM contacts ORDER BY name");
    while (query.next()) {
        Contact c;
        c.id = query.value("id").toInt();
        c.name = query.value("name").toString();
        c.phone = query.value("phone").toString();
        c.email = query.value("email").toString();
        c.address = query.value("address").toString();
        list.append(c);
    }
    return list;
}

void Database::updateContact(int id, const Contact &c) {
    QSqlQuery query;
    query.prepare("UPDATE contacts SET name=?, phone=?, email=?, address=? WHERE id=?");
    query.addBindValue(c.name);
    query.addBindValue(c.phone);
    query.addBindValue(c.email);
    query.addBindValue(c.address);
    query.addBindValue(id);
    query.exec();
}

void Database::deleteContact(int id) {
    QSqlQuery query;
    query.prepare("DELETE FROM contacts WHERE id=?");
    query.addBindValue(id);
    query.exec();
}

