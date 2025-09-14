#ifndef BEER_H
#define BEER_H

#include <string>

class Beer {
    public:
    Beer(int id, const std::string& name, double alcoholContent, double amount, int quantityRemaining, double popularityPercent);

        int getId() const;                    // Get beer ID
        std::string getName() const;          // Get beer name
        double getAlcoholContent() const;     // Get alcohol content
        double getAmount() const;              // Get amount sold
        int getQuantityRemaining() const;      // Get quantity remaining
        double getPopularityPercent() const;   // Get popularity percent

    private:
        int id;                                // Beer ID
        std::string name;                      // Beer name
        double alcoholContent;                 // Alcohol content
        double amount;                         // Amount sold
        int quantityRemaining;                 // Quantity remaining
        double popularityPercent;              // Popularity percent
};

#endif // BEER_H