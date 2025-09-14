#include <iostream>
#include <fstream>
#include <string>

using namespace std;

// Function prototypes
void writeToFile(const string& fileName);
void readFromFile(const string& fileName);

int main() {
    string fileName = "textfile.txt";

    // Write to file
    writeToFile(fileName);

    // Read from file
    readFromFile(fileName);

    return 0;
}

// Function to write data to file
void writeToFile(const string& fileName) {
    ofstream file(fileName);  // ofstream object for writing

    // Check if the file is open
    if (!file.is_open()) {
        cerr << "Error: Could not open the file for writing!" << endl;
        return;
    }

    // Write some text to the file
    file << "Hello world! This is my first line to the file." << endl;
    file << "And this is my second line." << endl;
    file << "And this is my fucking third." << endl;

    // Close the file
    file.close();
    cout << "Data written to the file successfully!" << endl;
}

// Function to read data from file
void readFromFile(const string& fileName) {
    ifstream file(fileName);  // ifstream object for reading
    string line;

    // Check if the file is open
    if (!file.is_open()) {
        cerr << "Error: Could not open the file for reading!" << endl;
        return;
    }

    // Read the file line by line and print it
    cout << "\nReading data from file:" << endl;
    while (getline(file, line)) {
        cout << line << endl;
    }

    // Close the file
    file.close();
    cout << "Finished reading the file." << endl;
}