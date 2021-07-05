#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main() {
	int n, a;
	int count = 0;
	int check = 0;
	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		scanf("%d", &a);
		if (a % 2 == 0) {
			if (a == 2) {
				count++;
			}
			else
				count = count;
		}
		else if (a % 2 == 1) {
			for (int j = 1; j <= a; j++) {
				if (a%j == 0) {
					check++;
				}
			}
			if (check == 2) {
				count++;
			}
			check = 0;
		}
	}
	printf("%d", count);
}