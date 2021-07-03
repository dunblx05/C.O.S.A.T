#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

void reverse(char *arr, int len);

int main() {
	char a[10002] = { '0' }, b[10002] = { '0' };
	int sum[10003] = { 0 };
	int a_len, b_len, sum_len;
	int carry = 0;
	scanf("%s %s", a, b);

	a_len = strlen(a);
	b_len = strlen(b);

	if (a_len >= b_len) {
		sum_len = a_len;
	}
	else {
		sum_len = b_len;
	}

	reverse(a, a_len);
	reverse(b, b_len);

	for (int i = 0; i <= sum_len; i++) {
		if (a[i] - '0' < 0 || b[i] - '0' < 0) {
			if (a[i] - '0' < 0 && b[i] - '0' < 0) {
				sum[i] = carry;
			}
			else if (b[i] - '0' < 0) {
				sum[i] = a[i] - '0' + carry;
			}
			else if (a[i] - '0' < 0) {
				sum[i] = b[i] - '0' + carry;
			}
		}
		else {
			sum[i] = (a[i] - '0') + (b[i] - '0') + carry;
		}
		if (sum[i] >= 10) {
			carry = 1;
			sum[i] = sum[i] - 10;
		}
		else
			carry = 0;
	}
	if (sum[sum_len] == 0) {
		for (int i = sum_len - 1; i >= 0; i--) {
			printf("%d", sum[i]);
		}
	}
	else
		for (int i = sum_len; i >= 0; i--) {
			printf("%d", sum[i]);
		}
}

void reverse(char *arr, int len) {
	int i;
	int left = 0, right = len - 1;
	char temp;
	for (i = 0; i < len / 2; i++) {
		temp = arr[left];
		arr[left] = arr[right];
		arr[right] = temp;
		left++;
		right--;
	}
}