// CurrentAccount.h
#ifndef CURRENTACCOUNT_H
#define CURRENTACCOUNT_H

#include "Account.h"

class CurrentAccount : public Account {
public:
    CurrentAccount(const std::string& accountHolder, double balance);
    void deposit(double amount) override;   // Deposit implementation
    void withdraw(double amount) override;  // Withdraw implementation
};

#endif // CURRENTACCOUNT_H