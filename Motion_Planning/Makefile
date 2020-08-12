CXX = g++
CXXFLAGS = -c 

search: search.o Graph.o
	$(CXX) search.o Graph.o -o output

search.o: search.cpp Graph.cpp Graph.hpp
	g++ -c search.cpp Graph.cpp

clean:
	rm *.o  output