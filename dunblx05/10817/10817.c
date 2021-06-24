#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	int a[3];
	int temp = 0;
	int key, i, j;
	scanf("%d %d %d", &a[0], &a[1], &a[2]);
	for (i = 0; i < 2; i++) {
		for(j=0;j<2-i;j++){
			if (a[j] > a[j + 1]) {
				temp = a[j];
				a[j] = a[j + 1];
				a[j + 1] = temp;
			}
		}
	}

	printf("%d", a[1]);
}