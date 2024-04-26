def longest_substring(s: str) -> int:
    
    """"
    
    Implement the function longest_substring 
    using the provided longest_substring function to find 
    the length of the longest substring without repeating characters.

    """ 
    pass


function longest_Substring(s) {
    if (!s) return 0;

    let charIndex = {};
    let maxLength = 0;
    let start = 0;

    for (let end = 0; end < s.length; end++) {
        if (s[end] in charIndex && charIndex[s[end]] >= start) {
            start = charIndex[s[end]] + 1;
        } else {
            maxLength = Math.max(maxLength, end - start + 1);
        }
        charIndex[s[end]] = end;
    }

    return maxLength;
}

module.exports = { longest_Substring };

