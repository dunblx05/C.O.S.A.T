#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

void d();

int main() {
	d();
}

void d() {
	int i, res;
	int arr[10001] = { 0, };
	for (i = 0; i < 10000; i++) {
		if (i < 10) {
			res = i + i % 10;
			arr[res] = 1;
		}
		if (i >= 10 && i < 100) {
			res = i + (i % 10) + ((i / 10) % 10);
			arr[res] = 1;
		}
		if (i >= 100 && i < 1000) {
			res = i + (i % 10) + ((i / 10) % 10) + ((i / 100) % 10);
			arr[res] = 1;
		}
		if (i >= 1000 && i < 10000) {
			res = i + (i % 10) + ((i / 10) % 10) + ((i / 100) % 10) + ((i / 1000) % 10);
			if (res <= 10000) {
				arr[res] = 1;
			}
		}
	}
	for (i = 1; i < 10000; i++) {
		if (arr[i] != 1) {
			printf("%d\n", i);
		}
	}

}