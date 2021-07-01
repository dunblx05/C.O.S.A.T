#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main() {
	int n;
	int i = 1;
	int count = 1;
	scanf("%d", &n);
	while (n>i) {
		i = i + 6 * count;
		count++;
	}
	printf("%d", count);
}