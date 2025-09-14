// Bank.h
#ifndef BANK_H
#define BANK_H

#include <vector>
#include <memory>
#include "Account.h"

class Bank {
public:
    void addAccount(std::unique_ptr<Account> account);  // Add an account
    void deposit(const std::string& accountHolder, double amount);  // Deposit to an account
    void withdraw(const std::string& accountHolder, double amount); // Withdraw from an account
    void displayBalances() const;  // Display all account balances

private:
    std::vector<std::unique_ptr<Account>> accounts;  // Vector to store accounts
};

#endif // BANK_H
}