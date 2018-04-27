#include<stdio.h>

int main()
{
	int i,j,k;
    int a = 67;
	int temp;
	int legal_num[10] = {18,25,7,36,13,2,89,63,12,34};
	for(i = 0;i<9;i++)
    {
        for (k=0;k<10-i-1;k++)
        {
            if (legal_num[k] >  legal_num[k+1])
            {
                temp = legal_num[k];
                legal_num[k] = legal_num[k+1];
                legal_num[k+1] = temp;
            }
        }
    }
    for (i = 0;i<10;i++)
    {
    	if (a>legal_num[i])
    	{
    		continue;
    	}
    	else
    	{
    		for (j = 0;j<10-i-1;j++)
    		{
    			temp = legal_num[j+1];
    			legal_num[j+1] = legal_num[j];
    		}
    		legal_num[i] = a;
    		break;
    	}


    }
    for (i = 0;i<10;i++)
   {
    		printf("%d\n", legal_num[i]);
	}
    }
