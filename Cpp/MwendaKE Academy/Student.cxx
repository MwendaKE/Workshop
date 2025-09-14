#include "Student.h"

// Constructor to initialize student details
Student::Student(int admNumber, const std::string& name, int grade, double feePaid, const std::string& parentPhone, const std::string& admissionDate)
    : admNumber(admNumber), name(name), grade(grade), feePaid(feePaid), parentPhone(parentPhone), admissionDate(admissionDate) {}

// Get admission number
int Student::getAdmNumber() const {
    return admNumber;
}

// Get student name
std::string Student::getName() const {
    return name;
}

// Get student grade
int Student::getGrade() const {
    return grade;
}

// Get fee paid
double Student::getFeePaid() const {
    return feePaid;
}

// Get parent's phone number
std::string Student::getParentPhone() const {
    return parentPhone;
}

// Get admission date
std::string Student::getAdmissionDate() const {
    return admissionDate;
}