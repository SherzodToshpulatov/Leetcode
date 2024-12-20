// https://leetcode.com/problems/apply-transform-over-each-element-in-array/description/?envType=study-plan-v2&envId=30-days-of-javascript

/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const newArr = [];
    for(let i = 0; i < arr.length; i++)
    {
        newArr.push(fn(arr[i], i));
    };
    return newArr;
};