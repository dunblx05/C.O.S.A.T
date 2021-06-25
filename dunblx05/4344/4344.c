#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	int c, i, n, j;
	int count = 0;
	int score[1001];
	double avg = 0;
	double ratio = 0;
	int sum = 0;
	scanf("%d", &c);

	for (i = 0; i < c; i++) {
		scanf("%d", &n);
		for (j = 0; j < n; j++) {
			scanf("%d", &score[j]);
			sum = sum + score[j];
		}
		avg = sum / n;
		for (j = 0; j < n; j++) {
			if (score[j] > avg) {
				count++;
			}
		}
		ratio = (double) count / n;
		printf("%.3lf%%\n", ratio * 100);
		sum = 0;
		avg = 0;
		count = 0;
	}
}