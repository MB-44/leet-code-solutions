/**
 * @param {string[]} words
 * @param {string} s
 * @return {boolean}
 */
var isAcronym = function(words, s) {
    let firstLetters = "";

    for (let i = 0; i < words.length; i++) {
        firstLetters += words[i][0];
    }

    return firstLetters == s;
};