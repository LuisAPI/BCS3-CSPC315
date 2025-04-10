#include <iostream>
#include <fstream>
using namespace std;

// Helper function to generate Graphviz DOT notation for recursive tree
void generateTreeGraph(int n, int level, int &nodeCounter, ofstream &file) {
    if (n <= 1) {
        file << "Node" << nodeCounter << " [label=\"" << n << "\"];\n";
        return;
    }

    int currentNode = nodeCounter;
    file << "Node" << currentNode << " [label=\"n = " << n << "\"];\n";

    // Left child (recursive call with n/2)
    nodeCounter++;
    file << "Node" << currentNode << " -> Node" << nodeCounter << ";\n";
    generateTreeGraph(n / 2, level + 1, nodeCounter, file);

    // Right child (another recursive call with n/2)
    nodeCounter++;
    file << "Node" << currentNode << " -> Node" << nodeCounter << ";\n";
    generateTreeGraph(n / 2, level + 1, nodeCounter, file);
}

// function to calculate the master method
double masterMethod (int a, int b, int n){
    if(n <= 1) return 1;
    // log_b(a)
    double log_b_a = log(a) / log(b);
    // work done outside recursion
    double f_n = n;


    // apply the master theorem case
    if(f_n == pow(n, log_b_a)){
        // case 2: T(n) = O(n log n)
        return n = log2(n);
    } else if (f_n < pow(n, log_b_a)){
        // case 1: T(n) = O(n^log_b a)
        return pow(n, log_b_a);
    } else {
        // case 3: T(n) = O(f(n))
        return f_n;
    }
}

int main(){
    int n = 16; // Example input
    ofstream file("recursive_tree.dot");

    // Start of DOT file for Graphviz
    file << "digraph RecursiveTree {\n";

    int nodeCounter = 0;
    generateTreeGraph(n, 0, nodeCounter, file);

    // End of DOT file
    file << "}\n";
    file.close();
    
    cout << "Graph of recursive tree has been generated as 'recursive_tree.dot'.\n";
    cout << "Use Graphviz (e.g., run 'dot -Tpng recursive_tree.dot -o recursive_tree.png') to generate the graph image.\n";

    return 0;
}