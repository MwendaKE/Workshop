#include "contactdialog.h"
#include <QVBoxLayout>
#include <QDialogButtonBox>

ContactDialog::ContactDialog(QWidget *parent) : QDialog(parent) {
    QFormLayout *form = new QFormLayout;

    nameEdit = new QLineEdit;
    phoneEdit = new QLineEdit;
    emailEdit = new QLineEdit;
    addressEdit = new QLineEdit;

    form->addRow("Name:", nameEdit);
    form->addRow("Phone:", phoneEdit);
    form->addRow("Email:", emailEdit);
    form->addRow("Address:", addressEdit);

    QDialogButtonBox *buttons = new QDialogButtonBox(QDialogButtonBox::Ok | QDialogButtonBox::Cancel);
    connect(buttons, &QDialogButtonBox::accepted, this, &QDialog::accept);
    connect(buttons, &QDialogButtonBox::rejected, this, &QDialog::reject);

    QVBoxLayout *layout = new QVBoxLayout;
    layout->addLayout(form);
    layout->addWidget(buttons);
    setLayout(layout);
}

Contact ContactDialog::getContact() const {
    Contact c;
    c.name = nameEdit->text();
    c.phone = phoneEdit->text();
    c.email = emailEdit->text();
    c.address = addressEdit->text();
    return c;
}

void ContactDialog::setContact(const Contact &c) {
    nameEdit->setText(c.name);
    phoneEdit->setText(c.phone);
    emailEdit->setText(c.email);
    addressEdit->setText(c.address);
}

