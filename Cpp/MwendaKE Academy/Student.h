#ifndef STUDENT_H
#define STUDENT_H

#include <string>

class Student {
    public:
        Student(int admNumber, const std::string& name, int grade, double feePaid, const std::string& parentPhone, const std::string& admissionDate);

        int getAdmNumber() const;              // Get admission number
        std::string getName() const;           // Get student name
        int getGrade() const;                   // Get student grade
        double getFeePaid() const;              // Get fee paid
        std::string getParentPhone() const;    // Get parent's phone number
        std::string getAdmissionDate() const;  // Get admission date

    private:
        int admNumber;                         // Admission number
        std::string name;                      // Student's name
        int grade;                             // Student's grade
        double feePaid;                        // Fee paid by the student
        std::string parentPhone;               // Parent's phone number
        std::string admissionDate;             // Admission date
};

#endif // STUDENT_H