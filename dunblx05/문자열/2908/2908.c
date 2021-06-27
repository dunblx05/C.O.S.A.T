#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(){
	int a, b;
	int a1, a2, a3, a4;
	int b1, b2, b3, b4;
	scanf("%d %d", &a, &b);

	a1 = a % 10;
	a2 = (a / 10) % 10;
	a3 = (a / 100) % 10;
	a4 = a1 * 100 + a2 * 10 + a3;
	
	b1 = b % 10;
	b2 = (b / 10) % 10;
	b3 = (b / 100) % 10;
	b4 = b1 * 100 + b2 * 10 + b3;

	if (a4 > b4) {
		printf("%d", a4);
	}
	else
		printf("%d", b4);
}