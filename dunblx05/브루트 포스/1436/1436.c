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
		int temp = num;				//�ӽ÷� ������
		while (temp != 0) {			//������ ���� 0�̵ɶ�����
			if (temp % 1000 == 666) {	//���� 6�� �����Ͽ� 3�� ������
				cnt++;					//Ƚ�� ����
				break;
			}
			else
				temp = temp / 10;		//�ƴ� ��� 1�ڸ��� �����
		}
	}
	printf("%d", num);

}