#include <iostream>

using namespace std;

int Fahrenheit(int n)
{
    return 63240 * n  ;
}

int main()
{
    double num;
    cout << "please enter a Celsius value :";
    cin>>num;
    int number;
    number = Fahrenheit(num);
    cout << "Hello world!" << number<<endl;
    return 0;
}
