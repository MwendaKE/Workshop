#ifndef INPATIENT_H
#define INPATIENT_H

#include "Patient.h"

class Inpatient : public Patient {
    public:
        Inpatient(const std::string& patientName, const std::string& sickness, double admissionFee);
        void addPayment(double amount) override;    // Add payment implementation
        double getTotalPayment() const override;    // Get total payment implementation
};

#endif // INPATIENT_H