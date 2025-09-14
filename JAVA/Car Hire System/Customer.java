// Class to manage customers.

public class Customer {
    private String name;
    private String id;

    // Constructor
    public Customer(String name, String id) {
        this.name = name;
        this.id = id;
    }

    // Display customer details
    public void displayInfo() {
        System.out.println("Customer Name: " + name + ", ID: " + id);
    }

    // Getters
    public String getId() {
        return id;
    }
}
