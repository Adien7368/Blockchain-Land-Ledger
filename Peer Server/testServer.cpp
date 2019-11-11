#include <iostream>
#include <array> 
#include <boost/asio.hpp>
#include <boost/array.hpp>
#include <string>

using boost::asio::ip::tcp;

int main(){

    boost::asio::io_service service;
    tcp::resolver resolver(service);
    tcp::resolver::query query("127.0.0.1","8000");
    tcp::resolver::iterator endpointIterated = resolver.resolve(query);
    tcp::socket socket(service);
    boost::asio::connect(socket, endpointIterated);
    boost::system::error_code error;
    std::string temp = "getData";
    boost::asio::write(socket, boost::asio::buffer(temp), error);

    std::array<char, 256> inputBuffer;
    std::size_t rsize = socket.read_some(boost::asio::buffer(inputBuffer), error);

    std::cout<< std::string(inputBuffer.data(), inputBuffer.data()+rsize)<<std::endl;

}