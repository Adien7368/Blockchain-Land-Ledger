main: main.o
	g++ -o main main.o -lboost_system -lboost_thread -lpthread
main.o: main.cpp
	g++ -c main.cpp
clean: 
	rm -f *.o main