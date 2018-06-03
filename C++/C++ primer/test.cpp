#include <iostream>
#include<vector>
using std::endl;
using std::cin;
using std::cout;
using std::string;
using std::vector;
using std::toupper;

int main()
{
    string word;
    vector<string> text;
    while (cin>>word){
        for (auto &c:word)
            c = toupper(c);
        text.push_back(word);
    }
    for (auto a:text){
        cout<<a<<endl;
    }
    return 0;
}