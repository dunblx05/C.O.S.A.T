#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(){
	char word[15];
	scanf("%s", word);
	int len = strlen(word);
	int i;
	int num[15] = { 0 };
	int sum = 0;
	for (i = 0; i < len; i++) {
		if (word[i] >= 65 && word[i] <= 67) {
			num[i] = 3;
		}
		if (word[i] >= 68 && word[i] <= 70) {
			num[i] = 4;
		}
		if (word[i] >= 71 && word[i] <= 73) {
			num[i] = 5;
		}
		if (word[i] >= 74 && word[i] <= 76) {
			num[i] = 6;
		}
		if (word[i] >= 77 && word[i] <= 79) {
			num[i] = 7;
		}
		if (word[i] >= 80 && word[i] <= 83) {
			num[i] = 8;
		}
		if (word[i] >= 84 && word[i] <= 86) {
			num[i] = 9;
		}
		if (word[i] >= 87 && word[i] <= 90) {
			num[i] = 10;
		}
		sum = sum + num[i];
	}
	printf("%d", sum);
}