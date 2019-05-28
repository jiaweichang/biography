#include <stdio.h>

int main()
{
    int taxi_dist, price;
   
    printf("請輸入里程數 -> ");
    scanf("%d", &taxi_dist);
    
	if (taxi_dist>=0 && taxi_dist<=5000)
    {
        if (taxi_dist >= 1500)
        {
           price = 70 + 5*(taxi_dist-1500)/500;
           
		   if ((taxi_dist-1500)%500 != 0)
              price += 5;
        }
        else
           price = 70;
        
		printf("價格是%d元\n",price);
    }
    else
       printf("請輸入0-5000的距離範圍!\n");    
    
    return 0;
}
