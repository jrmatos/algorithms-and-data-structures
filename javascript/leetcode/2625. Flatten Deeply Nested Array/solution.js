/**
 * @param {any[]} arr
 * @param {number} depth
 * @return {any[]}
 */
var flat = function (arr, n) {
    if (n == 0) {
        return arr;
    }

    const newArray = [];

    for (let i = 0; i < arr.length; i++) {
        if (Array.isArray(arr[i])) {
            const flattenElements = flat(arr[i], n - 1)
            for (let j = 0; j < flattenElements.length; j++) {
                newArray.push(flattenElements[j])
            }
        } else {
            newArray.push(arr[i])
        }
    }

    return newArray;
};