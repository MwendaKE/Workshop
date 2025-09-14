#ifndef SCHOOL_H
#define SCHOOL_H

#include <vector>
#include <sqlite3.h>
#include "Student.h"

class School {
    public:
        School();                            // Constructor
        ~School();                           // Destructor
        void addNewStudent(int admNumber, const std::string& name, int grade, double feePaid, const std::string& parentPhone, const std::string& admissionDate); // Add new student
        void updateStudent(int admNumber, const std::string& name, int grade, double feePaid, const std::string& parentPhone); // Update student
        void showAllStudents();              // Display all students

    private:
        sqlite3* db;                        // Pointer to the SQLite database
        void createTable();                 // Create the student table
};

#endif // SCHOOL_H