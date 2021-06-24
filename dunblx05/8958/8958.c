#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	int n, i, j;
	int sum = 0;
	int score = 0;
	char quiz[81];
	scanf("%d", &n);

	for (i = 0; i < n; i++) {
		scanf("%s", quiz);

		for (j = 0; j < strlen(quiz); j++) {
			if (quiz[j] == 'O') {
				sum = sum + 1;
			}
			else
				sum = 0;
			score = score + sum;
		}
		printf("%d\n", score);
		sum = 0;
		score = 0;
	}

}