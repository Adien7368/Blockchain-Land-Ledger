main: main.o
	g++ -o main main.o -lboost_system -lboost_thread -lpthread
main.o: main.cpp
	g++ -c main.cpp
run: main
	./main
clean: 
	rm -f *.o main