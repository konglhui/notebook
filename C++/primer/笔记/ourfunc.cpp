#include<iostream>
void simon(int)             //simon()函数原型

int main(){
    using namespace std;
    simon(3);
    cout <<"pick an integer";
    int count;
    cin>>count;
    simon(count);
    cout << "Done!" <<endl;
    return 0;
}

void simon(int n){
    using namespace std;
    count <<"simon saus touch your toes"<<n<<"times"<<endl;
}

