#ifndef DATABASE_H
#define DATABASE_H

#include <QtSql>
#include <QList>
#include "../models/contact.h"

class Database {
public:
    Database();
    ~Database();

    void addContact(const Contact &c);
    QList<Contact> getAllContacts();
    void updateContact(int id, const Contact &c);
    void deleteContact(int id);

private:
    QSqlDatabase db;
    void initializeDatabase();
    void insertInitialData();
};

#endif // DATABASE_H

