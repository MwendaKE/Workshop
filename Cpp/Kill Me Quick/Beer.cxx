#include "Beer.h"

// Constructor to initialize beer details
Beer::Beer(int id, const std::string& name, double alcoholContent, double amount, int quantityRemaining, double popularityPercent)
    : id(id), name(name), alcoholContent(alcoholContent), amount(amount), quantityRemaining(quantityRemaining), popularityPercent(popularityPercent) {}

// Get beer ID
int Beer::getId() const {
    return id;
}

// Get beer name
std::string Beer::getName() const {
    return name;
}

// Get alcohol content
double Beer::getAlcoholContent() const {
    return alcoholContent;
}

// Get amount sold
double Beer::getAmount() const {
    return amount;
}

// Get quantity remaining
int Beer::getQuantityRemaining() const {
    return quantityRemaining;
}

// Get popularity percent
double Beer::getPopularityPercent() const {
    return popularityPercent;
}