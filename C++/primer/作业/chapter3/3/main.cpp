#include <iostream>

using namespace std;

int main()
{
    int degrees;
    int minutes;
    int seconds;
    double all_degrees;

    cout << "������ȡ��֡��룺" << endl;
    cout<<"���ȣ������";
    cin>>degrees;
    cout<<"Ȼ�������";
    cin>>minutes;
    cout<<"���������";
    cin>>seconds;

    all_degrees = degrees + minutes/60.0 + seconds / 60.0/ 60.0;
    cout<<degrees<<" ��"<<minutes<<" ��"<<seconds<<" ��"<<"="<<all_degrees<<"��";
    return 0;
}
