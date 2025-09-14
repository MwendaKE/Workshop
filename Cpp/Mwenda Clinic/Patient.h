#ifndef PATIENT_H
#define PATIENT_H

#include <string>
#include <vector>

class Patient {
    public:
        Patient(const std::string& patientName, const std::string& sickness, double admissionFee);
    
        virtual void addPayment(double amount) = 0;    // Pure virtual function for adding payment
        virtual double getTotalPayment() const = 0;    // Pure virtual function for getting total payment
        virtual void showInfo() const;                  // Display patient info
        void addInjection(const std::string& injection);  // Add injection details
        void addDrug(const std::string& drug);            // Add drug details

    protected:
        std::string patientName;  // Patient's name
        std::string sickness;     // Patient's sickness
        double admissionFee;      // Admission fee
        std::vector<std::string> injections;  // List of injections administered
        std::vector<std::string> drugs;        // List of drugs administered
        double totalPayment;      // Total payment made by the patient
};

#endif // PATIENT_H