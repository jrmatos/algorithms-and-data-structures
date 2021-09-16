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
}
