import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class FileManagementSystem {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean exit = false;

        while (!exit) {
            System.out.println("\nFile Management System");
            System.out.println("1. Create File");
            System.out.println("2. Write to File");
            System.out.println("3. Read from File");
            System.out.println("4. Delete File");
            System.out.println("5. List Files in Directory");
            System.out.println("6. Exit");
            
            System.out.print("Enter your choice: ");
            
            int choice = scanner.nextInt();
            scanner.nextLine();  // Newline

            switch (choice) {
                case 1:
                    createFile(scanner);
                    break;
                case 2:
                    writeFile(scanner);
                    break;
                case 3:
                    readFile(scanner);
                    break;
                case 4:
                    deleteFile(scanner);
                    break;
                case 5:
                    listFilesInDirectory(scanner);
                    break;
                case 6:
                    exit = true;
                    System.out.println("Exiting system...");
                    break;
                default:
                    System.out.println("Invalid choice. Try again.");
            }
        }
        scanner.close();
    }

    // Method to create file
    private static void createFile(Scanner scanner) {
        System.out.print("Enter name of file (with path): ");
        String fileName = scanner.nextLine();
        File file = new File(fileName);

        try {
            if (file.createNewFile()) {
                System.out.println("File created: " + file.getName());
            } else {
                System.out.println("File exists already.");
            }
        } catch (IOException e) {
            System.out.println("An error occurred while creating file.");
            e.printStackTrace();
        }
    }

    // Method to write to file
    private static void writeFile(Scanner scanner) {
        System.out.print("Enter name of file (with path): ");
        String fileName = scanner.nextLine();
        System.out.print("Enter content to write: ");
        String content = scanner.nextLine();

        try (FileWriter writer = new FileWriter(fileName, true)) {  // Append mode
            writer.write(content + "\n");
            System.out.println("Successfully wrote to the file.");
        } catch (IOException e) {
            System.out.println("An error occurred while writing to the file.");
            e.printStackTrace();
        }
    }

    // Method to read file
    private static void readFile(Scanner scanner) {
        System.out.print("Enter name of file (with path): ");
        String fileName = scanner.nextLine();
        File file = new File(fileName);

        try (Scanner fileReader = new Scanner(file)) {
            System.out.println("File content:");
            while (fileReader.hasNextLine()) {
                String line = fileReader.nextLine();
                System.out.println(line);
            }
        } catch (IOException e) {
            System.out.println("An error occurred while reading the file.");
            e.printStackTrace();
        }
    }

    // Method to delete file
    private static void deleteFile(Scanner scanner) {
        System.out.print("Enter name of file (with path): ");
        String fileName = scanner.nextLine();
        File file = new File(fileName);

        if (file.delete()) {
            System.out.println("Deleted file: " + file.getName());
        } else {
            System.out.println("Failed to delete file.");
        }
    }

    // Method to list files in directory
    private static void listFilesInDirectory(Scanner scanner) {
        System.out.print("Enter directory path: ");
        String directoryPath = scanner.nextLine();
        File directory = new File(directoryPath);

        if (directory.isDirectory()) {
            File[] filesList = directory.listFiles();
            if (filesList != null) {
                System.out.println("Files in directory:");
                for (File file : filesList) {
                    System.out.println(file.getName());
                }
            } else {
                System.out.println("Directory is empty.");
            }
        } else {
            System.out.println("Path entered is not a directory.");
        }
    }
}
