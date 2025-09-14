// CurrentAccount.cxx
#include "CurrentAccount.h"
#include <iostream>

// Constructor to initialize CurrentAccount
CurrentAccount::CurrentAccount(const std::string& accountHolder, double balance) 
    : Account(accountHolder, balance) {}

// Deposit method implementation
void CurrentAccount::deposit(double amount) {
    if (amount <= 0) {
        throw std::invalid_argument("Deposit amount must be positive.");
    }
    balance += amount;  // Increase balance by the deposit amount
    std::cout << "Deposited: " << amount << " to Current Account of " << accountHolder << std::endl;
}

// Withdraw method implementation
void CurrentAccount::withdraw(double amount) {
    if (amount <= 0) {
        throw std::invalid_argument("Withdrawal amount must be positive.");
    }
    if (amount > balance) {
        throw std::runtime_error("Insufficient funds for withdrawal.");
    }
    balance -= amount;  // Decrease balance by the withdrawal amount
    std::cout << "Withdrew: " << amount << " from Current Account of " << accountHolder << std::endl;
}