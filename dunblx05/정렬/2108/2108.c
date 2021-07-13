#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int sort[500001];

void merge(int arr[], int left, int mid, int right);
void merge_sort(int arr[], int left, int right);

int main() {
	int n;
	int sum = 0;
	int min = 4001, max = -4001;
	int count[8001] = { 0, };
	int freq, freq_n, freq_count = 0, flag = 0, freq_n2 = 0;
	int *a = malloc(sizeof(int) * 500001);
	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		scanf("%d", &a[i]);
		if (min > a[i]) {
			min = a[i];
		}
		if (max < a[i]) {
			max = a[i];
		}
		sum = sum + a[i];
		count[a[i] + 4000]++;
	}
	freq = count[0];

	merge_sort(a, 0, n - 1);

	for (int i = 0; i < 8001; i++) {
		if (freq < count[i]) {
			freq = count[i];
			freq_n = i - 4000;
		}
	}

	for (int i = 0; i < 8001; i++) {
		if (freq == count[i] && count[i] != 0) {
			freq = count[i];
			flag++;
		}
		if (flag == 2) {
			freq_n2 = i - 4000;
			break;
		}
	}
	printf("%.0f\n", (double)sum / n);
	printf("%d\n", a[n / 2]);

	if (flag == 1) {
		printf("%d\n", freq_n);
	}
	else if (flag > 1) {
		printf("%d\n", freq_n2);
	}
	printf("%d", max - min);
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