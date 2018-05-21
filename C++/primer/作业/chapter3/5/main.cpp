#include <iostream>

using namespace std;

int main()
{
    double mileage;
    double oil;
    char ch;

    cout << "if you want cal a gallon ,input 1" << endl;
    cout <<"if you want a hundred kilometers,input 0"<<endl;
    cin >>ch;

    if (ch == '1'){
        cout <<"mileage:";
        cin>>mileage;
        cout <<"oil gallon:";
        cin>>oil;

        cout<<mileage/oil;

    }
    else{
        cout <<"kilometers:";
        cin>>mileage;
        cout <<"litre:";
        cin>>oil;

        cout<<oil/mileage*100.0;

    }
    return 0;
}
