import java.util.Scanner;

// Bayes' theorem is used to calculate the conditional probability
// of an event, given the probability of other related events.

public class BayesTheoremSolver {

    public static void main(String[] args) {
        // Create a scanner to get user input
        Scanner scanner = new Scanner(System.in);

        // Get the values from user
        System.out.print("Enter P(A) (Prior Probability of A): ");
        double pA = scanner.nextDouble();

        System.out.print("Enter P(B|A) (Likelihood of B given A): ");
        double pBA = scanner.nextDouble();

        System.out.print("Enter P(B) (Total Probability of B): ");
        double pB = scanner.nextDouble();

        // Calculate P(A|B) using Bayes Theorem
        double pAB = bayesTheorem(pA, pBA, pB);

        // Print the result
        System.out.println("The Posterior Probability P(A|B) is: " + pAB);

        // Close the scanner
        scanner.close();
    }

    // Method to calculate Bayes Theorem
    public static double bayesTheorem(double pA, double pBA, double pB) {
        return (pBA * pA) / pB;
    }
}
