#include <iostream>
#include "School.h"

using namespace std;

int main() {
    School school;  // Create a School object

    // Add new students
    school.addNewStudent(101, "Carison Mutuma", 1, 11000, "838-373-122", "2020-01-03");
    school.addNewStudent(102, "Bob", 4, 20000, "882-777-112", "2020-01-10");

    // Show all students
    school.showAllStudents();

    // Update student information
    school.updateStudent(101, "Carison Mutuma Njunge", 1, 15000, "838-373-122");  // Update Carison fee

    // Show all students again to see the updated information
    school.showAllStudents();

    return 0;  
}