#include <iostream>

using namespace std;

int main()

{


    double hundred_miloage_oil;
    double a_kilometer_oil;
    const double mileage = 62.14;
    const double oil = 3.875;

    cout <<"hundred miloage oil:";
    cin>>hundred_miloage_oil;

    a_kilometer_oil = hundred_miloage_oil*oil/ mileage;

    cout<<hundred_miloage_oil<<" hundred miloage oil "<<1/a_kilometer_oil<< " a kilometer oil";

    return 0;

}
