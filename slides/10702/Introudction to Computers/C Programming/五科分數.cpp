#include <stdio.h>

int main()
{
	int a,b,c,d,e;
	
	printf("請輸入數學成績:");
	scanf("%d",&a);
	
	printf("請輸入英文成績:");
	scanf("%d",&b);  
	
	printf("請輸入國文成績:");
	scanf("%d",&c); 
	 
	printf("請輸入地理成績:");
	scanf("%d",&d);  
	
	printf("請輸入物理成績:");
	scanf("%d",&e);  
	
	int avg = (a+b+c+d+e)/5;
	printf("平均: %d\n", avg);
	
	if(a<60)
		printf("數學不及格\n");
	if(b<60)
		printf("英文不及格\n");
	if(c<60)
		printf("國文不及格\n");
	if(d<60)
		printf("地理不及格\n");
	if(e<60)
		printf("物理不及格\n");
			
	if(a >= b && a >= c && a >= d && a >=e)
		printf("數學為最高分\n");
	if(b >= a && b >=c && b >= d && b >=e)
		printf("英文為最高分\n");
	if(c >= a && c >= b && c >= d && c >=e)
		printf("國文為最高分\n");
	if(d >= a && d >= b && d >= c && d >=e)
		printf("地理為最高分\n");
	if(e >= a && e >= b && e >= c && e >=d)
		printf("物理為最高分\n");
	
	if(a <= b && a <= c && a <= d && a <=e)
		printf("數學為最低分\n");
	if(b <= a && b <=c && b <= d && b <=e)
		printf("英文為最低分\n");
	if(c <= a && c <= b && c <= d && c <=e)
		printf("國文為最低分\n");
	if(d <= a && d <= b && d <= c && d <=e)
		printf("地理為最低分\n");
	if(e <= a && e <= b && e <= c && e <=d)
		printf("物理為最低分\n");
	
	return 0;	
} 
