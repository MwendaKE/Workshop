#include "mainwindow.h"

MainWindow::MainWindow(QWidget *parent) : QWidget(parent) {
    // --- Widgets ---
    QLabel *title = new QLabel("📝 Simple To-Do List", this);
    taskInput = new QLineEdit(this);
    taskList = new QListWidget(this);
    addButton = new QPushButton("Add Task", this);
    removeButton = new QPushButton("Remove Task", this);

    // --- Layouts ---
    QHBoxLayout *inputLayout = new QHBoxLayout;
    inputLayout->addWidget(taskInput);
    inputLayout->addWidget(addButton);

    QVBoxLayout *mainLayout = new QVBoxLayout(this);
    mainLayout->addWidget(title);
    mainLayout->addLayout(inputLayout);
    mainLayout->addWidget(taskList);
    mainLayout->addWidget(removeButton);
    setLayout(mainLayout);

    setWindowTitle("Simple To-Do App");
    resize(300, 400);

    // --- Connections ---
    connect(addButton, &QPushButton::clicked, this, &MainWindow::addTask);
    connect(removeButton, &QPushButton::clicked, this, &MainWindow::removeTask);

    // --- Load tasks from file on startup ---
    loadTasks();
}

// Add task
void MainWindow::addTask() {
    QString taskText = taskInput->text().trimmed();
    if (!taskText.isEmpty()) {
        taskList->addItem(taskText); // Add to list widget
        taskInput->clear();          // Clear input
        saveTasks();                 // Save immediately
    }
}

// Remove selected task
void MainWindow::removeTask() {
    QListWidgetItem *item = taskList->currentItem();
    if (item) {
        delete item; // Remove from widget
        saveTasks(); // Save immediately
    }
}

// Load tasks from "tasks.txt"
void MainWindow::loadTasks() {
    QFile file("tasks.txt");       // File in the same folder
    if (file.open(QIODevice::ReadOnly | QIODevice::Text)) {
        QTextStream in(&file);     // Stream to read text
        while (!in.atEnd()) {
            QString line = in.readLine().trimmed();
            if (!line.isEmpty()) {
                taskList->addItem(line); // Add each line as a task
            }
        }
        file.close();
    }
}

// Save tasks to "tasks.txt"
void MainWindow::saveTasks() {
    QFile file("tasks.txt");       // Same file
    if (file.open(QIODevice::WriteOnly | QIODevice::Text)) {
        QTextStream out(&file);    // Stream to write text
        for (int i = 0; i < taskList->count(); ++i) {
            QListWidgetItem *item = taskList->item(i);
            out << item->text() << "\n"; // Write each task line by line
        }
        file.close();
    }
}

