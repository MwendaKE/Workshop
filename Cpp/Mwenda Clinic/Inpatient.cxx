#include "Inpatient.h"

// Constructor to initialize Inpatient
Inpatient::Inpatient(const std::string& patientName, const std::string& sickness, double admissionFee) 
    : Patient(patientName, sickness, admissionFee) {}

// Add payment method implementation
void Inpatient::addPayment(double amount) {
    if (amount <= 0) {
        std::cout << "Payment amount must be positive." << std::endl;
        return;
    }
    totalPayment += amount;  // Increase total payment
    std::cout << "Payment of " << amount << " added for Inpatient " << patientName << std::endl;
}

// Get total payment method implementation
double Inpatient::getTotalPayment() const {
    return totalPayment;  // Return total payment
}