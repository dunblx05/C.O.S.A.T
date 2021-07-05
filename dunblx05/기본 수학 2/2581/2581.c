#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int prime(int a, int b);
int prime_min(int a, int b);

int main() {
	int m, n;
	scanf("%d", &m);
	scanf("%d", &n);
	printf("%d\n", prime(m, n));
	if (prime_min(m, n) == 0) {
		return 0;
	}
	else
		printf("%d", prime_min(m, n));
}

int prime(int a, int b) {
	int i, j;
	int sum = 0;
	int check = 0;
	int p_count = 0;
	for (i = a; i <= b; i++) {
		if (i % 2 == 0) {
			if (i == 2) {
				sum = sum + i;
				p_count++;
			}
			sum = sum;
		}
		else if (i % 2 == 1) {
			for (j = 1; j <= i; j++) {
				if (i%j == 0) {
					check++;
				}
			}
			if (check == 2) {
				sum = sum + i;
				p_count++;
			}
			check = 0;
		}

	}
	if (p_count == 0) {
		return -1;
	}
	else
		return sum;
}

int prime_min(int a, int b) {
	int i, j;
	int min = 0;
	int check = 0;
	int p_count = 0;

	for (i = a; i <= b; i++) {
		if (i % 2 == 0) {
			if (i == 2) {
				min = i;
				break;
			}
		}
		else if (i % 2 == 1) {
			for (j = 1; j <= i; j++) {
				if (i%j == 0) {
					check++;
				}
			}
			if (check == 2) {
				min = i;
				break;
			}
			check = 0;
		}
		
	}
	if (min == 0) {
		return 0;
	}
	return min;

}