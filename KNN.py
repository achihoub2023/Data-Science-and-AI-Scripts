
import math
from math import sqrt
import pandas as pd, numpy as np,csv
#TODO: Normalization class? https://stackoverflow.com/questions/57984070/python-normalise-floats-in-a-list-of-lists-to-range-from-0-0-smallest-to-1-0
#Change the sort type to Heapsort to get klogn efficency
'''
Important notes here:
This is the main KNN class comprising of the following function:
_______________________________________________________________________
1. Shortest distance 
    -params: row1,row2 (two lists)
    -return: float list distance
    - calculates the euclidean distance between a point and all the elements
2. Mergesort
    -params: arr, key (list and lambda function)
    -return arr
    - classic mergesort algorithm to sort the list by distances
    
3. Get Neighbors
    - params: training_data, train_row,num_neighbors (csv file, specific int to test against, number of neighbors to be added)
    -return: neighbors (list of rows that meet qualifications)
    - finds k neighbors closest to the data point in question
4. Driver
    - runs the class as a test client, output is piped to the GUI in this case
    
5. KNN constructor
    - initializes the class with param of the filename on UNIX format, n = the row desired, and k = number of neighbors to find
'''
class KNN:
    def __init__(self,dataset,n,k):
        #default
        super().__init__()
        #process the csv as to remove any categorical labels, etc.
        self.dataset = list(csv.reader(open(dataset)))
        self.dataset.pop(0)
        for row in self.dataset:
            del row[0]
        self.dataset= [[float(float(j)) for j in i] for i in self.dataset]
        #print(self.dataset)
        self.k=k
        self.n =n
        
    # calculate the Euclidean distance, uses the math class in python
    def shortestDistance(self,row1, row2):
        distance = 0.0
        for i in range(len(row1)-1):
            distance += math.pow((row1[i] - row2[i]),2)
        return math.sqrt(distance)


    #test comment
    #perform merge sort here as it is the best sorting algorithm
    def mergeSort(self,arr, key = lambda x:x): 
        if len(arr) <2:
            return arr
        
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
        self.mergeSort(L,key=lambda x: x[1]) # Sorting the first half 
        self.mergeSort(R,key=lambda x: x[1]) # Sorting the second half 
    
        i = 0
        j = 0
        k = 0
            
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if key(L[i]) <key(R[j]): 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
            
        # Checking if any elements were left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
            
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1  
    
    # Locate the most similar neighbors by calling the shortest distance function
    def get_neighbors(self,train, test_row, k):
        distances = list()
        labels = train[1]
        del train[1]
        
        #Iterate over the training rows 
        for train_row in train:
            distance = self.shortestDistance(test_row, train_row)
            distances.append((train_row,distance))
        #Call mergesort to sort the distances by most similar, etc.
        sortedDistances = self.mergeSort(distances,key=lambda x: x[1])
        neighbors = list()
        
        #Append the k most similar neighbors
        for i in range(k):
            neighbors.append(distances[i][0])         
        return neighbors

    def driver(self):
        # Tests distance function
        neighbors = self.get_neighbors(self.dataset, self.dataset[self.n], self.k)

        #Return the neighbors
        return neighbors