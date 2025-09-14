#include <iostream>

using namespace std;


// A pointer holds the memory address of a variable.
// A reference is like a nickname for an existing variable. 
// It does not create a new variable, it just refers to the original one.

void showPointerExample();
void showReferenceExample();

int main() {
    showPointerExample();  // Call the pointer example function
    showReferenceExample();  // Call the reference example function

    return 0;
}

// Function to explain pointers
void showPointerExample() {
    int myNumber = 10;  // A simple number
    int* myPointer = &myNumber;  // Pointer stores the address of myNumber

    // Output the value of myNumber and the pointer details
    cout << "Pointer Example:" << endl;
    cout << "myNumber = " << myNumber << endl;
    cout << "myPointer (memory address of myNumber) = " << myPointer << endl;
    cout << "Value at myPointer = " << *myPointer << endl;  // Dereference the pointer to get the value of myNumber
    cout << endl;
}

// Function to explain references
void showReferenceExample() {
    int myNumber = 20;  // Another simple number
    int& myReference = myNumber;  // Reference to myNumber

    // Output the value of myNumber and the reference details
    cout << "Reference Example:" << endl;
    cout << "myNumber = " << myNumber << endl;
    cout << "myReference (just another name for myNumber) = " << myReference << endl;
    cout << endl;
}

// Pointers allow us to directly manipulate the variable in memory. 
// References  provide a convenient way to pass variables to functions without making copies. 