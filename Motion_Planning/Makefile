#set up the flags needed
CXX = g++
CXXFLAGS = -c 

#Dependencies for the output file
search: search_driver.o Graph.o
	$(CXX) search_driver.o Graph.o -o output

#Dependencies for the driver method
search.o: search_driver.cpp Graph.cpp Graph.hpp
	g++ -c search_driver.cpp Graph.cpp

#Clean
clean:
	rm *.o  output