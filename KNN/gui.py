#Relevant imports
import pandas as pd,csv, tkinter as tk
from tkinter import *
from tkinter import filedialog,Text
from mysql.connector import MySQLConnection, Error
from KNN import *

'''
What is this?
This is a a Python program that illustrates the K nearest neighbors progam
using a csv to make recommendation on the best matches.
This is illustrated using a GUI that showcases to the use the best neighbors for their
selected data point.
The only caveat to this is that if the CSV is formatted in a different way, this will fail
'''
#initialize the gui
root = tk.Tk()

#create the canvas
canvas = tk.Canvas(root, height = 500,width = 500, bg='#193F6D')
canvas.pack()

#Set background
frame = tk.Frame(root, bg ="white")
frame.place(relwidth =0.6,relheight =.6,relx=.2,rely =0.05)

#define the submit label for the csv
entry = tk.Entry(root)
canvas.create_window(150,375,window=entry)

entry2 = tk.Entry(root)
canvas.create_window(375,375, window=entry2)

#Instructions
label = tk.Label(root,text = "Enter a file in a UNIX format")
label.config(font=('helvetica', 10))
canvas.create_window(150, 350, window=label)

#Instructions for label 2
label2 = tk.Label(root,text = "Enter neighbors and object as k,n")
label2.config(font=('helvetica', 10))
canvas.create_window(375, 350, window=label2)

#create the database in question
def dumpToDataBase(csv_name,selection,neighbors,results):
    query = "INSERT INTO data(csv_name,selection,neighbors,results)"\
            "VALUES(%s,%s,%s,%s)"
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()


#Driver class for the GUI
def topNRecs():
    #Get Entries
    csv_file_name = entry.get()
    string = entry2.get()
    
    #User selections
    numNeighbors = int(string[0])
    selectedPoint = int(string[2])
    
    #Call KNN class and get the neighbors
    knnClient = KNN(csv_file_name,selectedPoint,numNeighbors)
    list_of_Neighbors = knnClient.driver()
    
    #Catch bad input from a bad csv
    if list_of_Neighbors is None:
        out = "Warning: No Neighbors. Edit the CSV or try again."
    else:
        out = "Results are in the txt file"
    
    #Dump the results to a file 
    with open('output.txt','w') as f:
        for neighbor in list_of_Neighbors:
            f.write("%s\n" % str(neighbor))
    
    #Transform the csv into a dict of dicts
    reader = csv.DictReader(open(csv_file_name))
    dict_list = []
    for line in reader:
        dict_list.append(line)
    
    #Store the csv in a txt file with appropriate headers for better analysis
    with open('dict.txt','w') as d:
        for dictonary in dict_list:
            d.write("%s\n" % str(dictonary))
     
    
    #print(dict_list)
    list_of_Neighbors= [[str(str(j)) for j in i] for i in list_of_Neighbors]
    res = [''.join(ele) for ele in list_of_Neighbors] 

    
     #Output windows
    title = tk.Label(root,text = out,font=('helvetica', 10))
    canvas.create_window(220,80,window=title)
    
    #More output windows suggesting the user try another csv file
    ans = tk.Label(root,text ="Try another txt file below!" ,font=('helvetica', 15))
    canvas.create_window(250,300,window=ans)
    

#Create the button to run the topNRecs Function
button1 = tk.Button(text ="Get Neighbors", command = topNRecs, bg="brown",fg="white",font=('helvetica', 15, 'bold'))
canvas.create_window(247.5, 425, window=button1)

#Run the GUI by calling the mainloop
root.mainloop()
