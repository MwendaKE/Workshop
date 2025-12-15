#ifndef CONTACT_H
#define CONTACT_H

#include <QString>

struct Contact {
    QString name;
    QString phone;
    QString email;
    QString address;

    Contact(QString n="", QString p="", QString e="", QString a="")
        : name(n), phone(p), email(e), address(a) {}
};

#endif // CONTACT_H

