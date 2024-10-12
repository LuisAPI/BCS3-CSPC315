// Luis Anton P. Imperial
// BCS32

// S-CSPC315 — Algorithms and Complexity
// Midterm Technical Assessment

#include <iostream>
#include <vector>
#include <chrono>
#include <random>
using namespace std;
using namespace chrono;

// Bubble Sort Implementation
void bubbleSort(vector<int>& arr) {
    int N = arr.size();
    for (int i = 0; i < N - 1; i++) {
        for (int j = 0; j < N - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
            }
        }
    }
}

// Merge Sort Helper Functions
void merge(vector<int>& arr, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;
    vector<int> L(n1), R(n2);
    
    for (int i = 0; i < n1; i++) L[i] = arr[left + i];
    for (int j = 0; j < n2; j++) R[j] = arr[mid + 1 + j];
    
    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) arr[k++] = L[i++];
        else arr[k++] = R[j++];
    }
    
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];
}

void mergeSort(vector<int>& arr, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}

// Function to print array
void printArray(const vector<int>& arr) {
    for (int i : arr) cout << i << " ";
    cout << endl;
}

// Function to generate random numbers
vector<int> generateRandomNumbers(int size) {
    vector<int> randomNumbers(size);
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(1, 1000);

    for (int i = 0; i < size; ++i) {
        randomNumbers[i] = dis(gen);
    }
    return randomNumbers;
}

int main() {
    int dataSize = 10000;
    vector<int> deliveryTimes = generateRandomNumbers(dataSize);
    vector<int> bubbleSorted = deliveryTimes;
    vector<int> mergeSorted = deliveryTimes;

    // Bubble Sort
    auto startBubble = high_resolution_clock::now();
    bubbleSort(bubbleSorted);
    auto endBubble = high_resolution_clock::now();
    auto bubbleSortTime = duration_cast<microseconds>(endBubble - startBubble).count();

    // Merge Sort
    auto startMerge = high_resolution_clock::now();
    mergeSort(mergeSorted, 0, mergeSorted.size() - 1);
    auto endMerge = high_resolution_clock::now();
    auto mergeSortTime = duration_cast<microseconds>(endMerge - startMerge).count();

    // Output Results
    cout << "Bubble Sort Time: " << bubbleSortTime << " microseconds" << endl;
    cout << "Merge Sort Time: " << mergeSortTime << " microseconds" << endl;

    // Complexity Analysis
    cout << "\nTime Complexity Analysis:\n";
    cout << "Bubble Sort: O(N^2) - Inefficient for large inputs due to quadratic growth in operations.\n";
    cout << "Merge Sort: O(N log N) - More efficient for larger inputs due to logarithmic division of the array.\n";

    return 0;
}

