<?php

class Solution {

  /**
   * @param Integer $x
   * @return Integer
   */
  function reverse($x) {
  	$INT_MAX = (1<<31)-1;
  	$INT_MIN = -1<<31;
  	
  	$sign = 1;
  	if($x < 0) {
  		$sign = -1;
  		$x *= -1;
  	}
  	$y = 0;
  	while((int)$x > 0) {
  		if($y > 0) {
  			$y *= 10;
  		}
  		$y += $x % 10;
  		$x = (int)($x / 10);
  	}
  	$y *= $sign;
  	if($y > (int)$INT_MAX or $y < (int)$INT_MIN)
    	return 0;
		return $y;
  }
}

$sample = array(123, -123, 120, 1534236469, 0, -2147483412);
$testSolution = new Solution();
foreach ($sample as &$m) {
	printf("%d => %d\n",$m, $testSolution->reverse($m));
}
?>