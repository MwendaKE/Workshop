#ifndef CONTACT_H
#define CONTACT_H

#include <QString>

// 📘 Simple Contact class to hold information about each person
class Contact {
public:
    QString name;    // Contact's name
    QString phone;   // Contact's phone number
    QString email;   // Contact's email
    QString address; // Contact's physical address

    // Constructor to easily create a contact
    Contact(QString n = "", QString p = "", QString e = "", QString a = "") 
        : name(n), phone(p), email(e), address(a) {}
};

#endif // CONTACT_H

