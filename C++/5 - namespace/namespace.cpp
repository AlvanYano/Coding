#include <iostream>


namespace mahasiswa {
    std::string nama = "alvan";

    void ipk_now(){
        std::cout << "IPK saya saat ini adalah ..." << std::endl;
    }
}

int main(){

    std::cout << mahasiswa::nama << std::endl;


}