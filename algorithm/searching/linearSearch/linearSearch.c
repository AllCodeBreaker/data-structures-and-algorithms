#include <stdio.h>

int linearSearch(int array[], int size, int target){
	int i ;
	for(i = 0 ; i < size ; i++){
		if(array[i] == target){
			return i;	
		}
		
	}
	return -1;

}

int main(){
	int array[] = {192,54,53,46,43,76};
	int t1 = 54, t2 = 55, i;
	size_t size = (int)sizeof(array)/sizeof(array[0]);
	printf("Array is :");
	for (i=0; i<6;i++){
		printf(" %d,", array[i]);	
	}
	
	printf("Target 1: %d\nTarget 2: %d", t1, t2);
	printf("\nResult for %d : %d\nResult for %d : %d", t1, linearSearch(array, size, t1), t2, linearSearch(array, size, t2));
	
	
	return 0;

}
