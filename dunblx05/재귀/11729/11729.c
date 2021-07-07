#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void hanoi(int a, int b, int c, int n);

int main() {
	int n;
	scanf("%d", &n);
	printf("%d\n", (int) pow(2, n) - 1);	//하노이탑의 이동횟수는 2^n-1
	hanoi(1, 2, 3, n);
}

void hanoi(int a, int b, int c, int n) {//시작 기둥, 거쳐가는 기둥, 도착 기둥, 원판 갯수
	if (n <= 0) {
		return 1;
	}
	hanoi(a, c, b, n - 1);
	printf("%d %d\n", a, c);
	hanoi(b, a, c, n - 1);
}