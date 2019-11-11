server: server.o
	g++ -o server server.o -lboost_system -lboost_thread -lpthread
server.o: server.cpp
	g++ -c server.cpp
run: server
	./server
testServer: testServer.o
	g++ -o testServer testServer.o -lboost_system -lboost_thread -lpthread
testServer.o: testServer.cpp
	g++ -c testServer.cpp
clean: 
	rm -f *.o server testServer