// g++ -std=c++11 index.cpp;./a.exe
#include <iostream>
#include <string>
#include <math.h>
using namespace std;

class Solution {
public:
  int reverse(int x) {
  	int sign = 1;
  	if(x < 0) {
  		sign = -1;
  		if(x == INT_MIN) return 0;
  		x *= -1;
  	}
  	long long int y = 0;
  	while(x > 0) {
  		if(y > 0) y *= 10;
  		y += x % 10;
  		x /= 10;
    }
    if(y > 0x7FFFFFFF) return 0;
    return y*sign;
  }
};

int main(int argc, char *argv[]) {
	int sample [] = {123, -123, 120, 1534236469, 0, -2147483412, -2147483648};

	Solution mySolution;
	for (int m : sample) {
		cout << m << " => " << mySolution.reverse(m) << endl;
	}
}