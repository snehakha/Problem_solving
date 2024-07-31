#include <stdio.h>

int main() 
{
    int num, i;
    long long product = 1; 

    printf("Enter the number of elements in the array: ");
    scanf("%d", &num);
    int arr[num];

    printf("Enter the elements: ");
    for (i = 0; i < num; i++)
    {
        scanf("%d", &arr[i]);
        product *= arr[i]; 
    }

    printf("Product of the elements in the array: %lld\n", product);

    return 0;
}
