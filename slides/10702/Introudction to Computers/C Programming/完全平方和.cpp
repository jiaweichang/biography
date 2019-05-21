#include<stdio.h>

int main()
{
    int min, max;
    scanf("%d", &min);
    scanf("%d", &max);
    
    int sum = 0;
    
    for(int i=1 ; i*i <= max ; i++)
    {
    	if(i*i>=min && i*i<=max)
			sum = sum + i*i;
	}
	
	printf("%d", sum);
	
    return 0;
}
