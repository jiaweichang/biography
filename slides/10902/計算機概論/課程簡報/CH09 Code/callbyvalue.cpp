#include <stdio.h>

void swap(int x, int y) // 以值傳遞
{
    printf("before - x: %d, y: %d \r\n", x, y);
    
    int temp;
    
    temp = x;
    x = y;
    y = temp;
    
    printf("after - x: %d, y: %d \r\n", x, y);
}

int main()
{
    int a,b;
    
    a=3;
    b=5;
    
    printf("before - a: %d, b: %d \r\n", a, b);
    
    swap(a,b);
    
    printf("after - a: %d, b: %d \r\n", a, b);

    return 0;
}
