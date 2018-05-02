#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <windows.h>
#include <mmsystem.h>
//需要在设置→编译器→链接器设置→其他链接器选项中添加：-lwinmm
//或Setting→Compiler→Linker settings→Other link option 添加：-lwinmm
/*
 * 需要特别列出的扩展知识点：
 * 1、播放声音的函数及链接器设置
 * 2、Sleep()函数
 * 3、字符串数组及简单的字符串函数，如比较、复制
 * 4、时间函数和exit函数
 */
#pragma comment(lib, "Winmm.lib")
#define DAY_COUNT 10
int main()
{
    int i;          //循环变量，多次使用
    int count = 5;  //存放当前娘娘的总数
    int currDay = 0;//游戏当前进行到了第几天
    int choice;     //用来存放用户的选择
    int tempCount;  //临时变量，用来存放好感度低于60的个数
    int index = -1; //用来存放删除、查找时的索引
    char name[8];   //用来存放用户输入的姓名
    //姓名数组，最多容纳6个字符串，每个字符串的最大长度为8个字符（英文）
    char names[6][8] = {"西施", "貂蝉", "王昭君", "杨玉环", "赵飞燕"};
    //级别数组，最多容纳5个字符串，每个字符串的最大长度为8个字符（英文）
    char levelNames[5][8] = {"贵人", "嫔妃", "贵妃", "皇贵妃", "皇后"};
    //用来存放每个妃子的等级，与levelNames联用。-1表示未启用
    int level[] = {0, 2, 0, 0, 0, -1};
    //用来存放每个妃子的好感度，-1表示未启用
    int loves[] = {100, 100, 100, 100, 100, -1};
    printf("第%d天：\n", ++currDay);
    printf("1、皇帝下旨选妃！\t（增加）\n");
    printf("2、翻牌宠幸\t\t（修改状态）\n");
    printf("3、打入冷宫！\t\t（删除）\n");
    printf("4、朕的爱妃呢？\t\t（查找）\n");
    printf("陛下请选择：");
    scanf("%d", &choice);
    switch(choice)
    {
    case 1:
        if (count < MAX)
        {
            //添加人数操作
            printf("请输入娘娘的名讳");
            scanf("%s",names[count]);
        }

        else
        {
            printf("陛下要注意龙体，后宫已经人满为患\n")；
        }
        break;
    case 2://字符串进行比较
        if(strcmp(name, names[i]) == 0){
                    index = i;
                    continue;
                }
        break;
    case 3:
        break;
    case 4:
        break;
    }
}
