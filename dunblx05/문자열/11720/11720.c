#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

int main() {
	int n, i;
	char str[101];
	int num[101];
	int sum = 0;
	scanf("%d", &n);
	getchar();
	for (i = 0; i < n; i++) {
		scanf("%c", &str[i]);
	}
	for (i = 0; i < n; i++) {
		num[i] = str[i] - 48;
		sum = sum + num[i];
	}
	printf("%d", sum);
 }