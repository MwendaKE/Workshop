// Interface defining rental operations

public interface RentalService {
    void rentCar(Customer customer, Car car, int days);
    void returnCar(Customer customer, Car car);
    void displayAvailableCars();
    void displayRentedCars();
}
