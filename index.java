import java.lang.*;
import java.util.*;

class Solution {
  public int reverse(int x) {
  	int sign = 1;
  	if(x < 0) {
  		sign = -1;
  		x *= -1;
  	}
  	long y = 0;
  	while(x > 0) {
  		if(y > 0) y *= 10;
  		y += x % 10;
  		x /= 10;
  	}
  	//if(y > Math.pow(2, 31) - 1 || y < Math.pow(2, 31) * -1) return 0;
  	if(y > 0x7FFFFFFF) return 0;
  	return (int)y*sign;
  }
}

public class index {

	public static void main(String[] args) {
		int[] sample = {123, -123, 120, 1534236469, 0, -2147483412};

    Solution demo = new Solution();
    for(int m : sample) {
    	System.out.printf("%d => %d\n", m, demo.reverse(m));
    }
	}
}