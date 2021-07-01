#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main() {
	int n, i, j;
	int count = 0;
	char word[101];
	scanf("%d", &n);
	int group = n;
	for (i = 0; i < n; i++) {
		scanf("%s", word);
		int len = 0;
		len = strlen(word);
		int alpha[26] = { 0, };
		for (j = 0; j < len; j++) {
			if (alpha[word[j] - 97] == 0) {
				alpha[word[j] - 97]++;
			}
			else if (alpha[word[j] - 97] != 0) {
				if (word[j] != word[j - 1]) {
					alpha[word[j] - 97]++;
				}
				else
					alpha[word[j] - 97] == 1;
			}
		}
		
		for (j = 0; j < 26; j++) {
			if (alpha[j] >= 2) {
				count++;
			}
		}
		if (count >= 1) {
			group--;
		}
		count = 0;
		
	}
	printf("%d", group);
}