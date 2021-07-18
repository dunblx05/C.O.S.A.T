#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

typedef struct {
	char string[51];
	int length;
} str;

void merge(str* arr, int left, int mid, int right);
void merge_sort(str* arr, int left, int right);

str sort[20001];

int main() {
	int n, i, j;
	scanf("%d", &n);
	str a[20001];

	for (i = 0; i < n; i++) {
		scanf("%s", a[i].string);
		a[i].length = strlen(a[i].string);
	}

	merge_sort(a, 0, n - 1);

	for (i = 0; i < n; i++) {
		if (strcmp(a[i].string, a[i + 1].string) != 0) {
			printf("%s\n", a[i].string);
		}
	}

}

void merge(str* arr, int left, int mid, int right) {
	int i = left, j = mid + 1, k = left;
	int l;		//index

	//���� ���ĵ� �迭�� ����
	while (i <= mid && j <= right) {
		if (arr[i].length < arr[j].length) {
			sort[k++] = arr[i++];
		}
		else if (arr[i].length > arr[j].length) {
			sort[k++] = arr[j++];
		}
		else {
			if (strcmp(arr[i].string, arr[j].string) < 0) {
				sort[k++] = arr[i++];
			}
			else {
				sort[k++] = arr[j++];
			}
		}
	}

	//���� ������ ����
	if (i > mid) {
		for (l = j; l <= right; l++) {
			sort[k++] = arr[l];
		}
	}
	else {
		for (l = i; l <= mid; l++) {
			sort[k++] = arr[l];
		}
	}

	//sort�迭�� ������ arr�迭�� ����
	for (l = left; l <= right; l++) {
		arr[l] = sort[l];
	}
}

void merge_sort(str* arr, int left, int right) {	//��������
	int mid;

	if (left < right) {
		mid = (left + right) / 2;			//�߰���ġ ��� �� �迭 ����
		merge_sort(arr, left, mid);			//�迭�� �պκ� ����
		merge_sort(arr, mid + 1, right);	//�迭�� �޺κ� ����
		merge(arr, left, mid, right);		//���ĵ� �迭 ����
	}
}