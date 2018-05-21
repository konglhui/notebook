#include <iostream>

using namespace std;

int main()
{
    int degrees;
    int minutes;
    int seconds;
    double all_degrees;

    cout << "请输入度、分、秒：" << endl;
    cout<<"首先，输入度";
    cin>>degrees;
    cout<<"然后，输入分";
    cin>>minutes;
    cout<<"最后，输入秒";
    cin>>seconds;

    all_degrees = degrees + minutes/60.0 + seconds / 60.0/ 60.0;
    cout<<degrees<<" 度"<<minutes<<" 分"<<seconds<<" 秒"<<"="<<all_degrees<<"度";
    return 0;
}
