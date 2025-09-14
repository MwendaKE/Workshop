#include "Outpatient.h"

// Constructor to initialize Outpatient
Outpatient::Outpatient(const std::string& patientName, const std::string& sickness, double admissionFee) 
    : Patient(patientName, sickness, admissionFee) {}

// Add payment method implementation
void Outpatient::addPayment(double amount) {
    if (amount <= 0) {
        std::cout << "Payment amount must be positive." << std::endl;
        return;
    }
    totalPayment += amount;  // Increase total payment
    std::cout << "Payment of " << amount << " added for Outpatient " << patientName << std::endl;
}

// Get total payment method implementation
double Outpatient::getTotalPayment() const {
    return totalPayment;  // Return total payment
}