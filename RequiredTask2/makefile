all: CircularArray

CircularArray: CircularArray.o
	g++ -Wall -std=c++11 CircularArray.o -o CircularArray

CircularArray.o: CircularArray.cpp
	g++ -c CircularArray.cpp

clean:
	rm -rf *.o CircularArray
