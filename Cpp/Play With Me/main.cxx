// main.cxx / main.cpp
#include <iostream>
#include "Player.h"

using namespace std;

int main() {
    // Create a player object
    Player player1("Alice");

    // Set the player's score
    player1.setScore(50);

    // Display the player's name and score
    cout << "Player Name: " << player1.getName() << endl;
    cout << "Player Score: " << player1.getScore() << endl;

    return 0;
}