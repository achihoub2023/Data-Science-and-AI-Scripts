#include <stdio.h>
#include <iostream>
using namespace std;
using std::cout;
using std::cin;
using std::endl;

// Note, implementation is of a weighted, directed graph

//Basic node in the graph with its weight, its number, and the next node
struct Node{
    int number;
    int weight;
    Node* next;
};

//Edges link the nodes together.
struct Edge{
    int firstNode;
    int secondNode;
    int weight;
};


class Graph{
    
    //TODO add the constructor to read a txt file with edges
    public:













};





int main(){
    int dimA,dimB;
    cout << "Enter dimA: ";
    cin >> dimA;
    cout<<"Enter dimB: ";
    cin >> dimB;

    
    return 0;
}