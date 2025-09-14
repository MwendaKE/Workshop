#ifndef BAR_H
#define BAR_H

#include <vector>
#include "Beer.h"

class Bar {
   public:
       Bar();                                // Constructor
       void addBeer(int id, const std::string& name, double alcoholContent, double amount, int quantityRemaining, double popularityPercent); // Add new beer
       void updateBeer(int id, const std::string& name, double alcoholContent, double amount, int quantityRemaining, double popularityPercent); // Update beer
       void showAllBeers();                  // Display all beers
 
   private:
       std::vector<Beer> beers;              // Vector to store beers
};

#endif // BAR_H