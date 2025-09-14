// GameManager.h
#ifndef GAMEMANAGER_H  // Header guard to prevent multiple inclusions
#define GAMEMANAGER_H

#include <vector>
#include "Player.h"

// class definition for GameManager, which manages multiple players.

class GameManager {
    public:
        void addPlayer(const std::string& name);   // Method to add a player
        void setPlayerScore(const std::string& name, int score);  // Method to set a player's score
        void displayAllPlayers() const;              // Method to display all players and their scores

    private:
        std::vector<Player> players;  // List of players
};

#endif // GAMEMANAGER_H