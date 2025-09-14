#include <iostream>
#include <map>
#include <string>

using namespace std;

// std::map: A collection of key-value pairs, where keys are unique and values
//are associated with each key. It is sorted by key.

// Function prototypes
void insertEntry(map<string, string> &phoneBook, const string &name, const string &number);
void displayphoneBook(const map<string, string> &phoneBook);
void findEntry(const map<string, string> &phoneBook, const string &name);
void modifyEntry(map<string, string> &phoneBook, const string &name, const string &newNumber);
void deleteEntry(map<string, string> &phoneBook, const string &name);
void displaySize(const map<string, string> &phoneBook);
void checkEmpty(const map<string, string> &phoneBook);

int main() {
	map<string, string> phoneBook;

	// Insert entries
	insertEntry(phoneBook, "Erick", "342-827-224");
	insertEntry(phoneBook, "Mwenda", "933-434-100");
	insertEntry(phoneBook, "Njagi", "445-722-433");

	// Display the whole Phone Book
	displayphoneBook(phoneBook);

	// Find entry
	findEntry(phoneBook, "Erick");

	// Modify existing entry
	modifyEntry(phoneBook, "Mwenda", "834-663-222");

	// Display Phone Book after modification
	displayphoneBook(phoneBook);

	// Delete entry
	deleteEntry(phoneBook, "Njagi");

	// Display the Phone Book after deletion
	displayphoneBook(phoneBook);

	// Display size and check if the phoneBook is empty
	displaySize(phoneBook);
	checkEmpty(phoneBook);

	// Clear the Phone Book and check again
	phoneBook.clear();
	checkEmpty(phoneBook);

	return 0;
}

// Insert an entry into the phoneBook
void insertEntry(map<string, string> &phoneBook, const string &name, const string &number) {
	phoneBook[name] = number; // Inserts or updates the entry
	cout << "Inserted " << name << " with number " << number << endl;
}

// Display all entries in the phoneBook
void displayphoneBook(const map<string, string> &phoneBook) {
	cout << "Phone Book Entries:" << endl;
	for (const auto &entry : phoneBook) {
		cout << entry.first << ": " << entry.second << endl;
	}
	cout << endl;
}

// Find and display an entry by name
void findEntry(const map<string, string> &phoneBook, const string &name)
{
	auto it = phoneBook.find(name); // Find the entry by name (key)
	if (it != phoneBook.end()) {
		cout << "Found: " << it->first << "'s number is " << it->second << endl;
	} else {
		cout << "Entry for " << name << " not found." << endl;
	}
}

// Modify an existing entry
void modifyEntry(map<string, string> &phoneBook, const string &name, const string &newNumber) {
	auto it = phoneBook.find(name);
	if (it != phoneBook.end()) {
		phoneBook[name] = newNumber; // Update the entry with the new number
		cout << "Modified " << name << "'s number to " << newNumber << endl;
	} else {
		cout << "Entry for " << name << " not found, cannot modify." << endl;
	}
}

// Delete an entry by name
void deleteEntry(map<string, string> &phoneBook, const string &name) {
	if (phoneBook.erase(name) > 0) {
		cout << "Deleted entry for " << name << endl;
	} else {
		cout << "Entry for " << name << " not found, cannot delete." << endl;
	}
}

// Display the size of the phoneBook
void displaySize(const map<string, string> &phoneBook) {
	cout << "Phone Book contains " << phoneBook.size() << " entries." << endl;
}

// Check if the phoneBook is empty
void checkEmpty(const map<string, string> &phoneBook) {
	if (phoneBook.empty()) {
		cout << "Phone Book is empty." << endl;
	} else {
		cout << "Phone Book is not empty." << endl;
	}
}