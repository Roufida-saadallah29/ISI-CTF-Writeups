#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand((uint)38);
    for (int i = 0; i < 38; i++) {
        int randomNum = rand(); 
        printf("%d ,", randomNum % 0xff);
    }

    return 0;
}
