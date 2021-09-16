let recursionCounter = 0;

const parenthesesMap = {
    0: '(',
    1: ')'
}

function generateParenthesis(n) {
    const result = [];
    
    let combiningString = '';
    const internalParenthesesAmount = (n * 2) - 2;
    let index = 0;
    
    backtracking(result, combiningString, internalParenthesesAmount, index);
    
    return result;
};

function backtracking(result, combiningString, internalParenthesesAmount, index) {
    recursionCounter++;

    if (index === internalParenthesesAmount) { // stop recursion
        const fullParenthesesString = `(${combiningString})`; // leaf 

        if (isParenthesesStringValid(fullParenthesesString)) {
            result.push(fullParenthesesString);
        }
        
        return;
    }
    
    for (let i = 0; i <= 1; i++) {
        backtracking(result, combiningString + parenthesesMap[i], internalParenthesesAmount, index+1);
    }   
    
}

function isParenthesesStringValid(parenthesesString) {
    let openedParenthesesCount = 0;
    
    for (let parenthesis of parenthesesString) {
        
        if (parenthesis === parenthesesMap[0]) {
            openedParenthesesCount++;
        } else if (parenthesis === parenthesesMap[1]) {
            openedParenthesesCount--;
            
            if (openedParenthesesCount < 0) {
                return false;
            }
        } else {
            return false;
        }  
    }
    
    return openedParenthesesCount === 0;    
}
