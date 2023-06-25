/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    
    if (nums.length === 1) {
        return nums[0]
    }
    
    let cur = nums[0];
    let max = cur;
    for (let i = 1; i < nums.length; i++) {
        cur = Math.max(cur + nums[i], nums[i]);
        max = Math.max(cur, max)
    }
      
    return max;
    
};