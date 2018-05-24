# chapter 2

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180524/6iGJIe5IEd.png)

## 2.1

```c++
short //16位
    
int //16位

long //32位

long long //64位

//无符号类型只能表示0和正数。
//带符号类型可以表示负数 0 正数，但取值范围的大小与无符号类型一样。

//单精度浮点数	可以有6位有效数字
//双精度浮点数	可以有10位有效数字
```

## 2.2

double 或 float

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180524/8KajG4I9KC.png)

## 2.3

32

4294967264

32

-32

0

32

## 2.4 

正确

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180524/949K47LCcA.png)

## 2.5

a. 字符、宽字符、字符串、款字符串

b. 整型、无符号整型、长整型、无符号长整型、8进制整型、16进制整型

c. 浮点型、float浮点型、long double类型。

d. 整型、无符号整型、double、double、

## 2.6

有，

第一行10进制

第二行8进制，但mouth无效，因为8进制没有9

## 2.7

a.\145 = e 		\012 = 换行 		字符串型

b.long double类型	

c.float(正确答案：无效因为1024 是整型，无法变为float)

d.long double

## 2.8

```c++
#include <iostream>

int main()
{
    std::cout << 2 << "\115\012";
    std::cout << 2 << "\t\115\012";
    return 0;
}
```

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180524/abaHgJEem6.png)

## 2.9

a.需要先定义`input_value`

```c++
int input_value
std::cin>>input_value
```

b.由列表初始化类型时，如果存在信息丢失，编译器会报错。

c.wage没有定义，需要先定义

```c++
double wage,salary = wage = 999.99;
```

d.没有错误

## 2.10

`global_str` 和 `global_int` 是全局变量，所以初值分别为空字符串和 0 。 `local_int` 是局部变量并且没有初始化，它的初值是未定义的。 `local_str` 是 string 类的对象，它的值由类确定，为空字符串。 






