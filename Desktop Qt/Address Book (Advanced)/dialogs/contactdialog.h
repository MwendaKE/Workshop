#ifndef CONTACTDIALOG_H
#define CONTACTDIALOG_H

#include <QDialog>
#include <QLineEdit>
#include <QFormLayout>
#include <QPushButton>
#include "../models/contact.h"

class ContactDialog : public QDialog {
    Q_OBJECT
public:
    ContactDialog(QWidget *parent = nullptr);

    Contact getContact() const;
    void setContact(const Contact &c);

private:
    QLineEdit *nameEdit;
    QLineEdit *phoneEdit;
    QLineEdit *emailEdit;
    QLineEdit *addressEdit;
};

#endif // CONTACTDIALOG_H

