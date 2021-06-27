#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	int t, i, j, k;
	int r;
	char s[21];
	scanf("%d", &t);
	for (i = 0; i < t; i++) {
		scanf("%d", &r); 
		scanf("%s", s);
		char p[161];
		for (j = 0; j < strlen(s); j++) {
			for (k = 0; k < r; k++) {
				printf("%c", s[j]);
			}
		}
		printf("\n");
	}
 }