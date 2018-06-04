#include<iostream>
using std::endl;
using std::cin;
using std::cout;
using std::string;

int main()
{/*
    string str("some string");

    for (auto c:str){
        cout<< c <<endl;
    }*/
/*
    string s = "hello world!!!";
    decltype(s.size()) punct_cnt = 0;
    for (auto c:s){
        if (ispunct(c)){
            ++punct_cnt;
        }
    }
    cout<<punct_cnt<<"puntuation char in"<<s<<endl;
    */
    
    /*
    string s("Hello World!!!");
    for (auto &c:s){
        c = toupper(c);
    }
    cout<<s<<endl;
    */
/*
    string s("Hello World!!!");
    if(!s.empty())
        cout  <<s[0]<<endl;
  */

/*
    string s("hello World!!!");
    if (!s.empty())
        s[0] = toupper(s[0]);
    cout<<s<<endl;
  */

 /*
    string s("Hello World!!!");
    for(decltype(s.size()) index = 0;
        index != s.size() && !isspace(s[index]);++index)
        s[index] = toupper(s[index]);
    cout <<s<<endl;
    */

    const string hexdigits = "0123456789ABCDEF";
    cout <<"Enter a series of numbers between 0 and 15"
        <<" separated by spaces. HIT ENTER when finished:"<<endl;
    string result;
    string::size_type n;
    while(cin>>n)
        if (n<hexdigits.size())
            result += hexdigits[n];
    cout << "your hex number is "<< result<<endl;
    return 0;
}