![mark](http://p6yio0wew.bkt.clouddn.com/blog/180529/A0LhGfFaj4.png)

## 3.2

```c++
	string s;    
	while(getline(cin,s))
        cout <<s<<endl;
        
    while(cin>>s)
        cout<<s<<endl;
```

## 3.3

string类的输入时判断段空白符就停止

getline的输入时判断换行符停止

## 3.4

```c++
    string s1,s2;
    cin >>s1>>s2;
    if(s1 != s2){
        if (s1>s2)
            cout<< s1<<endl;
        else{
            cout << s2<<endl;
        }

    }
    return 0;
//2
    string s1,s2;
    cin >>s1>>s2;
    if(s1.size() != s2.size()){
        if (s1.size()>s2.size())
            cout<< s1<<endl;
        else{
            cout << s2<<endl;
        }

    }
    return 0;
```

## 3.5

```c++
    string s1,s2,s3,s4;
    cin>>s1>>s2>>s3>>s4;
    s1 += s2;
    s1 += s3;
    s1 += s4;
    cout <<s1;

    return 0;
//2
    string s1,s2,s3,s4;
    cin>>s1>>s2>>s3>>s4;
    s1 = s1 +" "+s2;
    s1 = s1+" "+s3;
    s1 = s1+" "+s4;
    cout <<s1;

    return 0;
```

## 3.6

```c++
#include <iostream>
using std::endl;
using std::cin;
using std::cout;
using std::string;

int main()
{
    string s("asdfasdfasdf");
    for (auto &c:s){
        c= 'x';
    }
    cout <<s<<endl;
    return 0;
}
```

## 3.7

没啥变化

## 3.8

当然是for循环，while循环需要索引来改变需要的每一个字母。

## 3.9 

不合法，它返回的是s的第一个字母，但是s没有定义初值。

## 3.10

```c++
#include <iostream>
using std::endl;
using std::cin;
using std::cout;
using std::string;

int main()
{
    string s("asdfasd.,fa12,.,s.d.f!");
    for (auto &c:s)
        if (isalnum(c))
            cout <<c<<endl; 
    return 0;
}
```

## 3.11

合法，`const char`类型。

## 3.12

a.合法

b.不合法

c.合法

## 3.13

a.不包含

b.10个，为定义

c.10个，42

d.1个，10

e.2个，10与42

f.10个，为定义

g.10个，hi

## 3.14

```c++
#include <iostream>
#include<vector>
using std::endl;
using std::cin;
using std::cout;
using std::string;
using std::vector;

int main()
{
    int word;
    vector<int> text;
    while (cin>>word){
        text.push_back(word);
    }
}
```

## 3.15

```c++
#include <iostream>
#include<vector>
using std::endl;
using std::cin;
using std::cout;
using std::string;
using std::vector;

int main()
{
    string word;
    vector<string> text;
    while (cin>>word){
        text.push_back(word);
    }
}
```

## 3.16

就不做了

## 3.17

```c++
#include <iostream>
#include<vector>
using std::endl;
using std::cin;
using std::cout;
using std::string;
using std::vector;
using std::toupper;

int main()
{
    string word;
    vector<string> text;
    while (cin>>word){
        for (auto &c:word)
            c = toupper(c);
        text.push_back(word);
    }
    for (auto a:text){
        cout<<a<<endl;
    }
    return 0;
}
```

## 3.18

不合法

`ivec.push_back(42)`

## 3.19

1.`vector<int> a(10,42);`

2.`vector<int> a{42,42,42,42,42,42,42,42,42,42};`

3.

```vector<int> ivec3;
for (int i = 0; i < 10; ++i)
	ivec3.push_back(42);
```

当然是第1种最好。

## 3.20

```c++
#include <iostream>
#include<vector>
using std::endl;
using std::cin;
using std::cout;
using std::string;
using std::vector;
using std::toupper;

int main()
{
	vector<int> ivec;
	int i;
	while (cin >> i){
		ivec.push_back(i);
	}
	for (int i = 0; i < ivec.size() - 1; ++i){
		cout << ivec[i] + ivec[i + 1] << endl;
	}
	//---------------------------------
	cout << "---------------------------------" << endl;
	int m = 0;
	int n = ivec.size() - 1;
	while (m < n){
		cout << ivec[m] + ivec[n] << endl;
		++m;    --n;
	}
	return 0;
}
```

## 3.21

```
#include<iostream>
#include<vector>

using namespace std;

void check_and_print(const vector<int>& vec)
{
    cout <<"size: "<<vec.size()<<"  content:[";
    for (auto it = vec.begin();it != vec.end(); ++it){
        cout <<*it <<(it != vec.end() -1?",":"");
    }
    cout <<"]\n" <<endl;
}

int main()
{
    vector<int> v1;
	vector<int> v2(10);
	vector<int> v3(10, 42);
	vector<int> v4{ 10 };
	vector<int> v5{ 10, 42 };
	vector<string> v6{ 10 };
	vector<string> v7{ 10, "hi" };

    check_and_print(v1);
	check_and_print(v2);
	check_and_print(v3);
	check_and_print(v4);
	check_and_print(v5);
    return 0;
}
```

## 3.22

```
#include<iostream>
#include<vector>

using namespace std;

int main()
{
	vector<string> text;
	text.push_back("aaaaaaaaa aaaaaaaaaaaa aaaa");
	text.push_back("");
	text.push_back("bbbbbbb bbbbbbbb bbbbbbbbbbbb");

	for (auto it = text.begin(); it != text.end() && !it->empty();++it){
		for (auto &c: *it)
			if (isalpha(c)) c = toupper(c);
	}
	for (auto it: text)
		cout  <<it <<endl;
    return 0;
}
```

## 3.27

a.非法，非const

b.合法

c.非法，非const

d.非法，值超了

## 3.28

sa 空字符

ia  0000000000

sa2空字符

ia2 未定义

## 3.29

- 数组大小是确定的
- 不能随意增加元素
- 不允许拷贝和赋值

## 3.30

当ix 增长到10，就会出现索引错误。

## 3.31

```c++
int main()
{
	int arr[10] = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };

	return 0;
}
```

## 3.32

```c++
#include<iostream>
#include<vector>

using namespace std;

int main()
{
	int arr[10] = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
	int arr2[10] ;
	for (auto i : arr)
		arr2[i] = i;
	for (auto j:arr2)
		cout <<j<<endl;
	vector<int> v(10);
	for (auto i:arr)
		v[i] = i;
	for (auto i :v)
		cout << i <<endl;
    return 0;
}
```

## 3.33

数组中所有元素的值将会未定义。

