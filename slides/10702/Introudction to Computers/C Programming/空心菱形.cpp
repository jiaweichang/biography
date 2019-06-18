#include<stdio.h> 
int main() 
{ 
	int a,b,c,i; 
	printf("輸入一個整數"); 
	scanf("%d",&i); 
	
	for(a=1;a<=2*i-1;a++) 
	{ 
		if(a<=i) 
		{ 
			for(b=i;b>a;b--) 
				printf(" "); 
			
			printf("*"); 
			
			for(c=1;c<=2*a-3;c++) 
				printf(" "); 
		
			if(a>1) 
				printf("*"); 
		} 
		else 
		{ 
			for(b=a;b>i;b--) 
				printf(" "); 
			
			printf("*"); 
			
			for(c=1;c<=4*i-2*a-3;c++) 
				printf(" "); 
			
			if(a<2*i-1) 
				printf("*"); 
		} 
		printf("\n"); 
	} 

return 0; 
} 