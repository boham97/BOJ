/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include <stdlib.h>

int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

int main()
{
    int n, i;
    int* arr1;
    int arr2[8001] = {0};
    double ans = 0;
    scanf("%d", &n);
    arr1 = (int*)malloc(sizeof(int)* n);
    for(i = 0; i < n; i++){
        scanf("%d", arr1 + i);
        ans += arr1[i];
        arr2[arr1[i] + 4000]++;
    }
    qsort(arr1, n, sizeof(int), compare);
    
    printf("%d\n", ans >= 0 ? (int)(ans / n + 0.5) : (int)(ans / n - 0.5));
    printf("%d\n", arr1[(int)(n/2)]);
    
    int is_change = 0;
    int ans3 = 0;
    int max = 0;
    for(i = 0; i < 8001; i++){
        if(arr2[i] > max){
            max = arr2[i];
            ans3 = i - 4000;
            is_change = 0;
        }else if(arr2[i] == max && is_change == 0){
            is_change = 1;
            ans3 = i - 4000;
        }
    }
    
    printf("%d\n", ans3);
    printf("%d\n", arr1[n -1] - arr1[0]);
    return 0;
}
