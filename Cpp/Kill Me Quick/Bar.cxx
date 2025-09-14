#include "Bar.h"
#include <iostream>

// Constructor
Bar::Bar() {}

// Add a new beer to the system
void Bar::addBeer(int id, const std::string& name, double alcoholContent, double amount, int quantityRemaining, double popularityPercent) {
    Beer newBeer(id, name, alcoholContent, amount, quantityRemaining, popularityPercent);
    beers.push_back(newBeer);  // Add new beer to the vector
    std::cout << "Beer added: " << name << std::endl;
}

// Update an existing beer's information
void Bar::updateBeer(int id, const std::string& name, double alcoholContent, double amount, int quantityRemaining, double popularityPercent) {
    for (auto& beer : beers) {
        if (beer.getId() == id) {
            // Update the beer details by creating a new Beer object
            beer = Beer(id, name, alcoholContent, amount, quantityRemaining, popularityPercent);
            std::cout << "Beer updated: " << name << std::endl;
            return;
        }
    }
    std::cout << "Beer with ID " << id << " not found." << std::endl;
}

// Show all beers in the system
void Bar::showAllBeers() {
    std::cout << "\nList of Beers:" << std::endl;
    for (const auto& beer : beers) {
        std::cout << "ID: " << beer.getId() << ", Name: " << beer.getName() 
                  << ", Alcohol Content: " << beer.getAlcoholContent() 
                  << ", Amount Sold: " << beer.getAmount() 
                  << ", Quantity Remaining: " << beer.getQuantityRemaining() 
                  << ", Popularity Percent: " << beer.getPopularityPercent() << "%" << std::endl;
    }
}