// Player.h
#ifndef PLAYER_H  // Header guard to prevent multiple inclusions
#define PLAYER_H

#include <string>

class Player {
    public:
        Player(const std::string& name);  // Constructor to initialize the player
        void setScore(int newScore);       // Method to set the score
        int getScore() const;              // Method to get the score
        std::string getName() const;       // Method to get the player's name

    private:
        std::string name;                  // Player's name
        int score;                         // Player's score
};

#endif // PLAYER_H