// https://leetcode.com/problems/add-two-promises/?envType=study-plan-v2&envId=30-days-of-javascript

/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {

    let sum = 0;
    function onDone(data) {
    sum += data;
    }

    await promise1.then(onDone);
    await promise2.then(onDone);

    return sum;
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */