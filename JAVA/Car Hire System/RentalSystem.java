import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;

// Implements RentalService
// Handles the main logic of the car rental system.

public class RentalSystem implements RentalService {
    // Container to hold available cars
    private ArrayList<Car> availableCars = new ArrayList<>();

    // HashMap to associate customers with rented cars
    private HashMap<Customer, Car> rentedCars = new HashMap<>();

    // HashSet to hold unique customers
    private HashSet<Customer> customers = new HashSet<>();

    // Add a car to the available cars list
    public void addCar(Car car) {
        availableCars.add(car);
    }

    // Add a customer to the system
    public void addCustomer(Customer customer) {
        customers.add(customer);
    }

    // Rent a car to a customer
    @Override
    public void rentCar(Customer customer, Car car, int days) {
        if (availableCars.contains(car)) {
            availableCars.remove(car);  // Remove car from available cars
            rentedCars.put(customer, car);  // Associate the car with the customer
            System.out.println("Car rented by " + customer.getId() + " for " + days + " days.");
            System.out.println("Rental cost: $" + car.calculateRentalCost(days));
        } else {
            System.out.println("Car is not available.");
        }
    }

    // Return a car
    @Override
    public void returnCar(Customer customer, Car car) {
        if (rentedCars.containsKey(customer)) {
            rentedCars.remove(customer);
            availableCars.add(car);
            System.out.println("Car returned by " + customer.getId());
        } else {
            System.out.println("No car was rented by this customer.");
        }
    }

    // Display all available cars
    @Override
    public void displayAvailableCars() {
        System.out.println("\nAvailable Cars:");
        for (Car car : availableCars) {
            car.displayInfo();
        }
    }

    // Display all rented cars
    @Override
    public void displayRentedCars() {
        System.out.println("\nRented Cars:");
        for (Customer customer : rentedCars.keySet()) {
            System.out.print("Rented by: ");
            customer.displayInfo();
            rentedCars.get(customer).displayInfo();
        }
    }
}

}