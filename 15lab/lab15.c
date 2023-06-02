#include <stdio.h>
#include <math.h>

double f(double i) {
    double drob;
    drob = (double)3/11;
    return sqrt(i+2) - sqrt(i) - drob;
}

double g(double j) {
    return ((3*pow(j,2)) - 11) / (pow((-j), 3) - 2);
}

int main() {
    int n = 10;  
    double a[n][n];  
    double total_sum = 0;  

    
    for (int i = 0; i < 10; i++) { 
        for (int j = 0; j < 10; j++) {
            a[i][j] = f(i+1) + g(i+1);
            total_sum += a[i][j];  
        }
    }
    double total;
    double ch;
    ch = (double)1/100;
    total = (ch*total_sum);

    printf("%lf\n", total);
   
    return 0;
}
