function letterCombinations (digits) {
    const result = [];
    
    if (!digits || !digits.length) {
        return result;        
    }
    
    const mapping = [
        "0",
        "1",
        "abc",
        "def",
        "ghi",
        "jkl",
        "mno",
        "pqrs",
        "tuv",
        "wxyz"
    ];
    
    letterCombinationsRecursive(result, digits, "", 0, mapping);
    
    return result;        
};

function letterCombinationsRecursive(result, digits, current, index, mapping) {
    if (index === digits.length) {
        result.push(current);
        return
    }
    
    const digit = digits.charAt(index);    
    const letters = mapping[digit];     
    
    for (let i = 0; i < letters.length; i++) {
        letterCombinationsRecursive(result, digits, current + letters.charAt(i), index + 1, mapping);
    }
        
}

const digits = "23";
const combination = letterCombinations(digits);

console.log(combination);