#include <stdio.h>

int main()
{
	while(1){
	
		int a;
		printf("叫块0-10ぇ丁计:");
		scanf("%d",&a);
		
		if(a>10 || a<0)
			break;
			//printf("%d 禬絛瞅\n", a);
		else if(a%2==0)
			printf("%d 琌案计\n", a);
		else
			printf("%d 琌计\n", a);
			
	}
	return 0;
} 
