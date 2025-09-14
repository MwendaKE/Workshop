#include "School.h"
#include <iostream>

// Constructor to open the database
School::School() {
    int exit = sqlite3_open("school.db", &db);  // Open the database
    if (exit) {
        std::cerr << "Error open database: " << sqlite3_errmsg(db) << std::endl;
    } else {
        createTable();  // Create table if it does not exist
    }
}

// Destructor to close the database
School::~School() {
    sqlite3_close(db);  // Close the database
}

// Create the student table
void School::createTable() {
    const char* sql = "CREATE TABLE IF NOT EXISTS STUDENTS("
                      "ADM_NUMBER INT PRIMARY KEY NOT NULL, "
                      "NAME TEXT NOT NULL, "
                      "GRADE INT NOT NULL, "
                      "FEE_PAID REAL NOT NULL, "
                      "PARENT_PHONE TEXT NOT NULL, "
                      "ADMISSION_DATE TEXT NOT NULL);";

    char* errorMessage;
    if (sqlite3_exec(db, sql, nullptr, 0, &errorMessage) != SQLITE_OK) {
        std::cerr << "Error creating table: " << errorMessage << std::endl;
        sqlite3_free(errorMessage);
    }
}

// Add a new student to the database
void School::addNewStudent(int admNumber, const std::string& name, int grade, double feePaid, const std::string& parentPhone, const std::string& admissionDate) {
    const char* sql = "INSERT INTO STUDENTS (ADM_NUMBER, NAME, GRADE, FEE_PAID, PARENT_PHONE, ADMISSION_DATE) VALUES (?, ?, ?, ?, ?, ?);";
    sqlite3_stmt* stmt;

    sqlite3_prepare_v2(db, sql, -1, &stmt, nullptr);
    sqlite3_bind_int(stmt, 1, admNumber);
    sqlite3_bind_text(stmt, 2, name.c_str(), -1, SQLITE_STATIC);
    sqlite3_bind_int(stmt, 3, grade);
    sqlite3_bind_double(stmt, 4, feePaid);
    sqlite3_bind_text(stmt, 5, parentPhone.c_str(), -1, SQLITE_STATIC);
    sqlite3_bind_text(stmt, 6, admissionDate.c_str(), -1, SQLITE_STATIC);

    if (sqlite3_step(stmt) != SQLITE_DONE) {
        std::cerr << "Error adding student: " << sqlite3_errmsg(db) << std::endl;
    } else {
        std::cout << "Student added successfully!" << std::endl;
    }
    sqlite3_finalize(stmt);  // Finalize the prepared statement
}

// Update an existing student's information
void School::updateStudent(int admNumber, const std::string& name, int grade, double feePaid, const std::string& parentPhone) {
    const char* sql = "UPDATE STUDENTS SET NAME = ?, GRADE = ?, FEE_PAID = ?, PARENT_PHONE = ? WHERE ADM_NUMBER = ?;";
    sqlite3_stmt* stmt;

    sqlite3_prepare_v2(db, sql, -1, &stmt, nullptr);
    sqlite3_bind_text(stmt, 1, name.c_str(), -1, SQLITE_STATIC);
    sqlite3_bind_int(stmt, 2, grade);
    sqlite3_bind_double(stmt, 3, feePaid);
    sqlite3_bind_text(stmt, 4, parentPhone.c_str(), -1, SQLITE_STATIC);
    sqlite3_bind_int(stmt, 5, admNumber);

    if (sqlite3_step(stmt) != SQLITE_DONE) {
        std::cerr << "Error updating student: " << sqlite3_errmsg(db) << std::endl;
    } else {
        std::cout << "Student updated successfully!" << std::endl;
    }
    sqlite3_finalize(stmt);  // Finalize the prepared statement
}

// Show all students in the database
void School::showAllStudents() {
    const char* sql = "SELECT * FROM STUDENTS;";
    sqlite3_stmt* stmt;

    sqlite3_prepare_v2(db, sql, -1, &stmt, nullptr);
    std::cout << "\nStudents List:" << std::endl;

    while (sqlite3_step(stmt) == SQLITE_ROW) {
        int admNumber = sqlite3_column_int(stmt, 0);
        std::string name = reinterpret_cast<const char*>(sqlite3_column_text(stmt, 1));
        int grade = sqlite3_column_int(stmt, 2);
        double feePaid = sqlite3_column_double(stmt, 3);
        std::string parentPhone = reinterpret_cast<const char*>(sqlite3_column_text(stmt, 4));
        std::string admissionDate = reinterpret_cast<const char*>(sqlite3_column_text(stmt, 5));

        std::cout << "Admission Number: " << admNumber << ", Name: " << name 
                  << ", Grade: " << grade << ", Fee Paid: " << feePaid 
                  << ", Parent Phone: " << parentPhone << ", Admission Date: " << admissionDate << std::endl;
    }
    sqlite3_finalize(stmt);  // Finalize the prepared statement
}