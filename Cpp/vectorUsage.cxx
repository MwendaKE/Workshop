#include <iostream>
#include <vector>
using namespace std;


// a vector is a Dynamic array that can grow in size.
// vector operations

void vectorDisplay(const vector<int>& vec) {
    cout << "Current List: ";
    for (const auto& num : vec) {
        cout << num << " ";
    }
    cout << endl << endl;
}

int main() {
    vector<int> numbers;  // Create an empty vector of integers

    // 1. Adding elements using push_back and emplace_back
    numbers.push_back(110);
    numbers.push_back(120);
    numbers.emplace_back(130);  // More efficient for complex objects

    cout << "After adding elements:" << endl;
    vectorDisplay(numbers);

    // 2. Accessing vector elements
    cout << "1st element: " << numbers[0] << endl; // using []
    cout << "2nd element: " << numbers.at(1) << endl; // Using .at()

    // 3. Inserting element at beginning
    numbers.insert(numbers.begin(), 5);
    cout << "After inserting 5 at beginning:" << endl;
    vectorDisplay(numbers);

    // 4. Removing an element from the end
    numbers.pop_back();
    cout << "After popping the last element:" << endl;
    vectorDisplay(numbers);

    // 5. Removing an element from a specific position
    numbers.erase(numbers.begin() + 1);  // Erase the second element
    cout << "After erasing the second element:" << endl;
    vectorDisplay(numbers);

    // 6. Resizing the vector
    numbers.resize(5, 300);  // Resize to 5 elements, new elements initialized to 300
    cout << "After resizing to 5 elements (new ones as 300):" << endl;
    vectorDisplay(numbers);

    // 7. Checking properties
    cout << "Vector Size: " << numbers.size() << endl;
    cout << "Vector Capacity: " << numbers.capacity() << endl;
    cout << "Vector empty? " << (numbers.empty() ? "Yes" : "No") << endl;

    // 8. Swapping two vectors
    vector<int> newNumbers = {1200, 1300, 1400};
    numbers.swap(newNumbers);
    cout << "After swapping with another vector:" << endl;
    cout << "oldNumbers: "; vectorDisplay(numbers);
    cout << "newNumbers: "; vectorDisplay(newNumbers);

    // 9. Clearing the vector
    numbers.clear();
    cout << "After clearing the numbers vector: ";
    vectorDisplay(numbers);
    cout << "Vector size after clear: " << numbers.size() << endl;

    return 0;
}