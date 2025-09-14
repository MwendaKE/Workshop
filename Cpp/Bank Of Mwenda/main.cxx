// main.cxx
#include <iostream>
#include <memory>
#include "Bank.h"
#include "SavingsAccount.h"
#include "CurrentAccount.h"

using namespace std;

int main() {
    Bank bank;  // Create a Bank object

    // Create some accounts
    bank.addAccount(make_unique<SavingsAccount>("Mwenda", 10000));
    bank.addAccount(make_unique<CurrentAccount>("Erick", 3000));

    // Deposit money into accounts
    bank.deposit("Mwenda", 10200);  // Valid deposit
    bank.deposit("Erick", 50000);    // Valid deposit

    // Withdraw money from accounts
    bank.withdraw("Mwenda", 5000); // Valid withdrawal
    bank.withdraw("Erick", 3000000);   // Invalid withdrawal (insufficient funds)

    // Display all account balances
    bank.displayBalances();

    // Attempt to withdraw from a non-existing account
    bank.withdraw("Njagi", 50000); // Invalid account

    return 0;
}

// Compile:
// g++ -o banking_system main.cpp Account.cpp SavingsAccount.cpp CurrentAccount.cpp Bank.cpp

// Run:
// ./banking_system