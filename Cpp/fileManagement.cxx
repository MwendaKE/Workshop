#include <iostream>
#include <filesystem>
#include <fstream>

using namespace std;
namespace fs = std::filesystem;

// file management operations using the C++17 <filesystem> library.
// This library provides a portable way to handle file system operations 
// such as file creation, deletion, renaming, checking existence, and 
// iterating over directories.

// make sure that your compiler supports C++17 or later,

void createFile(const fs::path& filePath);
void deleteFile(const fs::path& filePath);
void findFile(const fs::path& dirPath, const string& fileName);
void displayDirectoryContents(const fs::path& dirPath);
bool checkIfFileExists(const fs::path& filePath);

int main() {
    fs::path filePath = "file_example.txt";
    fs::path dirPath = fs::current_path();  // Get cwd

    // Create a file
    createFile(filePath);

    // Check if file exists
    if (checkIfFileExists(filePath)) {
        cout << "File exists: " << filePath << endl;
    } else {
        cout << "File does not exist." << endl;
    }

    // Display contents of the current directory
    displayDirectoryContents(dirPath);

    // Find a specific file in the directory
    findFile(dirPath, "file_example.txt");

    // Delete the file
    deleteFile(filePath);

    return 0;
}

// Function to create a file
void createFile(const fs::path& filePath) {
    ofstream file(filePath);  // Create and open the file
    if (file.is_open()) {
        file << "This is an example file." << endl;
        file.close();
        cout << "File created: " << filePath << endl;
    } else {
        cerr << "Error creating file: " << filePath << endl;
    }
}

// Function to delete a file
void deleteFile(const fs::path& filePath) {
    if (fs::exists(filePath)) {
        fs::remove(filePath);  // Delete the file
        cout << "File deleted: " << filePath << endl;
    } else {
        cerr << "File not found for deletion: " << filePath << endl;
    }
}

// Function to find a file in a directory
void findFile(const fs::path& dirPath, const string& fileName) {
    bool fileFound = false;
    for (const auto& entry : fs::directory_iterator(dirPath)) {
        if (entry.path().filename() == fileName) {
            cout << "File found: " << entry.path() << endl;
            fileFound = true;
            break;
        }
    }
    if (!fileFound) {
        cout << "File not found: " << fileName << endl;
    }
}

// Function to display contents of a directory
void displayDirectoryContents(const fs::path& dirPath) {
    cout << "\nDirectory contents of " << dirPath << ":" << endl;
    for (const auto& entry : fs::directory_iterator(dirPath)) {
        cout << entry.path().filename() << endl;  // Display the filename only
    }
}

// Function to check if a file exists
bool checkIfFileExists(const fs::path& filePath) {
    return fs::exists(filePath);  // Check if the file exists
}