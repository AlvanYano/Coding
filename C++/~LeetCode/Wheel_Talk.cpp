#include <iostream>
#include <vector>
#include <string>

#ifdef on
std::vector <std::string> input_str = {"saya"};

std::vector <std::string> add;

int main(){
    std::cout << input_str[0][0] << std::endl;


}

#endif

#include <iostream>
#include <string>
using namespace std;

string input_user;
string hasil;

int main(){
  getline(cin, input_user);

  cout << input_user << endl;

  for (int i = 0;i < input_user.size();i++){
    if(input_user[i] == 'u' or input_user[i] == 'e' ){
      cout << input_user[i] << input_user[i];
    } else if (input_user[i] == 'a' or input_user[i] == 'i' or input_user[i] == 'o'){
      cout << input_user[i];
    }
  }


}