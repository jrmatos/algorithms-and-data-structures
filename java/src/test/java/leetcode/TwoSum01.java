package leetcode;

import leetcode.interfaces.ITwoSumEasy01;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;


public class TwoSum01 {

    @Test
    public void bruteForce() {
        ITwoSumEasy01 twoSumEasy01BruceForce = new TwoSumEasy01BruceForce();

        int[] sums = {2,7,11,15};
        int target = 9;
        int[] expectedAnswer = {0, 1};

        int[] answer = twoSumEasy01BruceForce.twoSum(sums, target);

        assertArrayEquals(answer, expectedAnswer);
    }

}
