#include<stdio.h>
#include<stdlib.h>

int reverse(int x){

	int sign = 1;
	if(x < 0) {
		sign = -1;
		int INT_MIN = (-1)<<31;
		if(x == INT_MIN) return 0;
		x *= -1;
	}
	long long y = 0;
	while(x) {
		if(y > 0) y *= 10;
		y += x % 10;
		x /= 10;
	}
	if(y > 0x7FFFFFFF) return 0;
	return (int)y*sign;
}

int main(int argc, char *argv[]) {

  int sample[] = {123, -123, 120, 1534236469, 0, -2147483412, -2147483648};
  for(int i=0; i<sizeof(sample)/sizeof(int); i++) {
		printf("%d => %d\n", sample[i], reverse(sample[i]));
	}
}