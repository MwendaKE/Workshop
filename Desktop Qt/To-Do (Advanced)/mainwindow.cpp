#include "mainwindow.h"
#include <QMessageBox>
#include <QCheckBox>
#include <QBrush>
#include <QFont>

MainWindow::MainWindow(QWidget *parent) : QWidget(parent) {
    // --- Widgets ---
    QLabel *title = new QLabel("📝 Advanced To-Do List", this);
    taskInput = new QLineEdit(this);
    dueDateInput = new QDateEdit(this);
    dueDateInput->setCalendarPopup(true); // User-friendly date selection
    taskList = new QListWidget(this);

    addButton = new QPushButton("Add Task", this);
    removeButton = new QPushButton("Remove Task", this);
    deleteAllButton = new QPushButton("Delete All Tasks", this);

    // --- Layouts ---
    QHBoxLayout *inputLayout = new QHBoxLayout;
    inputLayout->addWidget(taskInput);
    inputLayout->addWidget(dueDateInput);
    inputLayout->addWidget(addButton);

    QHBoxLayout *buttonsLayout = new QHBoxLayout;
    buttonsLayout->addWidget(removeButton);
    buttonsLayout->addWidget(deleteAllButton);

    QVBoxLayout *mainLayout = new QVBoxLayout(this);
    mainLayout->addWidget(title);
    mainLayout->addLayout(inputLayout);
    mainLayout->addWidget(taskList);
    mainLayout->addLayout(buttonsLayout);

    setLayout(mainLayout);
    setWindowTitle("Advanced To-Do App");
    resize(400, 500);

    // --- Connect signals ---
    connect(addButton, &QPushButton::clicked, this, &MainWindow::addTask);
    connect(removeButton, &QPushButton::clicked, this, &MainWindow::removeTask);
    connect(deleteAllButton, &QPushButton::clicked, this, &MainWindow::removeAllTasks);
    connect(taskList, &QListWidget::itemChanged, this, &MainWindow::toggleTaskDone);

    // --- Database ---
    setupDatabase();
    loadTasksFromDB();
}

MainWindow::~MainWindow() {
    if (db.isOpen()) db.close();
}

// --- Setup SQLite DB ---
void MainWindow::setupDatabase() {
    db = QSqlDatabase::addDatabase("QSQLITE");
    db.setDatabaseName("tasks.db");

    if (!db.open()) {
        QMessageBox::critical(this, "Database Error", db.lastError().text());
        return;
    }

    // Create table with done status and due date
    QSqlQuery query;
    query.exec("CREATE TABLE IF NOT EXISTS tasks ("
               "id INTEGER PRIMARY KEY AUTOINCREMENT, "
               "task TEXT NOT NULL, "
               "done INTEGER DEFAULT 0, "
               "duedate TEXT)");
}

// --- Load tasks from DB ---
void MainWindow::loadTasksFromDB() {
    taskList->clear();

    QSqlQuery query("SELECT id, task, done, duedate FROM tasks ORDER BY id ASC");
    while (query.next()) {
        QString text = query.value("task").toString();
        bool done = query.value("done").toInt();
        QString due = query.value("duedate").toString();

        QString displayText = text;
        if (!due.isEmpty()) displayText += " (Due: " + due + ")";

        QListWidgetItem *item = new QListWidgetItem(displayText);
        item->setFlags(item->flags() | Qt::ItemIsUserCheckable | Qt::ItemIsEditable);
        item->setCheckState(done ? Qt::Checked : Qt::Unchecked);

        // Strike-through font if done
        QFont font = item->font();
        font.setStrikeOut(done);
        item->setFont(font);

        taskList->addItem(item);
    }
}

// --- Add task ---
void MainWindow::addTask() {
    QString text = taskInput->text().trimmed();
    QString due = dueDateInput->date().toString("yyyy-MM-dd");

    if (text.isEmpty()) return;

    // Insert into DB
    QSqlQuery query;
    query.prepare("INSERT INTO tasks (task, duedate) VALUES (:task, :duedate)");
    query.bindValue(":task", text);
    query.bindValue(":duedate", due);

    if (!query.exec()) {
        QMessageBox::warning(this, "Error", "Failed to add task: " + query.lastError().text());
        return;
    }

    // Add to list
    QListWidgetItem *item = new QListWidgetItem(text + " (Due: " + due + ")");
    item->setFlags(item->flags() | Qt::ItemIsUserCheckable | Qt::ItemIsEditable);
    item->setCheckState(Qt::Unchecked);
    taskList->addItem(item);

    taskInput->clear();
}

// --- Remove selected task ---
void MainWindow::removeTask() {
    QListWidgetItem *item = taskList->currentItem();
    if (!item) return;

    QString text = item->text();
    QSqlQuery query;
    query.prepare("DELETE FROM tasks WHERE task || ' (Due: ' || duedate || ')' = :text");
    query.bindValue(":text", text);
    query.exec();

    delete item;
}

// --- Remove all tasks ---
void MainWindow::removeAllTasks() {
    QSqlQuery query;
    query.exec("DELETE FROM tasks");
    taskList->clear();
}

// --- Toggle done/undone ---
void MainWindow::toggleTaskDone(QListWidgetItem *item) {
    if (!item) return;

    bool done = (item->checkState() == Qt::Checked);

    // Update font strike-through
    QFont font = item->font();
    font.setStrikeOut(done);
    item->setFont(font);

    // Update DB
    QString text = item->text();
    QString taskName = text;
    QString due = "";
    int idx = text.indexOf(" (Due: ");
    if (idx != -1) {
        taskName = text.left(idx);
        due = text.mid(idx + 7, text.length() - idx - 8); // extract due date
    }

    QSqlQuery query;
    query.prepare("UPDATE tasks SET done = :done WHERE task = :task AND duedate = :duedate");
    query.bindValue(":done", done ? 1 : 0);
    query.bindValue(":task", taskName);
    query.bindValue(":duedate", due);
    query.exec();
}

