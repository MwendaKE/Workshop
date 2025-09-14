import java.util.ArrayList;
import java.util.LinkedList;
import java.util.HashSet;
import java.util.HashMap;
import java.util.Stack;

class School {
    // Containers for different parts of the school
    ArrayList<String> students = new ArrayList<>();
    LinkedList<String> arrivalQueue = new LinkedList<>();
    HashSet<String> subjects = new HashSet<>();
    HashMap<String, Integer> scores = new HashMap<>();
    Stack<String> eventLog = new Stack<>();

    // Add a student to the ArrayList
    void addStudent(String name) {
        students.add(name);
        eventLog.push("Added student: " + name);
    }

    // Display all students
    void displayStudents() {
        System.out.println("Students List:");
        for (String student : students) {
            System.out.println("- " + student);
        }
    }

    // Record student arrival in the LinkedList
    void recordArrival(String student) {
        arrivalQueue.add(student);
        eventLog.push(student + " arrived at school.");
    }

    // Display the arrival order
    void displayArrivals() {
        System.out.println("Arrival Order:");
        for (String student : arrivalQueue) {
            System.out.println("- " + student);
        }
    }

    // Add a subject to the HashSet
    void addSubject(String subject) {
        subjects.add(subject);
        eventLog.push("Added subject: " + subject);
    }

    // Display all subjects
    void displaySubjects() {
        System.out.println("Subjects Offered:");
        for (String subject : subjects) {
            System.out.println("- " + subject);
        }
    }

    // Record a student's score in the HashMap
    void recordScore(String student, int score) {
        scores.put(student, score);
        eventLog.push("Recorded score for " + student + ": " + score);
    }

    // Display all scores
    void displayScores() {
        System.out.println("Student Scores:");
        for (String student : scores.keySet()) {
            System.out.println("- " + student + ": " + scores.get(student));
        }
    }

    // Display the event log from the Stack
    void displayEventLog() {
        System.out.println("Event Log:");
        while (!eventLog.isEmpty()) {
            System.out.println(eventLog.pop());
        }
    }
}

public class SchoolManagement {
    public static void main(String[] args) {
        School mySchool = new School();
        
        // Add students
        mySchool.addStudent("Alice");
        mySchool.addStudent("Bob");

        // Record arrivals
        mySchool.recordArrival("Alice");
        mySchool.recordArrival("Bob");

        // Add subjects
        mySchool.addSubject("Math");
        mySchool.addSubject("Science");

        // Record scores
        mySchool.recordScore("Alice", 85);
        mySchool.recordScore("Bob", 90);

        // Display all data
        mySchool.displayStudents();      // Display student list
        mySchool.displayArrivals();      // Display arrival order
        mySchool.displaySubjects();      // Display subjects
        mySchool.displayScores();        // Display scores
        mySchool.displayEventLog();      // Display the event log
    }
}
