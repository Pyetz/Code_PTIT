#include <stdio.h>

int bin(int dec) {
    if (dec == 0) {
        return 0;
    } else {
        return (dec % 2 + 10 * bin(dec / 2));
    }
}

int main() {
    int dec;
    scanf("%d", &dec);

    printf("%d", bin(dec));

    return 0;
}
