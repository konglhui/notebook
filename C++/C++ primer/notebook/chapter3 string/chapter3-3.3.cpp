#include<iostream>
#include<vector>

using std::vector;
using std::cin;
using std::cout;
using std::endl;
using std::string;

int main(){
    /*
    vector(unsigned) scores(11,0);
    unsigned grade;
    while (cin>>grade){
        if (grade<=100){
            ++scores[grade/10];
        }
    }
    */

    vector<int> ivec;
    for (decltype(ivec.size()) ix = 0;ix !=10;++ix){
        ivec.push_back(ix);
    }
}