import java.util.ArrayList;
import java.util.LinkedList;
import java.util.HashSet;
import java.util.HashMap;
import java.util.Stack;

// Book class represents a book with title, author, ISBN, and genre
class Book {
    String title;
    String author;
    String isbn;
    String genre;

    // Constructor to initialize a book
    public Book(String title, String author, String isbn, String genre) {
        this.title = title;
        this.author = author;
        this.isbn = isbn;
        this.genre = genre;
    }

    // Method to display book details
    public void displayInfo() {
        System.out.println("Title: " + title + ", Author: " + author +
                           ", ISBN: " + isbn + ", Genre: " + genre);
    }
}

// Library class manages books using various containers
class Library {
    // Containers
    ArrayList<Book> bookList = new ArrayList<>();
    LinkedList<Book> waitingList = new LinkedList<>();
    HashSet<String> genreSet = new HashSet<>();
    HashMap<String, Book> bookMap = new HashMap<>();
    Stack<Book> undoStack = new Stack<>();

    // Add a book to the library
    public void addBook(Book book) {
        bookList.add(book);
        genreSet.add(book.genre);
        bookMap.put(book.isbn, book);
        undoStack.push(book);
        System.out.println("Added book: " + book.title);
    }

    // Remove a book from the library
    public void removeBook(String isbn) {
        Book book = bookMap.get(isbn);
        if (book != null) {
            bookList.remove(book);
            bookMap.remove(isbn);
            undoStack.push(book);
            System.out.println("Removed book: " + book.title);
        } else {
            System.out.println("Book not found.");
        }
    }

    // Display all books in the library
    public void displayAllBooks() {
        System.out.println("\nAll Books in the Library:");
        for (Book book : bookList) {
            book.displayInfo();
        }
    }

    // Display all unique genres
    public void displayGenres() {
        System.out.println("\nAvailable Genres:");
        for (String genre : genreSet) {
            System.out.println(genre);
        }
    }

    // Borrow a book (add to waiting list)
    public void borrowBook(String isbn) {
        Book book = bookMap.get(isbn);
        if (book != null) {
            waitingList.add(book);
            System.out.println("Borrowed book: " + book.title);
        } else {
            System.out.println("Book not available.");
        }
    }

    // Return a book (remove from waiting list)
    public void returnBook(String isbn) {
        Book book = bookMap.get(isbn);
        if (book != null && waitingList.contains(book)) {
            waitingList.remove(book);
            System.out.println("Returned book: " + book.title);
        } else {
            System.out.println("Book was not borrowed.");
        }
    }

    // Display waiting list
    public void displayWaitingList() {
        System.out.println("\nWaiting List:");
        for (Book book : waitingList) {
            book.displayInfo();
        }
    }

    // Undo last operation (add or remove)
    public void undoLastOperation() {
        if (!undoStack.isEmpty()) {
            Book book = undoStack.pop();
            if (bookList.contains(book)) {
                // If the book is in the list, remove it
                bookList.remove(book);
                bookMap.remove(book.isbn);
                System.out.println("Undo add operation: Removed " + book.title);
            } else {
                // If the book is not in the list, add it back
                bookList.add(book);
                bookMap.put(book.isbn, book);
                System.out.println("Undo remove operation: Added back " + book.title);
            }
        } else {
            System.out.println("No operations to undo.");
        }
    }
}

// Main class to run the program
public class LibraryManagementSystem {
    public static void main(String[] args) {
        // Create a new library
        Library myLibrary = new Library();

        // Create some books
        Book book1 = new Book("Harry Potter", "J.K. Rowling", "ISBN001", "Fantasy");
        Book book2 = new Book("The Hobbit", "J.R.R. Tolkien", "ISBN002", "Fantasy");
        Book book3 = new Book("1984", "George Orwell", "ISBN003", "Dystopian");

        // Add books to the library
        myLibrary.addBook(book1);
        myLibrary.addBook(book2);
        myLibrary.addBook(book3);

        // Display all books
        myLibrary.displayAllBooks();

        // Display all genres
        myLibrary.displayGenres();

        // Borrow a book
        myLibrary.borrowBook("ISBN001");

        // Display waiting list
        myLibrary.displayWaitingList();

        // Return a book
        myLibrary.returnBook("ISBN001");

        // Display waiting list again
        myLibrary.displayWaitingList();

        // Remove a book
        myLibrary.removeBook("ISBN002");

        // Display all books after removal
        myLibrary.displayAllBooks();

        // Undo last operation (remove)
        myLibrary.undoLastOperation();

        // Display all books after undo
        myLibrary.displayAllBooks();
    }
}
