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
#pragma comment(lib, "Winmm.lib")
#define DAY_COUNT 10
int main()
{
    int i;          //ѭ�����������ʹ��
    int count = 5;  //��ŵ�ǰ���������
    int currDay = 0;//��Ϸ��ǰ���е��˵ڼ���
    int choice;     //��������û���ѡ��
    int tempCount;  //��ʱ������������źøжȵ���60�ĸ���
    int index = -1; //�������ɾ��������ʱ������
    char name[8];   //��������û����������
    //�������飬�������6���ַ�����ÿ���ַ�������󳤶�Ϊ8���ַ���Ӣ�ģ�
    char names[6][8] = {"��ʩ", "����", "���Ѿ�", "����", "�Է���"};
    //�������飬�������5���ַ�����ÿ���ַ�������󳤶�Ϊ8���ַ���Ӣ�ģ�
    char levelNames[5][8] = {"����", "����", "����", "�ʹ���", "�ʺ�"};
    //�������ÿ�����ӵĵȼ�����levelNames���á�-1��ʾδ����
    int level[] = {0, 2, 0, 0, 0, -1};
    //�������ÿ�����ӵĺøжȣ�-1��ʾδ����
    int loves[] = {100, 100, 100, 100, 100, -1};
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
        }

        else
        {
            printf("����Ҫע�����壬���Ѿ�����Ϊ��\n")��
        }
        break;
    case 2://�ַ������бȽ�
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
