#include <iostream>
#include "Bar.h"

using namespace std;

int main() {
    Bar bar;  // Create a Bar object

    // Add new beers
    bar.addBeer(1, "Chrome", 5.0, 700.0, 25, 85.0);
    bar.addBeer(2, "Konyagi", 6.5, 350.0, 200, 95.0);
    bar.addBeer(3, "Tusker", 8.0, 250.0, 5, 90.0);
    bar.addBeer(4, "Guiness", 6.0, 250.0, 3, 90.0)

    // Show all beers
    bar.showAllBeers();

    // Update a beer's information
    bar.updateBeer(2, "Kenya Cane", 37.0, 1050.0, 12, 85.0);  // Update Chrome to Kenya Cane

    // Show all beers again to see the updated information
    bar.showAllBeers();

    return 0;  
}