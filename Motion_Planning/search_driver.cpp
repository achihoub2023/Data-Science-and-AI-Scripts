#include "Graph.hpp"
#include "search.hpp"
#include "time.h"
#include <stdio.h>
#include <iostream>
using namespace std;
using std::cout;
using std::cin;
using std::endl;


// print all adjacent vertices of given vertex
void Print_Graph(Node* ptr,int i)
{
    while (ptr != nullptr) {
        cout << "(" << i << ", " << ptr->number
            << ", " << ptr->weight<< ") ";
        ptr = ptr->next;
    }
    cout << endl;
}

int main(){
     // graph edges array.
    Edge edges[] = {
        // (x, y, w) -> edge from x to y with weight w
        {0,1,2},{0,2,4},{1,4,3},{2,3,2},{3,1,4},{4,3,3}
    };
    int N = 6;      // Number of vertices in the graph
    // calculate number of edges
    int n = sizeof(edges)/sizeof(edges[0]);
    // construct graph
    Graph diagraph(edges, n, N);
    // print adjacency list representation of graph
    cout<<"Graph adjacency list "<<endl<<"(start_vertex, end_vertex, weight):"<<endl;
    for (int i = 0; i < N; i++)
    {
        // display adjacent vertices of vertex i
        Print_Graph(diagraph.head[i], i);
    }
    return 0;
}