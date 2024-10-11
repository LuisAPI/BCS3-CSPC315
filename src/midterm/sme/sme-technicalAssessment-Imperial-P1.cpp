// Luis Anton P. Imperial
// BCS32

// S-CSPC315 — Algorithms and Complexity
// Midterm Technical Assessment

#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

// Function to calculate distance between two points
double calculateDistance(pair<int, int> p1, pair<int, int> p2) {
    return sqrt(pow(p2.first - p1.first, 2) + pow(p2.second - p1.second, 2));
}

// Function to compute total distance for N points
double totalDistance(const vector<pair<int, int>>& points) {
    double totalDist = 0.0;
    for (size_t i = 0; i < points.size() - 1; i++) {
        totalDist += calculateDistance(points[i], points[i + 1]);
    }
    return totalDist;
}

// Function to compute sum of first N natural numbers
int sumOfNaturalNumbers(int N) {
    return (N * (N + 1)) / 2;
}

int main() {
    // Input: List of N delivery points
    vector<pair<int, int>> points = {{1, 1}, {4, 5}, {9, 6}, {12, 8}};
    int N = points.size();

    // Calculate total distance
    double distance = totalDistance(points);
    cout << "Total Distance: " << distance << endl;

    // Calculate sum of first N natural numbers
    int sum = sumOfNaturalNumbers(N);
    cout << "Sum of first " << N << " natural numbers: " << sum << endl;

    return 0;
}
