#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main() {
	int n;
	int i = 0;
	int stage = 0;
	int up = 0, down = 0;
	int diff;
	scanf("%d", &n);
	while (n > i) {
		i = i + stage;
		stage++;
	}
	diff = i - n;
	if (stage % 2 == 1) {
		up = stage - diff - 1;
		down = diff + 1;
	}
	else if (stage % 2 == 0) {
		up = diff + 1;
		down = stage - diff - 1;
	}
	printf("%d/%d", up, down);
}