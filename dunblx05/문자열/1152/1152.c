#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(){
	char str[1000001];
	int count = 0;
	gets(str);

	char *ptr = strtok(str, " ");
	while (ptr != NULL) {
		ptr = strtok(NULL, " ");
		count++;
	}
	printf("%d", count);
	return 0;
}