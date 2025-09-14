// MwendaKE Programs
// https://github.com/MwendaKE
// Email: erickmwenda256@gmail.com
// Phone: +254 702 623 729
// Phone: +254 799 678 038

#include <iostream>
#include <cmath>

using namespace std;

struct Answer {
	double root1;
	double root2;
};

void printBarner();

Answer solveQuadraticEqn(int a, int b, int c);


int main() {
	printBarner();
	
	int a, b, c;
	Answer answer;
	
	while (true) {
	
	    cout << " > QUADRATIC EQUATION SOLVER " << endl << endl;
	
	    cout << " > Enter Value of a: ";
	    cin >> a;
	
	    cout << " > Enter Value of b: ";
	    cin >> b;
	
	    cout << " > Enter Value of c: ";
	    cin >> c;
	
	    cout << endl;
	
	    answer = solveQuadraticEqn(a, b, c);
	
        cout << "  Roots: " << answer.root1 << " and " << answer.root2 << endl << endl;
	    
	}
}


Answer solveQuadraticEqn(int a, int b, int c) {
	double discrim = pow(b, 2) - 4 * a * c;
    
    double root1 = (-b - sqrt(discrim)) / (2 * a);
    double root2 = (-b + sqrt(discrim)) / (2 * a);
    
    Answer answer;
    answer.root1 = root1;
    answer.root2 = root2;
    
    return answer;
    
}

void printBarner() {
	cout << " ---------------------" << endl;
	cout << " |  MwendaKe Programs |" << endl;
	cout << " | mwendake@gmail.com | " << endl;
	cout << " |  +254 799 678 038  | " << endl;
	cout << " ---------------------" << endl;
	
	cout << endl;
	
	return;
}