# chapter5

## 请问下面哪些散列函数是一致的？

5.1 f(x) = 1 					一致

5.2 f(x) = rand()				不一致

5.3 f(x) = next_empty_slot()	不一致

5.4 f(x) = len(x)				一致

## 5.5

散列函数的结果必须是均匀分布的，这很重要。它们的映射范围必须尽可能大。最糟糕的散列函数莫过于将所有输入都映射到散列表的同一个位置。

假设你有四个处理字符串的散列函数。
A. 不管输入是什么，都返回1。

B. 将字符串的长度用作索引。

C. 将字符串的第一个字符用作索引。即将所有以a打头的字符串都映射到散列表的
同一个位置，以此类推。

D. 将每个字符都映射到一个素数： a = 2， b = 3， c = 5， d = 7， e = 11，等等。对于给定的字符串，这个散列函数将其中每个字符对应的素数相加，再计算结果除以散列表长度的余数。例如，如果散列表的长度为10，字符串为bag，则索引为(3 + 2 + 17) % 10 = 22 % 10 = 2。

在下面的每个示例中，上述哪个散列函数可实现均匀分布？假设散列表的长度为10。

答：B，D

5.5 将姓名和电话号码分别作为键和值的电话簿，其中联系人姓名为Esther、 Ben、 Bob和Dan。

```python 
phonenumber = dict()
phonenumber['Esther'] = 132
phonenumber['Ben'] = 132
phonenumber['Bob'] = 132
```

5.6 电池尺寸到功率的映射，其中电池尺寸为A、 AA、 AAA和AAAA。

```python 
phonenumber = dict()
phonenumber['A'] = 132
phonenumber['AA'] = 132
phonenumber['AAA'] = 132
```

5.7 书名到作者的映射，其中书名分别为Maus、 Fun Home和Watchmen。

```python 
phonenumber = dict()
phonenumber['Maus'] = 132
phonenumber['Fun Home'] = 132
phonenumber['Watchmen'] = 132
```














