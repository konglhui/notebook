# chapter 1



![mark](http://p6yio0wew.bkt.clouddn.com/blog/180522/JEl8LIDk7F.png)

## 1.1

略

##1.2

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180522/makJ6bA5kj.png)

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180522/Cd5j0gJG2I.png)

1.3

```c++
#include <iostream>

int main()
{
    std::cout<<"Hello Word!";
    return 0;
}
```

1.4

```c++
#include <iostream>

int main()
{
    std::cout << "enter two nuimber:" << std::endl;
    int v1 = 0,v2 = 0;
    std::cin >>v1>>v2;
    std::cout<<v1<<" + "<<v2 <<" = "<<v1+v2<<std::endl;
    std::cout<<v1<<" * "<<v2 <<" = "<<v1*v2<<std::endl;
    return 0;
}
```

1.5

```c++
#include <iostream>

int main()
{
	std::cout << "Enter two numbers:" << std::endl;
	int v1 = 0, v2 = 0;
	std::cin >> v1 >> v2;
	std::cout << "The product of ";
	std::cout << v1;
	std::cout << " and ";
	std::cout << v2;
	std::cout << " is ";
	std::cout << v1 * v2;
	std::cout << std::endl;
	return 0;
}
```

1.6

不合法，没有函数名，去掉前两句结尾的；，或者在后两句加上std::cout。

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180522/8G6iLd177e.png)

1.7

error: expected constructor, destructor, or type conversion before '/' token

1.8

只有第三个有错误：

改变方法：`std::cout<</*"*/"*/";`

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180522/8LjAK8LFeA.png)

1.9

```c++
#include <iostream>

int main()
{
    int sum = 0,val = 50;
    while(val<=100){
        sum+=val;   //将sun+val赋予sum
        ++val;      //将val+1
    }
    std::cout<<"Sum of 1 to 10 inclusive is "
            <<sum<<std::endl;
    return 0;
}
```

1.10

```c++
#include <iostream>

int main()
{
    int val = 10;
    while(val>=0){
    std::cout<<val<<std::endl;
    --val;      //将val-1
    }
    return 0;
}
```

1.11

```c++
#include <iostream>

int main()
{
    int num1 = 0,num2 =0;

    std::cout<<"Enter two numbers,from small to big:"<<std::endl;
    std::cin>>num1>>num2;

    while(num1<=num2){
    std::cout<<num1<<std::endl;
    ++num1;
    }
    return 0;
}
```

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180522/ac88i49bbg.png)

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180522/KedcC0Egda.png)

1.12

完成从-100一直加到100.sum=0.

1.13

(1)

```c++
#include <iostream>

int main()
{
    int sum = 0;
    for(int val = 50;val<=100;++val)
        sum+=val;   //将sun+val赋予sum

    std::cout<<"Sum of 1 to 10 inclusive is "
            <<sum<<std::endl;
    return 0;
}
```

(2)

```c++
#include <iostream>

int main()
{
    for(int val=10;val>=0;--val)
    std::cout<<val<<std::endl;

    return 0;
}
```

(3)

```c++
#include <iostream>

int main()
{
    int num1 = 0,num2 =0;

    std::cout<<"Enter two numbers,from small to big:"<<std::endl;
    std::cin>>num1>>num2;

    for(;num1<=num2;++num1)
    std::cout<<num1<<std::endl;

    return 0;
}
```

1.14

for 我们容易知道循环次数，

而while我们一般只知道循环条件。

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180522/3mAc73l2ml.png)

1.17

如果输入所有值都相等，会输出本次输入的值是多少，输入了多少次。

如果输入所有值都不相等，会输出最后一次的值，输出了一次。

1.18略

1.19

```c++
#include <iostream>

int main()
{
    int num1 = 0,num2 =0;

    std::cout<<"Enter two numbers:"<<std::endl;
    std::cin>>num1>>num2;
    if (num1 <= num2){
        while(num1<=num2){
            std::cout<<num1<<std::endl;
            ++num1;
 	   }
    }
    else{
        while(num1>=num2){
            std::cout<<num2<<std::endl;
            ++num2;
        }
    }
    return 0;
}
```

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180522/Ka5G62gcCe.png)

1.20

略

1.21

```c++
#include<iostream>
#include "Sales_item.h"

int main()
{
    Sales_item book,bool2;

    std::cin>>book>>book2;
    std::cout <<book+bool2<<std::endl;
    return 0;
}

```

1.22

```c++
#include<iostream>
#include "Sales_item.h"

int main()
{
    Sales_item book,current_book;
    std::cin>>book;
    do{
    std::cin>>current_book;
    if (book.isbn == current_book.isbn);
        book += current_book;

    }while(current_book.isbn == book.isbn);
    std::cout <<book<<std::endl;
    return 0;
}
```



