#ifndef CONTACTDIALOG_H
#define CONTACTDIALOG_H

#include <QDialog>
#include <QLineEdit>
#include <QFormLayout>
#include <QPushButton>
#include "mainwindow.h" // For Contact struct
#include "contact.h"          // Add this at the top


class ContactDialog : public QDialog {
    Q_OBJECT

public:
    explicit ContactDialog(QWidget *parent = nullptr);
    Contact getContact() const;        // Return contact info
    void setContact(const Contact &c); // Pre-fill fields for editing

private:
    QLineEdit *nameEdit;
    QLineEdit *phoneEdit;
    QLineEdit *emailEdit;
    QLineEdit *addressEdit;
};

#endif // CONTACTDIALOG_H

