/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
  
    function signCheck(num) {
        if (num > 0) {
            return 1;
        }
        else {
            return -1
        }
    }


    
    let sign = signCheck(x);
    let sX = String(Math.abs(x));

    let reverse = "";
    for (let i = sX.length-1; i >=0; i--){
        reverse += sX[i];
    }

    let value = parseInt(reverse) * sign;

    if (Math.abs(value) > (2 ** 31 - 1)) {
        return 0;
    }
    else {
        return value;
    }
};