// Implementation of the GameManager class methods.
// GameManager.cxx
#include "GameManager.h"
#include <iostream>

// Method to add a player
void GameManager::addPlayer(const std::string& name) {
    players.emplace_back(name);  // Add a new player to the vector
}

// Method to set a player's score
void GameManager::setPlayerScore(const std::string& name, int score) {
    for (auto& player : players) {
        if (player.getName() == name) {
            player.setScore(score);  // Set the score for the matching player
            return;
        }
    }
    std::cout << "Player not found: " << name << std::endl;
}

// Method to display all players and their scores
void GameManager::displayAllPlayers() const {
    std::cout << "\nPlayers and Scores:" << std::endl;
    for (const auto& player : players) {
        std::cout << "Name: " << player.getName() << ", Score: " << player.getScore() << std::endl;
    }
}