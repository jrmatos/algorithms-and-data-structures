package leetcode;

import leetcode.interfaces.ITwoSumEasy01;

import java.util.HashMap;
import java.util.Map;

public class TwoSumEasy01DP implements ITwoSumEasy01 {
    // O(n)
    @Override
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> previous = new HashMap<>();
        int[] answer = new int[2];

        for (int i = 0; i < nums.length; i++) {
            int current = nums[i];
            int key = target - current;

            if (previous.containsKey(key)) {
                answer[0] = previous.get(key);
                answer[1] = i;

                return answer;
            }

            previous.put(current, i);
        }

        return answer;
    }
}
