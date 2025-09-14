#include <iostream>

using namespace std;


void increasePlayerScore(int* scorePointer);  // Function using a pointer
void showPlayerScore(int& scoreReference);     // Function using a reference

int main() {
    int playerScore = 0;  // Start with a score of 0

    cout << "Initial player score: " << playerScore << endl;

    // Increase the score using a pointer
    increasePlayerScore(&playerScore);  // Pass the address of playerScore

    // Show the updated score using a reference
    showPlayerScore(playerScore);  // Pass playerScore as a reference

    return 0;
}

// Function to increase the score using a pointer
void increasePlayerScore(int* scorePointer) {
    *scorePointer += 10;  // Increase the score by 10 using dereferencing
    cout << "Score increased by 10 Points!" << endl;
}

// Function to show the score using a reference
void showPlayerScore(int& scoreReference) {
    cout << "Updated player score: " << scoreReference << endl;
}