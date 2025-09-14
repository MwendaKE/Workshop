// EconomyCar.java
// Specific Car Class
// Inherits from Car and implement specific behaviors.

public class EconomyCar extends Car {
    public EconomyCar(String licensePlate, String brand) {
        super(licensePlate, brand);
    }

    // Override method to calculate rental cost for economy car
    @Override
    public double calculateRentalCost(int days) {
        return days * 30.0;  // Economy car rental cost is $30 per day
    }
}
