package leetcode;

import leetcode.interfaces.ITwoSumEasy01;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;


public class TwoSum01 {

    @Test
    public void testSolutions() {
        int[] sums = {2,7,11,15};
        int target = 9;
        int[] expectedAnswer = {0, 1};

        TwoSumEasy01BruceForce twoSumEasy01BruceForce = new TwoSumEasy01BruceForce();
        TwoSumEasy01DP twoSumEasy01DP = new TwoSumEasy01DP();

        assertArrayEquals(twoSumEasy01BruceForce.twoSum(sums, target), expectedAnswer);
//        assertArrayEquals(twoSumEasy01DP.twoSum(sums, target), expectedAnswer);
    }

}
