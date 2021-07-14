#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int main() {
	int n, a;
	int max = 0;
	int count[10001] = { 0, };
	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		scanf("%d", &a);
		if (max < a) {
			max = a;
		}
		count[a]++;
	}

	for (int i = 0; i <= max; i++) {
		if (count[i] != 0) {
			printf("%d\n", i);
			count[i]--;
			i = i - 1;
		}
	}
}

/*
void count_sort(int init[], int res[], int k, int n);

void count_sort(int init[], int res[], int k, int n) {
	int i, j;

	for (i = 1; i <= k; i++) {
		count[i] = 0;
	}

	for (j = 1; j <= n; j++) {
		count[init[j]]++;
	}

	for (i = 2; i <= k; i++) {
		count[i] = count[i] + count[i - 1];
	}

	for (j = n; j >= 1; j--) {
		res[count[init[j]]--] = init[j];
	}
}
*/