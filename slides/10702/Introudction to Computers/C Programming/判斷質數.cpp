#include<stdio.h>

int is_Prime(int n);

int main()
{
    int n;
    scanf("%d", &n);
    
    if(is_Prime(n))
    {
        printf("It's a prime\n");
    }
	else
	{
        printf("It's not a prime\n");
    }
    
    return 0;
}

int is_Prime(int n)
{
    if(n==1)
        return 0;
    
    for(int i=2; i<n; i++)
    {
        if(n%i==0)
        {
            return 0;
        }
    }
    
    return 1;
}
