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

    cout << "�����������ߣ�xxӢ�ߣ�xxӢ��" << endl;
    cin>>weight_chi;
    cin>>weight_cun;
    weight_cun += weight_chi*chicun;
    double meter = weight_cun*trans_cun;

    cout<<"�������������:"<<endl;
    cin>>pound;
    double kilogram = pound / kilo_pound;

    BMI = kilogram/(meter*meter);

    cout<<"BMIΪ��"<<BMI<<endl;

    return 0;
}
