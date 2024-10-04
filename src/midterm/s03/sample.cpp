/*
    Factorial Computation
        - a factorial number of n is the product of all positive integers less than or equal to (n-1)

        n! = n x (n-1)!

        1! = 1
*/

#include <iostream>
using namespace std;


//recursive function to calculate factorial
int factorial(int n){
    //base case: if n is 0 or 1, return 1
    if(n <= 1)
        return 1;
    else
        return n * factorial(n-1);
}

//main
int main(){
    int number;
    cout << "Enter a number : ";
    cin >> number;

    //call the recursive function
    cout << "The factorial of " << number << " is: " << factorial(number) << endl;

    return 0;
}