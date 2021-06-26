#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

void hansu(int i);

int main() {
	int n;
	scanf("%d", &n);
	hansu(n);
}

void hansu(int i) {
	int n;
	int d1, d2, d3;
	int cnt = 0;
	for (n = 1; n <= i; n++) {
		if (n < 100) {
			cnt++;
		}
		else if (n >= 100 && n<1000) {
			d1 = n % 10;
			d2 = (n / 10) % 10;
			d3 = (n / 100) % 10;
			if ((d1 - d2) == (d2 - d3)) {
				cnt++;
			}
		}
	}
	printf("%d", cnt);
}