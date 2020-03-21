/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
	var sign = 1;
	if(x < 0) {
		sign = -1;
		x *= -1;
	}
	var y = 0;
	while(parseInt(x) > 0) {
		if(y > 0) {
			y *= 10;
		}
		y += parseInt(x % 10);
		x /= 10;
	}
  //if(y > Math.pow(2, 31) - 1 || y < Math.pow(2, 31) * -1)
  if(y > 0x7FFFFFFF) return 0;
	return y*sign;
};

var sample = [123, -123, 120, 1534236469, 0, -2147483412];
sample.forEach(function (m) {
	console.log(m, reverse(m));
});
