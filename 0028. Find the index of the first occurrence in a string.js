/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    if (haystack.includes(needle)) {
        i = haystack.indexOf(needle);
        return  i;
    }
    else {
        return -1;
    }

};