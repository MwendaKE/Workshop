// Include the header file for MainWindow — gives us access to class members
#include "mainwindow.h"

// ============================
// Constructor Implementation
// ============================
MainWindow::MainWindow(QWidget *parent) : QWidget(parent) {
    // --- Create Widgets ---
    // QLabel is used to show simple static text on the screen
    QLabel *title = new QLabel("📝 Simple To-Do List", this);

    // QLineEdit is a single-line text input field
    taskInput = new QLineEdit(this);

    // QListWidget is used to display a vertical list of text items
    taskList = new QListWidget(this);

    // QPushButton is a clickable button
    addButton = new QPushButton("Add Task", this);
    removeButton = new QPushButton("Remove Task", this);

    // --- Create Layouts ---
    // QHBoxLayout arranges widgets horizontally (side by side)
    QHBoxLayout *inputLayout = new QHBoxLayout;
    inputLayout->addWidget(taskInput);  // Add the input field on the left
    inputLayout->addWidget(addButton);  // Add the Add button on the right

    // QVBoxLayout arranges widgets vertically (top to bottom)
    QVBoxLayout *mainLayout = new QVBoxLayout(this);
    mainLayout->addWidget(title);        // Add title label at the top
    mainLayout->addLayout(inputLayout);  // Add input row (text + button)
    mainLayout->addWidget(taskList);     // Add the task list
    mainLayout->addWidget(removeButton); // Add the Remove button at the bottom

    // Apply this layout to the MainWindow
    setLayout(mainLayout);

    // Set the window title (shown in the title bar)
    setWindowTitle("Simple To-Do App");

    // Set the window size (width = 300px, height = 400px)
    resize(300, 400);

    // --- Connect Buttons to Actions ---
    // When Add button is clicked → call addTask()
    connect(addButton, &QPushButton::clicked, this, &MainWindow::addTask);

    // When Remove button is clicked → call removeTask()
    connect(removeButton, &QPushButton::clicked, this, &MainWindow::removeTask);
}

// ============================
// Slot 1: Add a Task
// ============================
void MainWindow::addTask() {
    // Get text from input field and remove any spaces at the start/end
    QString taskText = taskInput->text().trimmed();

    // Only add if the text box is not empty
    if (!taskText.isEmpty()) {
        // Add the text as a new item to the task list
        taskList->addItem(taskText);

        // Clear the input field for the next entry
        taskInput->clear();
    }
}

// ============================
// Slot 2: Remove Selected Task
// ============================
void MainWindow::removeTask() {
    // Get the currently selected item in the task list
    QListWidgetItem *item = taskList->currentItem();

    // If an item is selected, delete it
    if (item) {
        delete item;
    }
}

