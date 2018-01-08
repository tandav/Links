// put it here in order not to forget how to run c programs
// gcc -o fib fib.c && time ./fib
#include <stdio.h>
 
int fibonacci(int n) 
{   
    if      (n == 0) return 0;
    else if (n == 1) return 1;
    else             return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() 
{
    printf("fib: %d\n", fibonacci(40));
    return 0;
}
