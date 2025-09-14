#ifndef HOSPITAL_H
#define HOSPITAL_H

#include <vector>
#include <memory>
#include "Patient.h"

class Hospital {
    public:
        void addPatient(std::unique_ptr<Patient> patient);  // Add a patient
        void makePayment(const std::string& patientName, double amount);  // Make payment for a patient
        void showPatientInfo(const std::string& patientName) const;  // Display patient info
        void showAllPatients() const;  // Display all patients

    private:
        std::vector<std::unique_ptr<Patient>> patients;  // Vector to store patients
};

#endif // HOSPITAL_H