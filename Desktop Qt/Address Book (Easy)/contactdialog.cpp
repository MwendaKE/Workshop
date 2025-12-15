#include "contactdialog.h"

ContactDialog::ContactDialog(QWidget *parent) : QDialog(parent) {
    setWindowTitle("Contact");

    nameEdit = new QLineEdit(this);
    phoneEdit = new QLineEdit(this);
    emailEdit = new QLineEdit(this);
    addressEdit = new QLineEdit(this);

    QFormLayout *form = new QFormLayout;
    form->addRow("Name:", nameEdit);
    form->addRow("Phone:", phoneEdit);
    form->addRow("Email:", emailEdit);
    form->addRow("Address:", addressEdit);

    QPushButton *okButton = new QPushButton("OK");
    QPushButton *cancelButton = new QPushButton("Cancel");

    connect(okButton, &QPushButton::clicked, this, &QDialog::accept);
    connect(cancelButton, &QPushButton::clicked, this, &QDialog::reject);

    QHBoxLayout *buttonLayout = new QHBoxLayout;
    buttonLayout->addWidget(okButton);
    buttonLayout->addWidget(cancelButton);

    QVBoxLayout *mainLayout = new QVBoxLayout(this);
    mainLayout->addLayout(form);
    mainLayout->addLayout(buttonLayout);
}

Contact ContactDialog::getContact() const {
    return Contact(
        nameEdit->text(),
        phoneEdit->text(),
        emailEdit->text(),
        addressEdit->text()
    );
}

void ContactDialog::setContact(const Contact &c) {
    nameEdit->setText(c.name);
    phoneEdit->setText(c.phone);
    emailEdit->setText(c.email);
    addressEdit->setText(c.address);
}

