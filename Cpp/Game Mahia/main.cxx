// main.cpp
// main function to create and interact with the Player and GameManager classes.
#include <iostream>
#include "GameManager.h"

using namespace std;

int main() {
    GameManager gameManager;  // Create a GameManager object

    // Add players
    gameManager.addPlayer("Erick");
    gameManager.addPlayer("Mwenda");

    // Set scores for the players
    gameManager.setPlayerScore("Erick", 15);
    gameManager.setPlayerScore("Mwenda", 60);

    // Display all players and their scores
    gameManager.displayAllPlayers();

    // Try to set a score for a non-existing player
    gameManager.setPlayerScore("Njagi", 38);  // This will display an error message

    return 0;
}

// code is organized into separate files for better structure and readability, 
// implemented a GameManager class to handle multiple players, and demonstrated 
// the addition and management of player scores.

// This structure makes the code modular and easier to manage as the program grows.

// Compile:
// g++ -o game main.cpp Player.cpp GameManager.cpp

// Run: ./game