#include <iostream>

using namespace std;

int main()
{
    int weight_chi;
    int weight_cun;
    double pound;
    double BMI;
    const int chicun = 12;
    const double kilo_pound = 2.2;
    const double trans_cun = 0.0254;

    cout << "请输入你的身高：xx英尺，xx英寸" << endl;
    cin>>weight_chi;
    cin>>weight_cun;
    weight_cun += weight_chi*chicun;
    double meter = weight_cun*trans_cun;

    cout<<"请输入你的体重:"<<endl;
    cin>>pound;
    double kilogram = pound / kilo_pound;

    BMI = kilogram/(meter*meter);

    cout<<"BMI为："<<BMI<<endl;

    return 0;
}
