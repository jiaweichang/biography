#include <stdio.h>

int main() {
  int a,b,n,arr[10000],q,r;
  
  scanf("%d", &a);
  scanf("%d", &b);
  scanf("%d", &n);
  
  while (a){
    q=a/b;
    r=a%b;
    
    for(int i=0;i<n;i++){
      arr[i]=(r*10)/b;
      r=(r*10)%b;             
    }
    
    printf("%d", q);
	printf(".");
	
    for(int i=0;i<n;i++){
      printf("%d", arr[i]);            
    }
    
	break; 
  }
  return 0;
}
