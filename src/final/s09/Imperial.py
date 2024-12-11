# Imperial.py

# De La Salle University – Dasmariñas
# S–CSPC315 — Algorithms & Complexity

# Luis Anton P. Imperial
# BCS32

# Wednesday, December 4, 2024
# Short quiz - Fibonacci

"""
## Instructions:

1. ### Write a Program:
    - Use Dynamic Programming to calculate Fibonacci numbers efficiently.
    - The program should prompt the user to input nn (number of Fibonacci terms to display).
    - It should then output the Fibonacci sequence up to the nn-th term.

2. ### Requirements:
    - Include a function or method that computes Fibonacci numbers using a bottom-up approach.
    - The program should dynamically compute values and avoid redundant calculations.
    - The output should display the sequence cleanly.

3. ### Example Input/Output:
    - Input: Enter the number of Fibonacci terms to display: 10
    - Output: 0 1 1 2 3 5 8 13 21 34

4. ### Steps to Code:
    - Ask the user to input the number nn (e.g., "Enter the number of Fibonacci terms to display:").
    - Initialize a structure (e.g., array or list) to store Fibonacci numbers.
    - Set the base cases F(0)=0F(0)=0 and F(1)=1F(1)=1.
    - Use a loop to compute Fibonacci numbers dynamically from F(2)F(2) to F(n−1)F(n−1).
    - Display the sequence.

5. ### Take note:
    - Submit a screenshot showing your program's output with the sequence.
    - Include the source code file in the format of your chosen programming language:
        - For example: Surname.py for Python, Surname.cpp for C++, Surname.java for Java, etc.
"""

class Fibonacci:
    def __init__(self):
        self.fib_sequence = [];
        self.fib_sequence_completed = 0;
        self.fib_sum = 0;
        self.fib_input = None;

    def check_if_positive(self):
        return self.fib_input > 0;

    def reject_input(self, reason):
        if reason.lower() == "negative":
            print("Number for Fibonacci sequence must be a positive integer.")

    def square(self, factor):
        return factor ** 2;

    def generate_fibonacci_sequence(self):
        if self.fib_input <= 1:
            print("Fibonacci sequence:", [0, 1][:self.fib_input])
            return

        self.fib_sequence.append(0);
        self.fib_sequence_completed += 1;
        self.fib_sequence.append(1);
        self.fib_sequence_completed += 1;
        print(f"Fibonacci number(1): 0, Square: 0")

        for seq_count in range(2, self.fib_input + 1):
            fib_sequence_nextnum = self.fib_sequence[seq_count - 1] + self.fib_sequence[seq_count - 2]
            self.fib_sequence.append(fib_sequence_nextnum);
            seq_count_sq = self.square(self.fib_sequence[seq_count - 1]);
            print(f"Fibonacci number({seq_count}): {self.fib_sequence[seq_count - 1]}, Square: {seq_count_sq}")
            self.fib_sequence_completed += 1
        print("\nThe next number is:", self.fib_sequence[self.fib_sequence_completed - 1])

    def display_menu(self):
        print("Fibonacci Sequence Script —")
        print("Generate a Fibonacci sequence based on the user input, and know their squares.", end="\n\n")

        self.fib_input = int(input("Enter the number for Fibonacci sequence:\n"))
        print("")

        check_input = self.check_if_positive();

        if check_input is False:
            self.reject_input("negative");
        else:
            self.generate_fibonacci_sequence();

        print("")
        print("Fibonacci sequence:", self.fib_sequence)

def main():
    fibogen = Fibonacci();
    fibogen.display_menu();

if __name__ == "__main__":
    main();
