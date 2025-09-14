// Abstract Class for Cars
// Represents different types of cars (e.g., Economy, Luxury)
// Each car type will have different rental costs.

public abstract class Car {
    private String licensePlate;
    private String brand;

    // Constructor
    public Car(String licensePlate, String brand) {
        this.licensePlate = licensePlate;
        this.brand = brand;
    }

    // Abstract method to calculate rental cost
    public abstract double calculateRentalCost(int days);

    // Method to display car details
    public void displayInfo() {
        System.out.println("License Plate: " + licensePlate + ", Brand: " + brand);
    }

    // Getters
    public String getLicensePlate() {
        return licensePlate;
    }
}
