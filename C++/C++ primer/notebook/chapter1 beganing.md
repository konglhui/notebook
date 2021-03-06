# 第1章 开始

## 1.1 编写一个简单的C++程序

每个C++程序都包含一个或多个函数，其中一个必须命名为main。

一个函数的定义包含四个部分：

- 返回类型（return type）
- 函数名（function name）
- 一个括号包围的形参列表（parameter list）
- 以及函数体（function body）

main函数的返回类型必须是int。

函数定义的最后一部分时函数体，它是一个以左花括号开始，以右花括号结束的语句块（block of statements）

```c++
{
    return 0;
}
```

在大多数系统中，main的返回值被用来指示状态。返回0表明成功，非0的返回值含义有系统定义，通常用来指出错误类型。

### 1.1.1 编译、运行程序

## 1.2 初始输入输出

**标准输入输出对象**

cin的istream类型的对象为标准输入。

cout的ostream类型的对象为标准输出。

```c++
#include <iostream>	//告诉编译器我们要使用iostream库。

int main()
{
    std::cout << "Hello world!" << std::endl;	//第一个输出运算符是字符串字面值常量，第二个是操纵符（endl结束当前行，并将与设备关联的缓冲区（buffer）中的内容射到设备中，为了保证目前为止程序所产生的输出真正写入输出流，而不是停留在内存中等待写入流。）。
    int v1 = 0,v2 = 0;
    std::cin >>v1>>v2;
    std::cout<<"the sum of "<<v1<<" and "<<v2;
    return 0;
}
```

前缀的std：：是定义在名为std的命名空间中的。

**从流读取数据**

`std::cin>>v1>>v2;`输入运算符为>>，输入运算符返回其左侧运算对象作为其结果。，次表达式等价于`(std::cin>>v1)>>v2;`

## 1.3注释简介

#### C++注释的种类

- 单行以（//）开始。
- 继承自C语言的（/* ...*/）之间所有内容都为注释。

**注释界定不能嵌套**

## 1.4 控制流

### 1.4.1 while语句

while语句反复执行一段代码，直至给定条件为假为止。我们可以用while语句编写一段程序，求1到10这10个数之和。

```c++
#include <iostream>

int main()
{
    int sum = 0,val = 1;
    while(val<=10){
        sum+=val;   //将sun+val赋予sum
        ++val;      //将val+1
    }
    std::cout<<"Sum of 1 to 10 inclusive is "
            <<sum<<std::endl;
    return 0;
}
```

while语句的形式为：

```c++
while(condition)
    statement
```

while语句直至condition条件为假时停止。只要condition为真程序就一直执行下去。

`++val;`使用前缀递增运算符（++）。递增运算符将运算对象的值增加1.其等价为`val = val+1`.

## 1.4.2 for语句

可以用for语句重写1道10的程序。

```c++
#include <iostream>

int main()
{
    int sum = 0;
    for(int val = 1;val<=10;++val)
        sum +=val;
    std::cout<<sum<<std::endl;
    return 0;
}
```

每个for语句都包含两部分：循环头和循环体，循环头控制循环体的执行次数，由初始语句、循环条件以及表达式做成。

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180522/Ac8h868E35.png)

### 1.4.3 读取数量不定的输入数据

我们预先不知道要对多少个数求和，这就需要不断读取数据直至没有新的输入为止。

```c++
#include <iostream>

int main()
{
    int sum = 0,value =0;

    while(std::cin>>value)
        sum+=value;
    std::cout<<"sum is "<<sum<<std::endl;

    return 0;
}
```

当我们使用istream对象作为条件是，其效果是检测流的状态。如果流是有效的，即流未遇到错误，那么检测成功。当遇到文件结束符（end-of-file）或遇到无效输入时，会无效，故条件为假。

windows中ctrl+Z是文件结束符。

#### 在探编译

- 语法错误

  - 程序员犯了C++语言文法上的错误。

  - ![mark](http://p6yio0wew.bkt.clouddn.com/blog/180522/6CLb807c4G.png)

    ​

- 类型错误

  - C++中每个数据项都有其类型。
  - ![mark](http://p6yio0wew.bkt.clouddn.com/blog/180522/jmBchgIa7E.png)

- 声明错误

  - C++程序中每个名字都要先声明后使用。
  - ![mark](http://p6yio0wew.bkt.clouddn.com/blog/180522/K4aJBCEkhD.png)

### 1.4.4 if语句

C++也提供if语句来支持条件执行。

用if语句写一个程序，来统计在输入中每个值连续出现了多少次。

```C++
include <iostream>

int main()

{

    int current_val =0,val =0;

    if (std::cin>>current_val){

        int cnt = 1;                    //保存我们正在处理的当前值的个数

        while(std::cin>>val){

            if(val == current_val)		//使用相等运算符（==）判断两值这是否相等

                ++cnt;

            else{

                std::cout<<current_val<< " occurs "<<cnt<<" times "<<std::endl;

                current_val = val;

                cnt = 1;
            }

        }

        std::cout<<current_val<< " occurs "<<cnt<<" times "<<std::endl;

        current_val = val;

        cnt = 1;
    }

    return 0;

}

```

#### C++ 关键概念缩进和格式

C++程序很大程度上数格式自由的，唯一的要求是或括号必须是main的形参列表后第一个非空、非注释的字符。

例如：我们可以把整个main函数写在同一单元行，但会非常难读。

## 1.5 类简介

就是如何定义一个数据类型。在C++中我们通过定义一个类（class）来定义自己的数据结构。 

类机制是C++最重要的特性之一。

为了使用类我们需要了解三件事情：

- 类名是什么？
- 它是在哪里定义的？
- 他支持什么操作？

### 1.5.1 Sales_item类

每个类实际上都定义了一个新的类型，类型名就是类名。因此我们定义类类型的变量可以用如下语句：

```c++
Sales_item item;			//定义了一个Sales_item类型的对象item
```

除了定义类型变量外，我们还可以：

- 调用一个名为isbn的函数从Sales_item对象中提取ISBN书号。
- 用输入运算符和输出运算符读写Sales_item类型的对象。
- 用赋值运算符(=)将一个Sales_item对象赋值给另一个Sales_item类型的对象。
- 用加法运算符（+）将两个Sales_item对象相加。两个对象必须表示同一本书。
- 使用符合赋值运算符，将一个Sales_item对象加到另一个对象上。

#### 关键概念：类定义了行为

类Sales_item的作者定义了类对象可以执行的所有动作，即，Sales_item类定义了创建一个Sales_item对象时会发生的什么事情，以及对Sales_item对象进行赋值。加法时会发生什么情况。

一般而言，类作者决定了类类型对象上可以使用的所有操作。

#### 读写 Sales_item

### 1.5.2 初始成员函数

## 1.6 书店程序

```c++
#include<iostream>
#include "Sales_item.h"

int main()
{
    Sales_item book,current_book;
    if (std::cin>>current_book){
        int cnt = 1;
        while(std::cin>>book){
            if (book.isbn == current_book.isbn)
                book += current_book;
            else{
                std::cout<<book<<" orcus "<<cnt <<" times"<<std::endl;
                book = current_book;
            }
        }
        std::cout << book<<std::endl;
    }
    return 0;
}
```











