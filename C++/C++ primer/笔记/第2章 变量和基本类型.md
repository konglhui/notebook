## 第2章 变量和基本类型

## 基本内置类型

C++风衣了艺涛包括算数类型（arithmetic type）和空类型（void）。算数类型包括（字符、整数型、布尔值和浮点数）

### 2.1.1 算数类型

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180524/1CG5441b3B.png)

#### 带符号类型和无符号类型*

出去布尔型和扩展的字符型之外，其他整形可以划分为带符号的和无符号的。

通过对类型明前添加unsigned就可以得到无符号类型。

与其他整形不同，字符型分了三种：char、signed char和unsigned char。特别需要注意的，cahr与signed char并不一样。尽管字符型有三种，但自负的表现形式只有两种：带符号和无符号。

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180524/Dd7c09e7K0.png)

## 2.1.2 类型转换

类型所能表示的值的范围决定了转换的过程：

- 当我们把一个非布尔类型的算数值给布尔类型时，初始值为0则结果为false，够则结果为true。
- 当我们把一个布尔值赋给非布尔类型时，初始值为false则结果为0，初始值为true则结果为1.
- 当我们把一个浮点数赋给整数类型时，进行了近似处理。结果值将仅保留浮点数中小数点之前的部分。
- 当我们吧一个整数值赋给浮点类型时，小数部分记为0.如果该整数所占的空间超过了浮点类型的容量，精度可能有损失。
- 当我们赋给无符号类型一个超出它表示范围的值时，结果是初始值对无符号类型表示数值总数取模后的余数。
- 当我们赋给带符号类型一个超出它表示范围的值时，结果是未定义的（undefined）。此时程序可能继续工作、可能奔溃、也可能生成垃圾数据。

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180524/1EgGj7LmJg.png)

#### 含有无符号类型的表达式

```c++
#include <iostream>

int main()
{
    unsigned u = 10;
    int i = -42;
    std::cout << i+i<<std::endl;
    std::cout << i+u <<std::endl;
    return 0;
}
```



![mark](http://p6yio0wew.bkt.clouddn.com/blog/180524/cFg5CEbmg0.png)

### 2.1.3字面值常量

形如42的值被称作字面值常量（literal）。

#### 整数和浮点数字面值

我们能用下面的任意一种形式表示数值20：

```c++
20 	//十进制
024	//8进制
0x14//16进制
```

#### 字符和字符串字面值

由单引号阔起来的字符称为char型字面值，双引号括起来的另个或多个字符则构成字符串型字面值。

```c++
'a' 			//字符字面值
"Hello word!"	//字符串字面值
```

字符串字面值的类型实际上是由常量字符构成的数组。而字符串“A”则代表了一个字符的数组，该数组包含两个字符：一个是字母A，另一个是空字符。

#### 转义系列

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180524/Ck5mjd8HEd.png)

#### 指定字面值的类型

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180524/1HAlI4F174.png)



#### 布尔字面值和指针字面值

true 和 false 是布尔类型的字面值。

nullptr 是指针字面值。

## 2.2 变量

### 2.2.1 变量定义

变量定义的基本形式是：首先是类型说明符（type specifier），随后紧跟一个或多个变量名组成的列表，变量名以逗号分隔，最后以分好结束。

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180524/f8Efm9Fk5G.png)

#### 初始值

当对象在创建时获得了一个特定的值，我们说这个对象被初始化（initialized）了。

在C++中赋值与初始化并不一样。初始化的含义是创建变量时赋予其一个初始值，而赋值的含义是把对象的当前值擦除，而以一个新值来代替。

以下4个语句都可以实现初始化：

```c++
int a = 0;
int a = {0}; //用列表初始化内置类型的变量时，如果存在丢失信息的风险，则编译器将报错。
int a{0};
int a(0);
```

#### 默认初始化

如果定义变量时没有初值，则变量被默认初始化，此时变量被赋予默认值。默认值是什么有变量类型决定，同时定义变量的位置也会对此有影响。

定义在函数体内部类型的对象如果没有初始化，则其值未定义，入伏哦试图拷贝或以其他形式访问此类值将引发错误。类的对象如果没有显式地初始化，则其值由类确定。

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180524/1akbgJ216H.png)

### 2.2.2 变量声明和定义的关系

C++语言支持分离式编译机制，该机制允许将程序分各位若干个文件，每个文件可被独立编译。

为了支持分离式编译，C++将声明个定义区分开。声明使得名字为程序所知，一个文件如果想使用别处定义的名字则必须包含对那个名字的声明。而定义负责创建与名字关联的实体。

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180525/c2e3mHE3FJ.png)

### 2.2.3 标示符

C++的标示符由字母、数字和下划线做成。其中必须以字母或下划线开头。

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180525/mD1C8HBKAb.png)

### 2.2.4 名字的作用域

名字val丁一宇for语句内，在for语句之内可以访问val，但是在main函数的其他部分就不能访问它了。

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180525/7072G6j0iD.png)

#### 嵌套的作用域

作用域能批次包含，被包含的作用域称为内层作用域，包含着别的作用于的作用域称为外城作用域。

如果函数有可能用到全局变量，则不宜在定义一个同名的局部变量。

## 2.3 复合类型

符合类型是指基于其他类型定义的类型。c++有几种，本章介绍引用和指针。

### 2..3.1 引用

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180525/G7A1i7cfml.png)

引用并非对象，相反的，它只是为一个已经存在的对象所起的另外一个名字。

### 2.3.2 指针

指针是指向另外一种类型的符合类型。

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180525/FfCEg43JI3.png)

#### 指针值

指针的值（即地址）应属于下列4中状态之一：

- 只想一个对象
- 只想紧邻对象所占空间的下一个位置
- 空指针，意味着指针没有指向任何对象
- 无效指针，也就是上述情况之外的其他值

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180525/D35gK0476d.png)

#### 空指针

空指针不指向任何对象，在试图使用一个指针之前代码可以首先检查它是否为空。以下列出几个生成空指针的方法：

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180525/IBBaDa1JGi.png)

得到空指针最直接的办法就是用字面值nullptr来初始化指针。

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180525/DAaCKA0ffa.png)

#### 赋值和指针

指针和引用都能提供对其他对象的间接访问，然而在具体细节上而这有很大不同，其中最重要的一点就是引用本身并非一个对象，一旦定义了引用，就无法令其在绑定到另外的对象，之后每次使用这个引用都是访问它最初绑定的那个对象。

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180525/ghIecGLDh7.png)

有时候想搞清楚一条赋值语句到底是改变了指针的值还是改变了指针所指对象的值不太容易，最好的办法就是记住赋值永远改吧in的是等号左侧的对象。

```c++
int i = 42;
int *pi = 0;

pi = &i;	//pi的值发生改变，现在pi指向了i

*pi = 0;	//i的值被改变，指针i并没有发生改变
```

#### void* 指针

void*是一种特殊的指针类型，可用于存放任意对象的地址。一个void*指针存放着一个地址，这一点和其他指针类似。不同的是，我们对该地址中到底是个什么类型的对象并不了解：

```c++
double obj = 3.14,*pd = &obj;	//正确：void*能存放人一类型对象的地址

void *pv = &obj;	//obj可以是任意类型的对象
pv = pd;			//pv可以存放任意类型的指针
```

### 2.3.3 理解符合类型的声明

对基本数据类型和类型修饰符的关系很迷惑，其实手指不过是声明符的一部分罢了。

涉及指针或饮用的声明，一般有两种写法，第一种把修饰符和变量标示符写在一起：

`int *ptr_1,*ptr_2;	//p1,p2都是指向int的指针`

这种形式着重强调变量具有符合类型，第二种把修饰和类型名写在一起，并且每条鱼具值定义一个变量

`int* ptr_1;`
`int* ptr_2;`

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180525/4f0mJGm59m.png)

#### 指向指针的指针

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180525/bKJELdjkl6.png)

#### 指向只真的引用

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180525/blGAea9bcF.png)

## 2.4 const限定符

有时我们希望定义这样一种变量，它的值不能被改变。为了满足这一要求，可以用关键字const对变量的类型加以限定。

`const int bufsize = 512;`

这样我们就吧`bufsize`定义成一个常量。

因为const一旦创建就不能改变，多一必须对const对象初始化。

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180525/HiJab1jHkJ.png)

### 2.4.1 const的引用

可以把引用绑定到const对象上，就想绑定到其他对象上一样，我们称之为对常量的引用。

#### 初始化和对const的引用

 ![mark](http://p6yio0wew.bkt.clouddn.com/blog/180525/kgjbeC7j3j.png)

 #### 对const的引用可能引用一个并非const的对象

 ![mark](http://p6yio0wew.bkt.clouddn.com/blog/180525/mFEFbfiBHB.png)

 ### 2.4.2 指针和const

 与引用一样，也可以令指针指向常量或非常量。指向常量的指针不能用于改变其所指对象的值。要存放常量对象的地址，只能使用指向常量的指针：

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180525/EE1HB4I769.png)

所谓指向常量的指针或引用，不多是指针或引用“自以为是”罢了，它们觉得自己指向了常量，所以自觉地不去改变所指对象的值。

### 2.4.3 顶层const

用名词顶层const表示指针本身是个常量，而用底层const表示指针所指的对象是一个常量。

### 2.2.4 constexpr和常量表达式

常量表达式是指值不会改变并且在编译过程就能得到计算结果的表达式。显然，字面值属于常量表达式。用常量表达式初始化const‘对象也是常量表达式。

一个对象（或表达式）是不是常量表达式由它的数据类型和初始值共同决定，

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180526/7Jcl0J7FeG.png)

#### constexpr 变量

在C++新标准规定，循序将变量声明为constexpr类型以便由编译器来验证变量的值是否是一个常量表达式。

一般来说，如果你认定变量是一个常量表达式，那就把它声明成constexpr类型。

#### 字面值类型

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180526/1A8f2DkEiI.png)

#### 指针和constexpr

必须明确一点，在constexpr声明中如果定义了一个指针，限定符constexpr仅对指针有效，与指针所指对象无关。

```c++
const int *p = nullptr;				//p是一个指向整型常量的指针。
constexpr int *p = nullptr;			//q是一个指向整数的常量指针。
```

## 2.5 处理类型

### 2.5.1 类型别名

类型别名（type alias）是一个名字，它是某种类型的同义词。

有两种方法定义类型别名。传统的方法是使用关键字`typedef`：

```c++
typedef double wages;		//wage 是double 的同义词
typedef wages base,*p;		//base是double的同义词，p是double*的同义词。
```

新标准规定了一种新的方法，使用别名声明类定义类型的别名。

```c++
using si = Sales_item;		//si是Sales_item的同义词
```

类型别名和类型名字等价，只要是类型的名字能出现的地方，就能使用类型别名：

```c++
wages hourly,weekly; 		// = double hourly,weekly;
```

#### 指针、常量和类型别名

### 2.5.2 auto类型说明符

C++ 新标准引入`auto`类型说明符，用它就能让编译器替我们去分析表达式所属于的类型。和原来那些只对应一种特定类型的说明符不同，`auto`让编译器能通过初始值推算变量的类型。显然，`auto`d定义的变量必须有初始值：

```c++
auto item = val1 +val2;		//item初始化为val1与val2相加的结果
```

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180526/e2Jhk7L0AG.png)

使用`auto`也能在一条语句或者能够生命多个变量。因为一条声明语句只能有一个基本数据类型，

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180526/29mmBgHlHb.png)

#### 复合类型、常量和auto

编译器推断出来的`auto`类型有时候与初始值类型并不完全一样，编译器会适当地改变结果类型是其更符合初始化规则。

auto会忽略掉顶层const。同事底层const则会保留下来。

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180526/2BjEf04A91.png)

如果希望能推断出的`auto`类型是一个顶层const，需要明确指出：

```c++
const auto f = ci;
```

### 2.5.3 decltype类型指示符

C++引入了第二种类型说明符`decltype`,它的作用是选择并返回操作数的数据类型。再次过程中，编译器分析表达式并得到他的类型，却并不实际计算表达式的值：

```c++
decltype(f()) sum = x; 		//sum的类型就是函数f的返回类型
```

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180526/bLh8bj0dfE.png)

#### decltype和引用

如果`decltype`使用的表达式不是一个变量，则`decltype`返回表达式结果对应的类型

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180526/ameh95gmBF.png)

`decltype`与`auto`另一处重要的区别是，`decltype`的结果类型与表达式形式密切相关。有一种需要特别注意的是：对于`decltype`所用的表达式来说，如果变量名加上括号，则得到的类型与不加括号有时会不同。

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180526/Ed552ke1Bg.png)

## 2.6 自定义数据结构

从最基础的层面理解，数据结构是把一组相关的数据元素组织起来然后使用它们的策略和方法。

C++语言允许用户以累的形式自定义数据结构，而库类型，string，istream，ostream等也都是以类的形式定义的。

### 2.6.1 定义Sales_data类型

Sales_data初步定义如下

```c++
struct Sales_data{
    std::string bookNo;
    unsigned unites_sold = 0;
    double revenue = 0.0;
}
```

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180526/jFf4ALkaEi.png)

**在类定义的最后不要忘记加上分号。**

类体定义类的成员，我们的类只有数据成员，类的数据成员定义了类的对象的具体内容，每个对象有自己的一份数据成员拷贝。修改一个对象的数据成员，不会影响到其他的数据成员。

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180526/61ABclH7Ej.png)

### 2.6.2 使用`Sales_data`类

#### 添加两个`Sales_data`对象

因为`Sales_data`类没有提供任何操作，所以我们必须编码实现输入、输出和相加的功能。

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180526/5a81Bgm5Li.png)

#### Sales——data对象读入数据

```c++
std::cin >>data1.bookNo >> data1.units_sold>>price;
data1.revenues = data1.units_sold*price;
std::cin >>data2.bookNo >> data2.units_sold>>price;
data2.revenues = data2.units_sold*price;
```
#### 输入两个Sales_data对象的和

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

### 2.6.3 编写自己的头文件

为了确保各个文件中类的定义一致，类通常被定义在头文件中，而且类所在的头文件与类的名字一致。

头文件一旦改变，相关的源文件必须重新编译以获取更新过得声明。

### 预处理概述

确保头文件多次包含仍能安全工作的常用技术是预处理。

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180526/j4ciCmfKc6.png)

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180526/jJhj5ji3DG.png)









