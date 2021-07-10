#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void insertion_sort(int arr[], int a);

int main() {
	int n;
	int a[1001] = { 0, };
	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		scanf("%d", &a[i]);
	}

	insertion_sort(a, n);

	for (int i = 0; i < n; i++) {
		printf("%d\n", a[i]);
	}
}

void insertion_sort(int arr[], int a) {
	int i, x, j;

	for (i = 1; i < a; i++) {
		x = arr[i];
		j = i - 1;
		while (j >= 0 && arr[j] > x) {
			arr[j + 1] = arr[j];
			j--;
		}
		arr[j + 1] = x;
	}
}