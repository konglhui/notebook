#include <iostream>
using std::cin;
using std::cout;
using std::string;
using std::endl;

int main()
{/*
    string s;       //null character
    cin>>s;         //
    cout<<s<<endl;
    return 0;*/

    //read over and over again
    /*string word;
    while(cin>>word)        //read over and over again,while file is null
        cout <<word<<endl;*/

    //using getline read a line
    /*string line;
    while(getline(cin,line))
        cout <<line<<endl;*/

    //string's operate empty and size
    //empty is a judge
    /*string line;
    while(getline(cin,line))
        if(!line.empty())
            cout <<line<<endl;
    */

    //size  return the string size
    /*string line;
    while(getline(cin,line))
        if (line.size()>80)
            cout <<line<<endl;
    */

    //assignment to string
    /*string st1(10,'c'),st2;
    st1 = st2;

    st1 += st2;

    // string add to word
    string s1 = "Hello",s2 = "word";
    string s3 = s1 + ","+ s2;

    cout<<s3<<endl;

    string s7 = ("hello" + ",") +s2; //error:word can't add to word

    //home work
    while(getline(cin,s))
        cout <<s<<endl;

    string s;
    while(cin>>s)
        cout<<s<<endl;

    string s1,s2;
    cin >>s1>>s2;
    if(s1.size() != s2.size()){
        if (s1.size()>s2.size())
            cout<< s1<<endl;
        else{
            cout << s2<<endl;
        }

    }*/

    string s1,s2,s3,s4;
    cin>>s1>>s2>>s3>>s4;
    s1 = s1 +" "+s2;
    s1 = s1+" "+s3;
    s1 = s1+" "+s4;
    cout <<s1;

    return 0;
}