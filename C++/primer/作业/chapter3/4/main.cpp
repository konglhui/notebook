#include <iostream>

using namespace std;

int main()
{
    long all_seconds;
    int days;
    int hours;
    int minutes;
    int seconds;
    int temp_seconds;
    const int trans_minutes = 60;
    const int trans_hours = 60;
    const int trans_days = 24;

    cout << "Enter the number of seconds:" ;
    cin>>all_seconds;

    seconds = all_seconds%trans_minutes;
    temp_seconds = all_seconds/trans_minutes;

    minutes = temp_seconds%trans_hours;
    temp_seconds =temp_seconds/trans_hours;

    hours = temp_seconds%trans_days;
    days = temp_seconds / trans_days;
    cout <<all_seconds<<" seconds "<<"="<<days<<" days "<<hours<<" hours "<<minutes<<" minutes "<<seconds<<" seconds "<<endl;

    return 0;
}
