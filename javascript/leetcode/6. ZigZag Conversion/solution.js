/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
function convert(s, numRows) {
    const rows = Array.from(new Array(numRows), () => []);
    let counter = 0;
    let incrementing = true;

    // base cases
    if (s.length === 1 || numRows === 1) return s;

    s = s.replace(/,/g, '#');

    // O(n) where n is the s length
    for (let letter of s) {
        rows[counter].push(letter);

        // start to decrement
        if (incrementing && counter === numRows - 1) {
            incrementing = false;
        }

        // start to increment
        if (!incrementing && counter === 0) {
            incrementing = true;
        }

        incrementing ? counter++ : counter--;
    }

    return rows.join().replace(/,/g, '').replace(/#/g, ',');
}

// const result = convert("PAYPALISHIRING", 2);
// const result = convert("Apalindromeisaword,phrase,number,orothersequenceofunitsthatcanbereadthesamewayineitherdirection,withgeneralallowancesforadjustmentstopunctuationandworddividers.", 1);
// console.log(result);
