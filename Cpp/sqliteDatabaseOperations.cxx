#include <iostream>
#include <sqlite3.h>  // Include the SQLite library

using namespace std;

// Install required libraries:
// sudo apt-get install libsqlite3-dev

int createTable(sqlite3* db);
int insertEntry(sqlite3* db, const string& name, int age);
int queryEntry(sqlite3* db);
int updateEntry(sqlite3* db, const string& name, int newAge);
int deleteEntry(sqlite3* db, const string& name);

int main() {
    sqlite3* db;
    int exit = 0;

    // Open SQLite database (creates if it doesn't exist)
    exit = sqlite3_open("database_file.db", &db);
    if (exit) {
        cerr << "Error opening SQLite database: " << sqlite3_errmsg(db) << endl;
        return exit;
    } else {
        cout << "Database opened successfully!" << endl;
    }

    // Create table
    createTable(db);

    // Insert data
    insertEntry(db, "Erick", 30);
    insertEntry(db, "Mwenda", 29);
    insertEntry(db, "Njagi", 49);

    // Query data
    queryEntry(db);

    // Update data
    updateEntry(db, "Erick", 31);
    queryEntry(db);  // Query again to see the updated data

    // Delete data
    deleteEntry(db, "Njagi");
    queryEntry(db);  // Query again to see the deleted data

    // Close the database connection
    sqlite3_close(db);
    cout << "Database connection closed." << endl;

    return 0;
}

// Function to create a table
int createTable(sqlite3* db) {
    string sql = "CREATE TABLE IF NOT EXISTS PEOPLE("
                 "ID INTEGER PRIMARY KEY AUTOINCREMENT, "
                 "NAME TEXT NOT NULL, "
                 "AGE INT NOT NULL);";

    char* errorMessage;
    int exit = sqlite3_exec(db, sql.c_str(), NULL, 0, &errorMessage);
    if (exit != SQLITE_OK) {
        cerr << "Error creating table: " << errorMessage << endl;
        sqlite3_free(errorMessage);
    } else {
        cout << "Table created successfully." << endl;
    }
    return exit;
}

// Function to insert data into the table
int insertEntry(sqlite3* db, const string& name, int age) {
    string sql = "INSERT INTO PEOPLE (NAME, AGE) VALUES('" + name + "', " + to_string(age) + ");";
    char* errorMessage;
    int exit = sqlite3_exec(db, sql.c_str(), NULL, 0, &errorMessage);
    if (exit != SQLITE_OK) {
        cerr << "Error inserting data: " << errorMessage << endl;
        sqlite3_free(errorMessage);
    } else {
        cout << "Data inserted successfully: " << name << ", " << age << endl;
    }
    return exit;
}

// Function to query data from the table
int queryEntry(sqlite3* db) {
    string sql = "SELECT * FROM PEOPLE;";
    sqlite3_stmt* stmt;

    int exit = sqlite3_prepare_v2(db, sql.c_str(), -1, &stmt, NULL);
    if (exit != SQLITE_OK) {
        cerr << "Error querying data: " << sqlite3_errmsg(db) << endl;
        return exit;
    }

    cout << "\nID | NAME    | AGE" << endl;
    cout << "-------------------" << endl;

    // Loop through each row
    while (sqlite3_step(stmt) == SQLITE_ROW) {
        int id = sqlite3_column_int(stmt, 0);
        const unsigned char* name = sqlite3_column_text(stmt, 1);
        int age = sqlite3_column_int(stmt, 2);

        cout << id << "  | " << name << " | " << age << endl;
    }

    sqlite3_finalize(stmt);  // Clean up after query
    return SQLITE_OK;
}

// Function to update data in the table
int updateEntry(sqlite3* db, const string& name, int newAge) {
    string sql = "UPDATE PEOPLE SET AGE = " + to_string(newAge) + " WHERE NAME = '" + name + "';";
    char* errorMessage;
    int exit = sqlite3_exec(db, sql.c_str(), NULL, 0, &errorMessage);
    if (exit != SQLITE_OK) {
        cerr << "Error updating data: " << errorMessage << endl;
        sqlite3_free(errorMessage);
    } else {
        cout << "Data updated successfully for " << name << " to age " << newAge << endl;
    }
    return exit;
}

// Function to delete data from the table
int deleteEntry(sqlite3* db, const string& name) {
    string sql = "DELETE FROM PEOPLE WHERE NAME = '" + name + "';";
    char* errorMessage;
    int exit = sqlite3_exec(db, sql.c_str(), NULL, 0, &errorMessage);
    if (exit != SQLITE_OK) {
        cerr << "Error deleting data: " << errorMessage << endl;
        sqlite3_free(errorMessage);
    } else {
        cout << "Data deleted successfully for " << name << endl;
    }
    return exit;
}