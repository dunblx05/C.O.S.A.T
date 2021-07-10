#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
	int n;
	int cnt = 0, num = 0;
	scanf("%d", &n);

	while (cnt != n) {
		num++;
		int temp = num;				//임시로 값저장
		while (temp != 0) {			//저장한 값이 0이될때까지
			if (temp % 1000 == 666) {	//만약 6이 연속하여 3번 나오면
				cnt++;					//횟수 증가
				break;
			}
			else
				temp = temp / 10;		//아닐 경우 1자리씩 지우기
		}
	}
	printf("%d", num);

}