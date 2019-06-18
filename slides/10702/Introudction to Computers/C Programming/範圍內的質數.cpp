#include<stdio.h>

int is_Prime(int n);

int main()
{
    int a, b;
    scanf("%d", &a);
    scanf("%d", &b);
    
    for(;a<=b;a++)
	{
	    if(is_Prime(a))
	    {
	        printf("%d is a prime\n", a);
	    }
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
