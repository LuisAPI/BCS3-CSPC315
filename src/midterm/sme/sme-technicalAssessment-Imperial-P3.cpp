// Luis Anton P. Imperial
// BCS32

// S-CSPC315 — Algorithms and Complexity
// Midterm Technical Assessment

#include <iostream>
using namespace std;

// Recursive function to solve Tower of Hanoi
void towerOfHanoi(int N, char source, char destination, char auxiliary) {
    if (N == 1) {
        // Base case: Move one disc from source to destination
        cout << "Move disc 1 from " << source << " to " << destination << endl;
        return;
    }
    // Move N-1 discs from source to auxiliary using destination as buffer
    towerOfHanoi(N - 1, source, auxiliary, destination);
    
    // Move the Nth disc from source to destination
    cout << "Move disc " << N << " from " << source << " to " << destination << endl;
    
    // Move the N-1 discs from auxiliary to destination using source as buffer
    towerOfHanoi(N - 1, auxiliary, destination, source);
}

// Function to calculate the total number of moves required
int totalMoves(int N) {
    return (1 << N) - 1; // 2^N - 1
}

int main() {
    int N;
    cout << "Enter the number of discs: ";
    cin >> N;

    cout << "\nSequence of steps to solve Tower of Hanoi:\n";
    towerOfHanoi(N, 'A', 'C', 'B'); // A is the source, C is the destination, B is the auxiliary

    int moves = totalMoves(N);
    cout << "\nTotal number of moves required: " << moves << endl;
    cout << "Time Complexity: O(2^N - 1)\n";

    return 0;
}
