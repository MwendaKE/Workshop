#include "mainwindow.h"
#include <QMessageBox>

MainWindow::MainWindow(QWidget *parent) : QWidget(parent) {
    // --- Widgets ---
    QLabel *title = new QLabel("📝 To-Do List (SQLite)", this);
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

    setWindowTitle("To-Do App with SQLite");
    resize(300, 400);

    // --- Connect buttons ---
    connect(addButton, &QPushButton::clicked, this, &MainWindow::addTask);
    connect(removeButton, &QPushButton::clicked, this, &MainWindow::removeTask);

    // --- Database ---
    setupDatabase();
    loadTasksFromDB();
}

MainWindow::~MainWindow() {
    if (db.isOpen())
        db.close();
}

// Initialize the SQLite database
void MainWindow::setupDatabase() {
    db = QSqlDatabase::addDatabase("QSQLITE"); // SQLite driver
    db.setDatabaseName("tasks.db");           // DB file in current folder

    if (!db.open()) {
        QMessageBox::critical(this, "Database Error", db.lastError().text());
        return;
    }

    // Create table if it doesn't exist
    QSqlQuery query;
    query.exec("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT NOT NULL)");
}

// Load tasks from database into the list widget
void MainWindow::loadTasksFromDB() {
    taskList->clear();
    QSqlQuery query("SELECT id, task FROM tasks ORDER BY id ASC");
    while (query.next()) {
        QString taskText = query.value(1).toString();
        taskList->addItem(taskText);
    }
}

// Add task to list widget and database
void MainWindow::addTask() {
    QString text = taskInput->text().trimmed();
    if (text.isEmpty()) return;

    // Add to DB
    QSqlQuery query;
    query.prepare("INSERT INTO tasks (task) VALUES (:task)");
    query.bindValue(":task", text);

    if (!query.exec()) {
        QMessageBox::warning(this, "Error", "Failed to add task: " + query.lastError().text());
        return;
    }

    // Add to list and clear input
    taskList->addItem(text);
    taskInput->clear();
}

// Remove selected task from list and database
void MainWindow::removeTask() {
    QListWidgetItem *item = taskList->currentItem();
    if (!item) return;

    QString text = item->text();

    // Delete from database
    QSqlQuery query;
    query.prepare("DELETE FROM tasks WHERE task = :task");
    query.bindValue(":task", text);
    if (!query.exec()) {
        QMessageBox::warning(this, "Error", "Failed to remove task: " + query.lastError().text());
        return;
    }

    // Remove from widget
    delete item;
}

