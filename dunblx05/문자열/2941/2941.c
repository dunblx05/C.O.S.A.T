#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main() {
	char word[101];
	scanf("%s", word);
	int count = 0;
	int len = strlen(word);
	for (int i = 0; i < len; i++) {
		if (word[i] == 'c') {
			if (word[i + 1] == '=' || word[i + 1] == '-') {
				count++;
				i++;
			}
			else
				count++;
		}
		else if (word[i] == 'd') {
			if (word[i + 1] == 'z' && word[i + 2] == '=') {
				count++;
				i = i + 2;
			}
			else if (word[i + 1] == '-') {
				count++;
				i++;
			}
			else
				count++;
		}
		else if (word[i] == 'l' || word[i] == 'n') {
			if (word[i + 1] == 'j') {
				count++;
				i++;
			}
			else
				count++;
		}
		else if (word[i] == 's' || word[i] == 'z') {
			if (word[i + 1] == '=') {
				count++;
				i++;
			}
			else
				count++;
		}
		else if (word[i] != 'c' || word[i] != 'd' || word[i] != 'l' || word[i] != 'n' || word[i] != 's' || word[i] != 'z') {
			count++;
		}
	}
	printf("%d", count);
	return 0;
}