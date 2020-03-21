<?php

class Solution {

  /**
   * @param Integer $x
   * @return Integer
   */
  function reverse($x) {
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
    if($y > pow(2, 31) - 1 or $y < pow(2, 31) * -1)
    	return 0;
		return $y*$sign;
  }
}

$sample = array(123, -123, 120, 1534236469, 0);
$testSolution = new Solution();
foreach ($sample as &$m) {
	printf("%d => %d\n",$m, $testSolution->reverse($m));
}
?>