#ifndef OUTPATIENT_H
#define OUTPATIENT_H

#include "Patient.h"

class Outpatient : public Patient {
    public:
        Outpatient(const std::string& patientName, const std::string& sickness, double admissionFee);
        void addPayment(double amount) override;    // Add payment implementation
        double getTotalPayment() const override;    // Get total payment implementation
};

#endif // OUTPATIENT_H