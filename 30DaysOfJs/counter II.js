// https://leetcode.com/problems/counter-ii/description/?envType=study-plan-v2&envId=30-days-of-javascript

/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let object = {
        increment: function(arg) {
            return arg ++

        },
        decrement: function(arg) {
            return arg --
        },

        reset: function(arg) {
            return arg
        }
    };
    return object
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */
