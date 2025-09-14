// Account.cxx
#include "Account.h"

// Constructor to initialize account holder and balance
Account::Account(const std::string& accountHolder, double balance) 
    : accountHolder(accountHolder), balance(balance) {}

// Get the current balance
double Account::getBalance() const {
    return balance;
}

// Get the account holder's name
std::string Account::getAccountHolder() const {
    return accountHolder;
}