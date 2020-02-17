import java.util.HashMap;

class Solution {
    public static void twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> indexMap = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            System.out.println(nums[i]);
        }
        
    }

    public static void main(String[] args) {
        int[] nums = {1,2,7,11};
        int target = 13;
        twoSum(nums, target);
        // System.out.println(indexList);
    }
}