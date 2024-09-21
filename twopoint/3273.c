/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include <stdlib.h>
int comp(const void* a, const void* b){
    return (*(int*)a - *(int*)b);
}
int main()
{
    int n, x;
    int* arr;
    int l, r;
    int ans = 0;
    int now;
    scanf("%d", &n);
    arr = (int*)malloc(n * sizeof(int));
    for(int i = 0; i < n; i++){
        scanf("%d", &arr[i]);
    }
    scanf("%d", &x);
    qsort(arr, n, sizeof(int), comp);
    l =0;
    r = n -1;
    while(l< r){
        now = arr[l] + arr[r];
        if (now < x){
            l++;
        }else if (now == x){
            l++;
            ans++;
        }else{
            r--;
        }
    }
    printf("%d", ans);
    return 0;
}
