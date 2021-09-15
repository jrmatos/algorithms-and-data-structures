/**
 * @param {number[]} arr
 * @return {number}
 */
 var maxTurbulenceSize = function(arr) {
    const GREATER_THAN_SIGN = '>';
    const LESS_THAN_SIGN = '<';
    let lastSign = 0;
    let maxTurbulenceSize = 1;
    let currentTurbulenceSize = 1;
        
    for (let i = 1; i < arr.length; i++) {    
        let isEqual = arr[i] === arr[i - 1];
        let isGreaterThanLastItem = arr[i - 1] > arr[i];
        let currentSign = isGreaterThanLastItem ? GREATER_THAN_SIGN : LESS_THAN_SIGN;
 
        if (isEqual) {
             if (currentTurbulenceSize >= maxTurbulenceSize) {
                 maxTurbulenceSize = currentTurbulenceSize;
             }
 
             currentTurbulenceSize = 1;
             continue;
        }
        
        if (lastSign && currentSign == lastSign) {
             // same sign or is first comparison   
            if (currentTurbulenceSize > maxTurbulenceSize) {
                maxTurbulenceSize = currentTurbulenceSize;
            }
 
            currentTurbulenceSize = 2;
        } else {
             // changed sign
             currentTurbulenceSize++;    
        }
 
        lastSign = currentSign;
    }
    
    return maxTurbulenceSize > currentTurbulenceSize ? maxTurbulenceSize : currentTurbulenceSize;
};

// const input = [9,4,2,10,7,8,8,1,9];
// const input = [4,8,12,16];
// const input = [2,0,2,4,2,5,0,1,2,3];
// const input = [0,1,1,0,1,0,1,1,0,0];
// const input = [8,8,9,10,6,8,2,4,2,2,10,6,6,10,10,2,3,5,1,2,10,4,2,0,9,4,9,3,0,6,3,2,3,10,10,6,4,6,4,4,2,5,1,4,1,1,9,8,9,5,3,5,5,4,5,5,6,5,3,3,7,2,0,10,9,7,7,3,5,1,0,9,6,3,1,3,4,4,3,6,3,2,1,4,10,2,3,4,4,3,6,7,6,2,1,7,0,6,8,10];
// const input = [0,1,1,0,1,0,1,1,0,0];
const input = [0,8,45,88,48,68,28,55,17,24];

const result = maxTurbulenceSize(input);

console.log('result =>', result);