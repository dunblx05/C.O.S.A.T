#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <assert.h>

int sort[1000001];		//병합정렬은 추가적인 공간 필요

void merge(int arr[], int left, int mid, int right);
void merge_sort(int arr[], int left, int right);
int binary_search(int arr[], int target, int n);
int compact(int *array, int size);

int main() {
	int *cur = malloc(sizeof(int) * 1000001);
	int *cur1 = malloc(sizeof(int) * 1000001);
	int n, i, ans, c_n;
	int count = 0;
	scanf("%d", &n);

	for (i = 0; i < n; i++) {
		scanf("%d", &cur[i]);
		cur1[i] = cur[i];
	}

	merge_sort(cur1, 0, n - 1);

	c_n = compact(cur1, n);

	for (i = 0; i < n; i++) {
		ans = binary_search(cur1, cur[i], c_n);
		printf("%d ", ans);
	}

	free(cur);
	free(cur1);

}

void merge(int arr[], int left, int mid, int right) {
	int i = left, j = mid + 1, k = left;
	int l;		//index

	//분할 정렬된 배열의 병합
	while (i <= mid && j <= right) {
		if (arr[i] < arr[j]) {
			sort[k++] = arr[i++];
		}
		else {
			sort[k++] = arr[j++];
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

void merge_sort(int arr[], int left, int right) {	//병합정렬
	int mid;

	if (left < right) {
		mid = (left + right) / 2;			//중간위치 계산 후 배열 분할
		merge_sort(arr, left, mid);			//배열의 앞부분 정렬
		merge_sort(arr, mid + 1, right);	//배열의 뒷부분 정렬
		merge(arr, left, mid, right);		//정렬된 배열 병합
	}
}

int binary_search(int arr[], int target, int n) {
	int low = 0;
	int high = n - 1;
	int mid;

	while (low <= high) {
		mid = (low + high) / 2;
		if (arr[mid] == target) {
			return mid;
		}
		else if (arr[mid] > target) {
			high = mid - 1;
		}
		else
			low = mid + 1;
	}
	return -1;
}

int compact(int *array, int size) {
	int i;
	int last = 0;
	assert(size >= 0);
	if (size <= 0) {
		return size;
	}
	for (i = 1; i < size; i++) {
		if (array[i] != array[last])
			array[++last] = array[i];
	}
	return (last + 1);
}