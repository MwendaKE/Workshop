#include "Hospital.h"
#include <iostream>

// Method to add a patient
void Hospital::addPatient(std::unique_ptr<Patient> patient) {
    patients.push_back(std::move(patient));  // Add patient to the vector
}

// Method to make a payment for a patient
void Hospital::makePayment(const std::string& patientName, double amount) {
    for (const auto& patient : patients) {
        if (patient->getName() == patientName) {
            patient->addPayment(amount);  // Call the addPayment method
            return;
        }
    }
    std::cout << "Patient not found: " << patientName << std::endl;
}

// Method to display patient info
void Hospital::showPatientInfo(const std::string& patientName) const {
    for (const auto& patient : patients) {
        if (patient->getName() == patientName) {
            patient->showInfo();  // Call the showInfo method
            return;
        }
    }
    std::cout << "Patient not found: " << patientName << std::endl;
}

// Method to display all patients
void Hospital::showAllPatients() const {
    std::cout << "\nPatient List:" << std::endl;
    for (const auto& patient : patients) {
        patient->showInfo();  // Call the showInfo method for each patient
    }
}