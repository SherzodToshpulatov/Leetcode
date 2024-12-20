// https://leetcode.com/problems/memoize/description/?envType=study-plan-v2&envId=30-days-of-javascript

/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const cache = {};
    return function(...args) {
        const key = args.join(",");
        if(cache.hasOwnProperty(key)){
            return cache[key]
        }
        else {
            cache[key] = fn(...args);
            return cache[key];
        };

    }
}


/**
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1
 */