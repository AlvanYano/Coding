// A C/C++ program for splitting a string
// using strtok()
#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

void tokenize(string s, string del = "")
{
    int start, end = -1*del.size();

    do {
        start = end + del.size();
        cout << start << endl;

        end = s.find("", start);
        cout << end << endl;

        cout << s.substr(start, end - start) << endl;
    } while (end != -1);
}

int main()
{
    char str[] = "Geeks-for---Geeks--";

    // Returns first token 
    char *token = strtok(str, "-");
  
    // Keep printing tokens while one of the
    // delimiters present in str[].
    while (token != NULL)
    {
        printf("%s\n", token);
        token = strtok(NULL, "-");
    }

    string a = "How$%do$%you$%do$%!$";
    tokenize(a);
    cout << endl;


    string coba_1 = "ikan";

    string hasil =  coba_1.substr(2, -10);

    cout << hasil << endl;

    string i = " ";

    cout << i.size() << endl;

    return 0;


}