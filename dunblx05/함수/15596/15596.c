#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

long long sum(int *a, int n) {
	long long ans = 0;
	for (int i = 0; i < n; i++) {
		ans = ans + a[i];
	}
	return ans;
}
