#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <windows.h>
#include <mmsystem.h>
//��Ҫ�����á������������������á�����������ѡ������ӣ�-lwinmm
//��Setting��Compiler��Linker settings��Other link option ��ӣ�-lwinmm
/*
 * ��Ҫ�ر��г�����չ֪ʶ�㣺
 * 1�����������ĺ���������������
 * 2��Sleep()����
 * 3���ַ������鼰�򵥵��ַ�����������Ƚϡ�����
 * 4��ʱ�亯����exit����
 */

#define DAY_COUNT 10
#define MAX 6
int main()
{
    int i,j;          //ѭ�����������ʹ��
    int num = 0;
    int count = 5;  //��ŵ�ǰ���������
    int currDay = 0;//��Ϸ��ǰ���е��˵ڼ���
    int choice;     //��������û���ѡ��
    char tempname[8];//��ʱ�������������ɾ��������������
    int tempCount;  //��ʱ������������źøжȵ���60�ĸ���
    int index = -1; //�������ɾ��������ʱ������
    char name[8];   //��������û����������
    //�������飬�������6���ַ�����ÿ���ַ�������󳤶�Ϊ8���ַ���Ӣ�ģ�
    char names[MAX][8] = {"��ʩ", "����", "���Ѿ�", "����", "�Է���"};
    //�������飬�������5���ַ�����ÿ���ַ�������󳤶�Ϊ8���ַ���Ӣ�ģ�
    char levelNames[5][8] = {"����", "����", "����", "�ʹ���", "�ʺ�"};
    //�������ÿ�����ӵĵȼ�����levelNames���á�-1��ʾδ����
    int level[MAX] = {0, 2, 0, 0, 0, -1};
    //�������ÿ�����ӵĺøжȣ�-1��ʾδ����
    int loves[MAX] = {100, 100, 100, 100, 100, -1};
    printf("��%d�죺\n", ++currDay);
    printf("1���ʵ���ּѡ����\t�����ӣ�\n");
    printf("2�����Ƴ���\t\t���޸�״̬��\n");
    printf("3�������乬��\t\t��ɾ����\n");
    printf("4���޵İ����أ�\t\t�����ң�\n");

    do {
        printf("������ѡ��");
        scanf("%d", &choice);
        switch(choice)
        {
        case 1:
            if (count < MAX)
            {
                //�����������
                printf("���������������:");
                scanf("%s",names[count]);
                level[count] = 0;
                loves[count] =100;
                count++;
            }

            else
            {
                printf("����Ҫע�����壬���Ѿ�����Ϊ��\n");
            }
            break;
        case 2://�ַ������бȽ�
            printf("��������������䣺");
            scanf("%s",tempname);
            for (i = 0;i<count;i++)
            {
                if (strcmp(tempname, names[i]) == 0)
                {
                    loves[i] +=20;
                }
                else
                {
                     loves[i] -=10;
                }
            }
            break;
        case 3:
            printf("���������������");
            for (i = 0;i<count;i++)
            scanf("%s",tempname);
            {
                if (strcmp(tempname, names[i]) == 0)
                {
                    loves[i] +=20;
                }
                else
                {
                     loves[i] -=10;
                }
            }
            break;
        case 4:
            break;
        }
    for(i = 0;i<count;i++)
    {
        printf("%-12s %-12s %-12d\n",names[i],levelNames[level[i]],loves[i]);
    }


    num ++;
    }while(num<=10);

}
