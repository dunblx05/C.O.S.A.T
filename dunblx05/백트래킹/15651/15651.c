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

void backtracking(int a, int b, int k) {	//backtracking -> 1���� a������ �ڿ������� ���̰� b�� ������ �ߺ����� ���� ���, k���� ���� ���õǾ���.
	if (k == b) {
		for (int i = 0; i < b; i++) {
			printf("%d ", arr[i]);
		}
		printf("\n");
		return;
	}

	for (int i = 1; i <= a; i++) {
		if (!visited[i]) {
			arr[k] = i;
			//visited[i] = true;
			backtracking(a, b, k + 1);
			visited[i] = false;
		}
	}
}