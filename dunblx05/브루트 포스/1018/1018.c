#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
	int n, m, i, j;
	char chess[51][51];
	int count = 0;
	scanf("%d %d", &n, &m);
	for (i = 0; i < n; i++) {	//행의 상태가 주어지기 때문에 문자열형식으로 입력
		scanf("%s", chess[i]);
	}
	int min = 64;
	for (i = 0; i < n - 7; i++) {
		for (j = 0; j < m - 7; j++) {
			for (int a = i; a < i + 8; a++) {
				for (int b = j; b < j + 8; b++) {
					if ((a + b) % 2 == 1) {			//행과 열합이 홀수일때
						if (chess[a][b] == 'W') {
							count++;
						}
					}
					else if ((a + b) % 2 == 0) {	//행과 열합이 짝수일때
						if (chess[a][b] == 'B') {
							count++;
						}
					}
				}
			}
			if (count > 32) {						//절반을 칠하는 경우보다 많은 경우
				count = 64 - count;					
			}
			if (min > count) {
				min = count;
			}
			count = 0;
		}
	}
	printf("%d", min);
}