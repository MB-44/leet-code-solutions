function isAcronymTs(words: string[], s: string ): boolean {
    let firstLetters = "";
    
    for (let i = 0; i < words.length; i++) {
        firstLetters += words[i][0];
    }

    return firstLetters == s;


};