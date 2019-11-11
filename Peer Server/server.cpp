#include <iostream>
#include <fstream>
#include <string> 
#include <boost/asio.hpp>
#include <array>
using boost::asio::ip::tcp;

std::string getList(){
    std::ifstream myfile;
    myfile.open("list.txt");
    std::string data="",line;
    if(myfile.is_open()){
        while(getline(myfile,line)){
            data+="\n"+line;
        }
        myfile.close();
    }
    return data;
}

void addList(std::string data){
    std::ofstream myfile;
    myfile.open("list.txt");
    data = data+"\n";
    myfile<<data;
    myfile.close();
    return;
}


int main(){

    try{
        boost::asio::io_service service;

        tcp::acceptor acceptor(service, tcp::endpoint(tcp::v4(), 8000));
        while(true){
            boost::system::error_code ignored;
            tcp::socket socket(service);
            acceptor.accept(socket);
            std::string data =  getList();
            std::array<char, 256> inputBuffer;
            std::size_t inSize = socket.read_some(boost::asio::buffer(inputBuffer), ignored);
            std::string visitor(inputBuffer.data(), inputBuffer.data() + inSize);
            std::cout<<visitor<<std::endl;
            std::cout<<data<<std::endl;
            addList(socket.remote_endpoint().address().to_string());
            boost::asio::write(socket, boost::asio::buffer(data), ignored);
            socket.shutdown(tcp::socket::shutdown_both, ignored);
            socket.close();
        }
    }catch(std::exception& e){
        std::cerr << e.what() << std::endl;
    }

    return 0;
}