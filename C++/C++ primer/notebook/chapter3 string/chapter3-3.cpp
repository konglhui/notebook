#include<iostream>
#include<vector>

using std::vector;
using std::cin;
using std::cout;
using std::endl;
using std::string;

int main()
{
    /*
    vector<int> ivec;           //initialization ,svec don't have any element.
    vector<int> ivec2(ivec);    //ivec copy to ivec2.
    vector<int> ivec3 = ivec;   //ivec copy to ivec3.
    */

   /*
    vector<int> v2;
    for (int i=0;i!=100;++i){
        v2.push_back(i);
    }
    cout << v2<<endl;
    */

    string word;
    vector<string> text;
    while (cin>>word){
        text.push_back(word);
    }
}
