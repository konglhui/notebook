#include <iostream>

using namespace std;

int Fahrenheit(int n)
{
    return 1.8 * n + 32.0;
}

int main()
{
    int num;
    cout << "please enter a Celsius value :";
    cin>>num;
    int number;
    number = Fahrenheit(num);
    cout << "Hello world!" << number<<endl;
    return 0;
}
