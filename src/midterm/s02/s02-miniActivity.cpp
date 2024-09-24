/*
De La Salle University – Dasmariñas
College of Information and Computer Studies
Computer Science Department

S–CSPC315: Algorithms and Complexity
240909 - Mini Activity
Monday, September 9, 2024

Mini Activity
 Compute the time complexity of the given numbers, identify the correct complexity and show your solutions and answer. Failure to will not gain any mark on this activity. Screen shot your solution and answer, box your answer.

Luis Anton P. Imperial
BCS32

*/

#include <iostream>
using namespace std;

// 1.
int getFirstElement(int arr[], int size) {
     return arr[0];     // --> O(1)
 }
// Complexity: O(1)

// 2.
int binarySearch(int arr[], int l, int r, int x) {
    while (l <= r) {
        int mid = l + (r - l) / 2;
            // (n/2)(n/4)
            // --> log[sub(2)](n) = O(log n)
        if (arr[mid] == x) return mid;
            // O(1)
        if (arr[mid] < x) l = mid + 1;
            // O(1)
        else r = mid - 1;
            // O(1)
    }
    return -1;
}
// Complexity: O(log n)

// 3.
int findMax(int arr[], int size) {
    int max = arr[0];                   // O(1)
    for (int i = 1; i < size; i++) {    // O(n)
        if (arr[i] > max) max = arr[i]; // O(1)
    }
    return max;
}
// Complexity: O(n)

// 4.
void merge(int arr[], int l, int m, int r) {
     // Merge function for merge sort
     // Details omitted for brevity
 }
 void mergeSort(int arr[], int l, int r) {
     if (l < r) {
         int m = l + (r - l) / 2;
         // O(1)
         mergeSort(arr, l, m);
         mergeSort(arr, m + 1, r);
         // O(log n)
         merge(arr, l, m, r);
         // O(n)
     }
 }
// Complexity:
//      O(log n) * O(n)
//    = O(n log n)

// 5.
void bubbleSort(int arr[], int size) {
    for (int i = 0; i < size - 1; i++) {
                        // --> O(n^2) * O(n) = O(n^3)
        for (int j = 0; j < size - i - 1; j++) {
                        // --> O(n) * O(n) = O(n^2)
            if (arr[j] > arr[j + 1]) {
                        // --> O(n)
                swap(arr[j], arr[j + 1]);
                        // --> O(1)
            }
        }
    }
}
// Complexity: O(n^3)

// 6.
void printAllTriplets(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        //  O(n^2) * O(n) --> O(n^3)
        for (int j = i + 1; j < size; j++) {
            // O(n) * O(n) --> O(n^2)
            for (int k = j + 1; k < size; k++) {
                // O(n)
                cout << arr[i] << ", " << arr[j] << ", " << arr[k] << endl;
            }
        }
    }
}
// Complexity: O(n^2)

// 7.
void permute(string str, int l, int r) {
    if (l == r) {               // --> O(1)
         cout << str << endl;
         } else {
         for (int i = l; i <= r; i++) {
            // --> O(n)
             swap(str[l], str[i]); // --> O(1)
             permute(str, l + 1, r);
                // --> O(n!)
             swap(str[l], str[i]); // Backtrack
                // --> O(1)
             }
        }
}
// Complexity:
// O(1) * O(n) * O(n!) * O(1)
// = O(n * n!)

// 8.
int fib(int n) {
     if (n <= 1) return n;
     // --> O(1)
     return fib(n - 1) + fib(n - 2);
     // --> O(n) + O(n) = O(2^n)

}
// Complexity:
// = O(2^n)

// 9.
void heapify(int arr[], int n, int i) {// Heapify function for heap sort// Details omitted for brevity}

void heapSort(int arr[], int n) {
    for (int i = n / 2 - 1; i >= 0; i--)
        // --> O(n)
        heapify(arr, n, i);     // --> O(log n)
    for (int i = n - 1; i >= 0; i--) {
        // --> O(n)
        swap(arr[0], arr[i]);   // --> O(1)
        heapify(arr, i, 0);     // --> O(log n)
    }
}
// Complexity:
// O(n) * O(log n)
// = O(n log n)

// 10.
    bool hasDuplicate(std::vector<int>& nums){
        std::unordered_set<int> seen;
    for (int num : nums) {
        // --> O(n)
        if (seen.find(num) != seen.end()) {
            // --> O(1)
            return true; // Duplicate found}
        seen.insert(num);}
    return false; // No duplicates
    }
}
// Complexity: O(n)

// 11.
    int countSetBits(int n) {
     if (n == 0) return 0; // --> O(1)
     return (n & 1) + countSetBits(n >> 1);
     // --> O(1) + O(log n)

}
// Complexity: O(log n)


// 12.
    void printPairs(int arr[], int size) {
    for (int i = 0; i < size; i++) {
                        // --> O(n) * O(n) = O(n^2)
        for (int j = i + 1; j < size; j++) {
                        // --> O(n)
            cout << "(" << arr[i] << ", " << arr[j] << ")" << endl;}}
                        // --> O(1)

}
// Complexity: O(n^2)

// 13.
    bool containsSubstring(const string& str, const string& pattern) {
     size_t pos = str.find(pattern);    // O(n)
    return pos != string::npos;         // O(1)

}
// Complexity: O(n)

// 14.
    void generateSubarrays(int arr[], int size) {
    for (int start = 0; start < size; start++) {
    // --> O(n²) * O(n) = O(n³)
        for (int end = start; end < size; end++) {
        // --> O(n) * O(n) = O(n²)
            for (int i = start; i <= end; i++) {
            // --> O(n)
                cout << arr[i] << " ";
                // --> O(1)
            }
            cout << endl;}}

}
// Complexity: O(n³)

// 15.
    void reverseA