#include <stdio.h>
#define SIZE_OF_ARRAY(ary) sizeof(ary) / sizeof(ary[0])

void bubble_sort(int arr[], int n)
{
	for(int i = 0; i < n ; i++)
	{
		for(int j = 0; j < i; j++)
		{
			if(arr[j] > arr[i])
			{
				int temp = arr[j];
				arr[j] = arr[i];
				arr[i] = temp;
			}
		}

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

	bubble_sort(arr1, n);

	output_arr(arr1, n);

	return 0;
}