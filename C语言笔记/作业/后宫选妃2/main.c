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
    printf("������ѡ��");
    scanf("%d", &choice);
    switch(choice)
    {
    case 1:
        if (count < MAX)
        {
            //�����������
            printf("���������������");
            scanf("%s",names[count]);
            level[count] = 0;
            loves[count] =100;
            count++;
        }

        else
        {
            printf("����Ҫע�����壬���Ѿ�����Ϊ��\n")��
        }
        break;
                if(strcmp(name, names[i]) == 0){
                    index = i;
                    continue;
                }
    case 2://�ַ������бȽ�
        printf("���������������");
        scanf("%s",name);
        if(strcmp(name, names[i]) == 0)
        {
        	index =i;
        	loves[index] +=30;
        	for(j=0;j<count;j++)
        	{
        		loves[j] -=10;
        	}
        }
        else
        {
        	printf("��Ҫ�Ĳ����ڣ��Ҵ��ˡ�")��
        }
        break��
    case 3:
        printf("���������������");
        scanf("%s",name);
        if(strcmp(name, names[i]) == 0)
        {
        	break;
        }
        break;
    case 4:
        break;
    }
}
