struct Node{
    int number;
    int weight;
    Node* next;
};

//Edges link the nodes together. Implemented as a struct to take advantage of pass by value
struct Edge{
    int firstNode;
    int secondNode;
    int weight;
};

class Graph{
    private:
        int size;
        
        Node* insert(Node* head, int identifier, int givenWeight);
        int getSize();
    public:
        Node **head;
        Graph(Edge listOfEdges[], int numEdges, int numVertices);

};