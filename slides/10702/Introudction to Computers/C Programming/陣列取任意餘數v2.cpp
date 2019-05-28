#include <stdio.h>

int main() {
  int a,b,n,q,r;
  
  scanf("%d", &a);
  scanf("%d", &b);
  scanf("%d", &n);
  
  while (a){
    q=a/b;
    r=a%b;
    
    printf("%d.", q);
	
    for(int i=0;i<n;i++){
      int temp=(r*10)/b;
      r=(r*10)%b;
	  printf("%d", temp);        
    }
    
	break; 
  }
  return 0;
}
