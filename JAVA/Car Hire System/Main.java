// Main class to test the system

public class Main {
    public static void main(String[] args) {
        // Create the rental system
        RentalSystem rentalSystem = new RentalSystem();

        // Add some cars to the system
        Car economyCar = new EconomyCar("ABC123", "Toyota");
        Car luxuryCar = new LuxuryCar("XYZ789", "BMW");
        Car suvCar = new SUVCar("JKL456", "Nissan");

        rentalSystem.addCar(economyCar);
        rentalSystem.addCar(luxuryCar);
        rentalSystem.addCar(suvCar);

        // Add customers
        Customer customer1 = new Customer("John Doe", "C001");
        Customer customer2 = new Customer("Jane Smith", "C002");

        rentalSystem.addCustomer(customer1);
        rentalSystem.addCustomer(customer2);

        // Display available cars
        rentalSystem.displayAvailableCars();

        // Rent a car
        rentalSystem.rentCar(customer1, economyCar, 3);  // John rents economy car for 3 days
        rentalSystem.rentCar(customer2, luxuryCar, 2);   // Jane rents luxury car for 2 days

        // Display rented cars
        rentalSystem.displayRentedCars();

        // Return a car
        rentalSystem.returnCar(customer1, economyCar);  // John returns his car

        // Display available and rented cars after return
        rentalSystem.displayAvailableCars();
        rentalSystem.displayRentedCars();
    }
}

// Insight:

// Abstraction: Car is an abstract class with an abstract method calculateRentalCost, forcing subclasses to provide their own implementation.
// Inheritance: EconomyCar, LuxuryCar, and SUVCar inherit from Car and implement specific rental costs.
// Polymorphism: All car types (EconomyCar, LuxuryCar, SUVCar) are referenced using the Car type.
// Interface: The RentalService interface defines the core rental operations, and RentalSystem implements this interface.
