#set up the flags needed
CXX = g++
CXXFLAGS = -c 

#Dependencies for the output file
search_driver: search_driver.o Graph.o A*.o Djikstra.o
	$(CXX) search_driver.o Graph.o -o output

#Dependencies for the driver method
search_driver.o: search_driver.cpp Graph.cpp Graph.hpp A*.cpp Djikstra.cpp search.hpp
	g++ -c search_driver.cpp Graph.cpp

#Clean
clean:
	rm *.o  output