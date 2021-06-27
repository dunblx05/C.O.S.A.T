#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	char word[1000001];
	int a[27] = { 0 };
	int i, j;
	int max = 0;
	int count = 0;

	scanf("%s", word);

	int len = strlen(word);
	for (i = 0; i < len; i++) {
		if (word[i] >= 97) {
			word[i] = word[i] - 32;
		}
		a[word[i] - 65]++;
	}

	for (i = 0; i < 26; i++) {
		if (max < a[i]) {
			max = a[i];
			count = i;
		}
		else if (max == a[i] && a[i] != 0) {
			count = -1;
		}
	}
	if (count != -1) {
		printf("%c", count + 65);
	}
	else
		printf("?");
}