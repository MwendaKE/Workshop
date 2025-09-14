// Player.cxx
#include "Player.h"

// Constructor to initialize the player's name and score
Player::Player(const std::string& name) : name(name), score(0) {}

// Method to set the score
void Player::setScore(int newScore) {
    score = newScore;
}

// Method to get the score
int Player::getScore() const {
    return score;
}

// Method to get the player's name
std::string Player::getName() const {
    return name;
}