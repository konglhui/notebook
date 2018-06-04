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

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180525/BkdbcmLf5C.png)

## 2.11

a.定义

b.定义

c.声明

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180525/L2bkii1ea3.png)

## 2.12 

a，c，d违法

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180525/FjB6haGDFI.png)

## 2.13

J = 100

## 2.14

I = 100,SUM = 45

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180525/A88150jEdJ.png)

## 2.15

d：引用必须是对象

d：引用必须初始化

## 2.16

都合法

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180525/Aa51lghcFH.png)

## 2.18

```c++
int i = 0;
int *ptr_i = &i;
ptr_i = 0;	//更改指针的值
*ptr_i = 0;	//更改指针所指的值
```

## 2.19

指针是指向的对象的地址，并且指针本身就是一个对象。

而引用是另一个对象的别名。

引用必须初始化，而指针无需在定义时就初始化

## 2.20 

i = 1764

## 2.21

a 	非法指针和对象类型不同，

b	非法因为指针只能赋地址的值。

## 2.22

判断是不是空指针，

判断指针的对象的值是不是0：

## 2.23

不能，因为首先要确定这个指针是不是合法的，才能判断它所指向的对象是不是合法的。

## 2.24

因为viod支持任何类型，而long只支持long类型

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180525/E9IbHfeDkd.png)

## 2.25

a。	ip指针 	i值	r是i的引用

b.。	i值		ip是空指针	

c。	ip指针	ip2值

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180525/L22iLEEAeB.png)

a.不合法，必须赋初值。

d.不合法const不能改变。

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180525/5JhA5Ha70g.png)

## 2.27

a.不合法，取地址不能赋值

b.合法

c.合法

d.合法

e.合法

f.不合法

g.合法

## 2.28

都不合法

## 2.29

```c++
i = ic;     // 合法, 常量赋值给普通变量
p1 = p3;    // 不合法, p3 是const指针不能赋值给普通指针
p1 = &ic;   // 不合法, 普通指针不能指向常量
p3 = &ic;   // 合法, p3 是常量指针且指向常量
p2 = p1;    // 合法, 可以将普通指针赋值给常量指针
ic = *p3;   // 合法, 对 p3 取值后是一个 int 然后赋值给 ic
```

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180526/Ggik7llb7G.png)

## 2.33

## 2.34

```c++
#include <iostream>

int main()
{
	int i = 0, &r = i;
	auto a = r;   // a是一个整数（r是i的别名，而i是以一个整数）

	const int ci = i, &cr = ci;
	auto b = ci; // b是一个整数（ci的顶层const特性被忽略掉了）
	auto c = cr; // c是一个整数（cr是ci的别名，ci本身是一个顶层const）
	auto d = &i; // d是一个整型指针（整数的地址就是指向整数的指针）
	auto e = &ci; // e是一个指向整数常量的指针（对常量对象去地址是一种底层const）

	const auto f = ci; // ci的推演类型是int，f是const int
	auto &g = ci; // g是一个整型常量引用，绑定到ci

	std::cout << a << std::endl;
	std::cout << b << std::endl;
	std::cout << c << std::endl;
	std::cout << d << std::endl;
	std::cout << e << std::endl;
	std::cout << f << std::endl;
	std::cout << g << std::endl;
	std::cout << "--------------" << std::endl;
	a = 42; b = 42; c = 42; //d = 42; e = 42; g = 42;

	std::cout << a << std::endl;
	std::cout << b << std::endl;
	std::cout << c << std::endl;
	std::cout << d << std::endl;
	std::cout << e << std::endl;
	std::cout << f << std::endl;
	std::cout << g << std::endl;

	return 0;
}
```

## 2.35

```c++
i; 	//整型常量
j;	//整型
k;	//整型常量的引用；
p;	//指向常量的指针
j2;	//整型常量
k2;	//引用整型常量
```

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180526/mahh8hl15D.png)

## 2.36

全是4

## 2.37

c 是 int 类型，值为 3。d 是 int& 类型，绑定到 a。

## 2.38

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180526/EEb33flcdc.png)

## 2.39

error: expected ';' after struct definition

## 2.40

```c++
struct Sales_data{
    std::string bookNo;
    unsigned units_sold = 0;
    double revenues = 0.0;
}
```

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180526/e9mG488KAh.png)

## 2.41

```c++
struct Sales_data{
    std::string bookNo;
    unsigned units_sold = 0;
    double revenues = 0.0;
};

int main()
{
    Sales_data data1,data2;
    double price = 0;
    std::cin >>data1.bookNo >> data1.units_sold>>price;
    data1.revenues = data1.units_sold*price;
    std::cin >>data2.bookNo >> data2.units_sold>>price;
    data2.revenues = data2.units_sold*price;
    
    if (data1.bookNo == data2.bookNo){
        unsigned totalcnt = data1.units_sold + data2.units_sold;
        double total_revenue = data1.revenues + data2.revenues;
        std ::cout<<data1.bookNo<<" "<<totalcnt 
                <<" "<<total_revenue<<" ";
        if (totalcnt != 0){
            std::cout << total_revenue/totalcnt <<std ::endl;
        }
        else{
            std::cout <<"no sales"<<std::endl;
        }
        return 0;
    }
    else{
        std::cerr<<"data must refer to same isbn"<<std::endl;
        return -1;
    }
}
```

### 










