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