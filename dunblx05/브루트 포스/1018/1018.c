#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
	int n, m, i, j;
	char chess[51][51];
	int count = 0;
	scanf("%d %d", &n, &m);
	for (i = 0; i < n; i++) {	//���� ���°� �־����� ������ ���ڿ��������� �Է�
		scanf("%s", chess[i]);
	}
	int min = 64;
	for (i = 0; i < n - 7; i++) {
		for (j = 0; j < m - 7; j++) {
			for (int a = i; a < i + 8; a++) {
				for (int b = j; b < j + 8; b++) {
					if ((a + b) % 2 == 1) {			//��� ������ Ȧ���϶�
						if (chess[a][b] == 'W') {
							count++;
						}
					}
					else if ((a + b) % 2 == 0) {	//��� ������ ¦���϶�
						if (chess[a][b] == 'B') {
							count++;
						}
					}
				}
			}
			if (count > 32) {						//������ ĥ�ϴ� ��캸�� ���� ���
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