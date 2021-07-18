#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct cursor {
	int x;
	int y;
}cur;

cur sort[100001];

void merge(cur arr[], int left, int mid, int right);
void merge_sort(cur arr[], int left, int right);

int main() {
	int n, i, j;
	cur a[100001];
	scanf("%d", &n);

	for (i = 0; i < n; i++) {
		scanf("%d %d", &a[i].x, &a[i].y);
	}

	merge_sort(a, 0, n - 1);

	for (i = 0; i < n; i++) {
		printf("%d %d\n", a[i].x, a[i].y);
	}
}

void merge(cur arr[], int left, int mid, int right) {
	int i = left, j = mid + 1, k = left;
	int l;		//index

	//분할 정렬된 배열의 병합
	while (i <= mid && j <= right) {
		if (arr[i].x < arr[j].x) {
			sort[k++] = arr[i++];
		}
		else if (arr[i].x > arr[j].x) {
			sort[k++] = arr[j++];
		}
		else {
			if (arr[i].y < arr[j].y) {
				sort[k++] = arr[i++];
			}
			else {
				sort[k++] = arr[j++];
			}
		}
	}

	//남은 값들을 복사
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

	//sort배열의 내용을 arr배열로 복사
	for (l = left; l <= right; l++) {
		arr[l] = sort[l];
	}
}

void merge_sort(cur arr[], int left, int right) {	//병합정렬
	int mid;

	if (left < right) {
		mid = (left + right) / 2;			//중간위치 계산 후 배열 분할
		merge_sort(arr, left, mid);			//배열의 앞부분 정렬
		merge_sort(arr, mid + 1, right);	//배열의 뒷부분 정렬
		merge(arr, left, mid, right);		//정렬된 배열 병합
	}
}