#include <stdio.h>
#define SIZE_OF_ARRAY(ary) sizeof(ary) / sizeof(ary[0])

void insertion_sort(int arr[], int n)
{
	int i, j;
    int temp;
    for (i = 1; i < n; i++)
    {
        temp = arr[i]; 
        j = i - 1;     
        for (; j >= 0 && arr[j] > temp; j--) 
        {
            arr[j + 1] = arr[j];             
        }
        arr[j + 1] = temp;                  
    }
}

void output_arr(int arr[], int n)
{
	for(int i = 0; i < n; i++)
	{
		printf("%d", arr[i]);
		printf("\n");
	}
}

int main()
{
	int arr1 = {3, 2, 1, 7, 6, 5, 9, 8, 7};

	int n = SIZE_OF_ARRAY(arr1);
	printf("%d\n", n);

	insertion_sort(arr1, n);

	output_arr(arr1, n);

	return 0;
}

/*
http://notepad.yehyeh.net/Content/Algorithm/Sort/Insertion/1.php
*/