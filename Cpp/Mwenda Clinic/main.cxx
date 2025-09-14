#include <iostream>
#include <memory>
#include "Hospital.h"
#include "Inpatient.h"
#include "Outpatient.h"

using namespace std;

int main() {
    Hospital hospital;  // Create a Hospital object

    // Create some patients
    hospital.addPatient(make_unique<Inpatient>("Peter Kamau Mwangi", "Fever", 500));
    hospital.addPatient(make_unique<Outpatient>("Hannah Katinge Wanzanze", "Headache", 450));

    // Display all patients
    hospital.showAllPatients();

    // Make payments
    hospital.makePayment("Peter Kamau Mwangi", 100);
    hospital.makePayment("Hannah Katinge Wanzanze", 250);

    // Show updated patient info
    hospital.showPatientInfo("Peter Kamau Mwangi");
    hospital.showPatientInfo("Hannah Katinge Wanzanze");

    // Try to make payment for a non-existing patient
    hospital.makePayment("Timothy Mutugi Ngai", 1000);

    return 0;  // Indicate successful completion
}