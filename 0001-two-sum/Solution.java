import java.util.Arrays;
import java.util.HashMap;

class Solution {
    public static int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> complementMap = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (complementMap.containsKey(nums[i])){
                return new int[] {complementMap.get(nums[i]), i};
            } else {
                complementMap.put(target - nums[i], i);
            }
        }
        return new int[] {};
    }

    public static void main(String[] args) {
        int[] nums = {1,2,7,13};
        int target = 4;
        int[] res = twoSum(nums, target);
        System.out.println(Arrays.toString(res));
    }
}