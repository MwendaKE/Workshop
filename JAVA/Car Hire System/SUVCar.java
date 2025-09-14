// SUVCar.java
// Specific Car Class
// Inherits from Car and implement specific behaviors.

public class SUVCar extends Car {
    public SUVCar(String licensePlate, String brand) {
        super(licensePlate, brand);
    }

    // Override method to calculate rental cost for SUV car
    @Override
    public double calculateRentalCost(int days) {
        return days * 70.0;  // SUV rental cost is $70 per day
    }
}

}