#ifndef CONTACT_H
#define CONTACT_H

#include <QString>

struct Contact {
    int id;          // Unique ID for the contact (auto-increment in DB)
    QString name;
    QString phone;
    QString email;
    QString address;
};

#endif // CONTACT_H

