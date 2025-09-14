// LuxuryCar.java
// Specific Car Class
// Inherits from Car and implement specific behaviors.

public class LuxuryCar extends Car {
    public LuxuryCar(String licensePlate, String brand) {
        super(licensePlate, brand);
    }

    // Override method to calculate rental cost for luxury car
    @Override
    public double calculateRentalCost(int days) {
        return days * 100.0;  // Luxury car rental cost is $100 per day
    }
}

}