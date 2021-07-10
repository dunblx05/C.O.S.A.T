1018
===========
#입력

    for (i = 0; i < n; i++) {
            scanf("%s", chess[i]);
        }
입력 받을 때 행단위로 입력 받음

#구현

    for (i = 0; i < n - 7; i++) {
            for (j = 0; j < m - 7; j++) {
                for (int a = i; a < i + 8; a++) {
                    for (int b = j; b < j + 8; b++) {
                        if ((a + b) % 2 == 1) {			//행과 열합이 홀수일때
                            if (chess[a][b] == 'W') {
                                count++;
                            }
                        }
                        else if ((a + b) % 2 == 0) {	//행과 열합이 짝수일때
                            if (chess[a][b] == 'B') {
                                count++;
                            }
                        }
                    }
                }
                if (count > 32) {						//절반을 칠하는 경우보다 많은 경우
                    count = 64 - count;					
                }
                if (min > count) {
                    min = count;
                }
                count = 0;
            }
        }
풀때 나는 첫 번째 칸이 W일 때를 기준으로 삼아서 count를 증가 시킴, 만약 count가 32보다 커질 경우 첫번째 칸이 B일 때를 기준으로 푸는 것이 최소값이 작으므로 64 - count를 하여 빠르게 계산

#규칙

![규칙](https://blog.kakaocdn.net/dn/beAKu8/btqBkORtKw4/5XW4Fq7PtqDSoP2seGt3Ck/img.png)
