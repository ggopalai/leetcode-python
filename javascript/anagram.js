/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    const arr = Array(26).fill(0);
    const ref = Array(26).fill(0);
    
    for (const i of s) {
        arr[i.charCodeAt(0) - 97] += 1
    }
    
    for (const i of t) {
        ref[i.charCodeAt(0) - 97] += 1
    }
    
    return JSON.stringify(arr) === JSON.stringify(ref)
};