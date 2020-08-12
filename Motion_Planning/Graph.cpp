#include <stdio.h>
#include <iostream>
#include "Graph.hpp"
using namespace std;
using std::cout;
using std::cin;
using std::endl;


Node* Graph::insert(Node* head, int identifier, int givenWeight){
    //Create a new node and using the data provided in the params, attatch it to the head
    Node* nodeToInsert = new Node;
    nodeToInsert->number = identifier;
    nodeToInsert ->weight =  givenWeight;
    nodeToInsert->next = head;
    return nodeToInsert;
}

int Graph::getSize(){
    return size;
}

Graph::Graph(Edge listOfEdges[], int numEdges, int numVertices){
    //Initialize the adjacency list 
    head = new Node*[numVertices]();
    this->size = numVertices;

    //make each element in the adjacency list null as to fill them in later
    for(int i  = 0; i< numVertices; i++){
        head[i] = nullptr;
    }
            
    //For loop to fill in the adjacency lists
    for(unsigned i = 0; i<numEdges; i++){
        //get the value of previous node, the next node, and the weight between them
        int first_vertex = listOfEdges[i].firstNode;
        int last_vertex = listOfEdges[i].secondNode;
        int current_weight= listOfEdges[i].weight;

        //Insert the new node
        Node* addedNode = insert(head[first_vertex],last_vertex,current_weight);
        head[first_vertex] = addedNode;
        }
}



