#include<stdio.h>
void main(){
	int i=0;
	int total = 0;
	int last_day = 1;
	int previou_day = 0;
	while (i < 9){
		i++;
		previou_day = (last_day+1)*2;
		last_day = previou_day;
	}
	printf("%d\n",last_day );
}