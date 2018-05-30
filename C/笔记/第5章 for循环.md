# 第5章 for循环

## for循环

**语法：**（将循环三要素放在头上）

```c
for(表达式1;表达式2;表达式3;){
    语句；
}
//例如
for(i = 0;i<9;i++){
    printf("");
}
```

**常量：**

```c
const int num =100;//num是常量，只读模式的，不允许修改。
int num =100;//num是变量，可以修改。
```

for循环的循环模式：

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180425/AFldaCf4fg.png)

for循环常见的问题：

- 忘记定义循环变量或初始值
- 循环条件缺少是会造成死循环
- 循环变量不更新，造成死循环。
- 不可省略分号

## break语句的作用

跳出循环，执行循环之后的语句。

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180425/9i5415bK9C.png)

## continue 语句

跳过本次循环，继续下次循环

![mark](http://p6yio0wew.bkt.clouddn.com/blog/180425/3kek4ifJcF.png)













