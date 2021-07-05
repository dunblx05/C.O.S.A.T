#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main() {
	int n;
	int i = 2;
	scanf("%d", &n);
	while (n != 1) {
		if (n%i == 0) {
			n = n / i;
			printf("%d\n", i);
		}
		else
			i++;
	}
}
