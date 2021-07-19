#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <stdbool.h>

void backtracking(int a, int b, int k);

int arr[10];
bool visited[10];

int main() {
	int n, m;
	scanf("%d %d", &n, &m);
	backtracking(n, m, 0);
}

void backtracking(int a, int b, int k) {	//backtracking -> 1부터 a까지의 자연수에서 길이가 b인 수열을 중복없이 고르는 경우, k개의 수가 선택되었다.
	if (k == b) {
		int count = 0;
		for (int i = 0; i < b; i++) {
			if (arr[i] > arr[i - 1]) {	//수열이 오름차순인지 검사
				count++;
			}
			else
				count = count;
		}
		if (count == b) {				//오름차순이라면 출력
			for (int i = 0; i < b; i++) {
				printf("%d ", arr[i]);
			}
			printf("\n");
		}
		return;
	}

	for (int i = 1; i <= a; i++) {
		if (!visited[i]) {
			arr[k] = i;
			visited[i] = true;
			backtracking(a, b, k + 1);
			visited[i] = false;
		}
	}
}