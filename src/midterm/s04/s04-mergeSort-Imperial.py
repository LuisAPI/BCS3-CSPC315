"""
''De La Salle University – Dasmariñas''  
''College of Information and Computer Studies''

''S-CSPC315 — Algorithms and Complexity''  
''6. '''Divide and Conquer Algorithms'''''

''Luis Anton P. Imperial''  
''BCS32''
"""

"""
# Merge Sort Program simulation

- Type: Dropbox
- Max score: 20
- Category: Enabling Asssessment
- Start: Sep 30, 7:00 am
- Due: Oct 2, 5:00 pm

1. Create a  mergesort program - divide and conquer design technique using any of your preferred programming language. NOTE : refer to Module for the sample algortihm
2. Run the program using this array with n=8 elements as input.
  - [8, 3, 2, 9, 7, 1, 5, 4]
3. Trace the program by printing or output the following elements in this order:  
  - [mceclip3.png]
4. Upload your program and the screenshot of your code and output of your program when run.
"""

from typing import List

node_counter: int = 0
edges: list = []

dot_file_name: str = "s04-mergeSort-Imperial-output-v6.dot"

def merge_sort_dot(
        arr: List[int],
        parent_node: int = None
        ) -> int:
    global node_counter
    current_node = node_counter
    node_counter += 1

    edges.append(f'    node{current_node} [label="{arr}"];')

    if parent_node is not None:
        edges.append(f'    node{parent_node} -> node{current_node};')

    if len(arr) > 1:
        mid: int = len(arr) // 2
        left_half: List[int] = arr[:mid]
        right_half: List[int] = arr[mid:]

        # Recursively sort both halves
        left_node: int = merge_sort_dot(left_half, current_node)
        right_node: int = merge_sort_dot(right_half, current_node)

        # Merging the sorted halves
        i = j = k = 0

        # Create a copy of the current array
        merge_process: List[int] = arr[:]

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                merge_process[k] = left_half[i]
                i += 1
            else:
                merge_process[k] = right_half[j]
                j += 1
            k += 1

        # Check for any remaining elements
        while i < len(left_half):
            merge_process[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            merge_process[k] = right_half[j]
            j += 1
            k += 1

        # Create a new node for the merged result
        merge_node = node_counter
        node_counter += 1

        edges.append(f'    node{merge_node} [label="{merge_process}"];')
        edges.append(f'    node{left_node} -> node{merge_node};')
        edges.append(f'    node{right_node} -> node{merge_node};')

        # Copy back the merged result into the original array
        arr[:] = merge_process


    return current_node

def add_final_sorted_array(arr: List[int], root_node: int) -> None:
    global node_counter
    final_node: int = node_counter
    node_counter += 1

    edges.append(f'    node{final_node} [label="Final sorted: {arr}"];')
    edges.append(f'    node{root_node} -> node{final_node};')


def write_dot_file(filename: str) -> None:
    with open(filename, 'w') as f:
        f.write("digraph MergeSort {\n")
        f.write("    node [shape=box];\n")
        f.write("\n".join(edges))
        f.write("\n}")


def main() -> None:
    global node_counter, edges

    # Example list provided by professor: 8,3,2,9,7,1,5,4
    input_str: str = input("Enter a list, separated by commas. (Example: 2,7,4,6)\n> ")

    # Create new variable to list each input element
    int_array: List[int] = list(map(int, input_str.split(',')))

    node_counter = 0
    edges = []
    
    root_node = merge_sort_dot(int_array);
    add_final_sorted_array(int_array, root_node)

    print(f"Sorted array:", int_array)

    write_dot_file(dot_file_name)
    print("DOT file generated:", dot_file_name)

main();