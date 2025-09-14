#include "Patient.h"
#include <iostream>

// Constructor to initialize patient details
Patient::Patient(const std::string& patientName, const std::string& sickness, double admissionFee)
    : patientName(patientName), sickness(sickness), admissionFee(admissionFee), totalPayment(admissionFee) {}

// Add an injection to the patient record
void Patient::addInjection(const std::string& injection) {
    injections.push_back(injection);  // Add the injection to the list
}

// Add a drug to the patient record
void Patient::addDrug(const std::string& drug) {
    drugs.push_back(drug);  // Add the drug to the list
}

// Display patient information
void Patient::showInfo() const {
    std::cout << "Patient Name: " << patientName << std::endl;
    std::cout << "Sickness: " << sickness << std::endl;
    std::cout << "Total Payment: " << totalPayment << std::endl;
    std::cout << "Injections: ";
    for (const auto& injection : injections) {
        std::cout << injection << " ";
    }
    std::cout << std::endl;
    std::cout << "Drugs: ";
    for (const auto& drug : drugs) {
        std::cout << drug << " ";
    }
    std::cout << std::endl;
}