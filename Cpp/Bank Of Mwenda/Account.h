// Account.h
#ifndef ACCOUNT_H  // Header guard to prevent multiple inclusions
#define ACCOUNT_H

#include <string>
#include <stdexcept>

class Account {
    public:
        Account(const std::string& accountHolder, double balance);
    
        virtual void deposit(double amount) = 0;    // Pure virtual function for deposit
        virtual void withdraw(double amount) = 0;   // Pure virtual function for withdraw
        double getBalance() const;                   // Get current balance
        std::string getAccountHolder() const;        // Get account holder's name

    protected:
        std::string accountHolder;  // Account holder's name
        double balance;             // Account balance
};

#endif // ACCOUNT_H