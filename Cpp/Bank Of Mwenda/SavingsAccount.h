// SavingsAccount.h
#ifndef SAVINGSACCOUNT_H
#define SAVINGSACCOUNT_H

#include "Account.h"

class SavingsAccount : public Account {
    public:
        SavingsAccount(const std::string& accountHolder, double balance);
        void deposit(double amount) override;   // Deposit implementation
        void withdraw(double amount) override;  // Withdraw implementation
};

#endif // SAVINGSACCOUNT_H