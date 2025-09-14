// Bank.cxx
#include "Bank.h"
#include <iostream>
#include <algorithm>

// Method to add an account
void Bank::addAccount(std::unique_ptr<Account> account) {
    accounts.push_back(std::move(account));  // Add account to the vector
}

// Method to deposit money to an account
void Bank::deposit(const std::string& accountHolder, double amount) {
    for (const auto& account : accounts) {
        if (account->getAccountHolder() == accountHolder) {
            account->deposit(amount);  // Call the deposit method
            return;
        }
    }
    std::cout << "Account not found: " << accountHolder << std::endl;
}

// Method to withdraw money from an account
void Bank::withdraw(const std::string& accountHolder, double amount) {
    for (const auto& account : accounts) {
        if (account->getAccountHolder() == accountHolder) {
            try {
                account->withdraw(amount);  // Call the withdraw method
            } catch (const std::runtime_error& e) {
                std::cout << "Error: " << e.what() << std::endl;  // Catch runtime errors
            }
            return;
        }
    }
    std::cout << "Account not found: " << accountHolder << std::endl;
}

// Method to display all account balances
void Bank::displayBalances() const {
    std::cout << "\nAccount Balances:" << std::endl;
    for (const auto& account : accounts) {
        std::cout << "Account Holder: " << account->getAccountHolder() 
                  << ", Balance: " << account->getBalance() << std::endl;
    }
}