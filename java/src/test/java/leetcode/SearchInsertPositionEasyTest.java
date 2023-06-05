package leetcode;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class SearchInsertPositionEasyTest {
    @Test
    void testSolution1() {
        int[] nums = { 1,3,5,6 };
        int target = 5;
        int expectedAnswer = 2;

        SearchInsertPositionEasy searchInsertPositionEasy = new SearchInsertPositionEasy();

        Assertions.assertEquals(expectedAnswer, searchInsertPositionEasy.searchInsert(nums, target));
    }

    @Test
    void testSolution2() {
        int[] nums = { 1,3,5,6 };
        int target = 2;
        int expectedAnswer = 1;

        SearchInsertPositionEasy searchInsertPositionEasy = new SearchInsertPositionEasy();

        Assertions.assertEquals(
            expectedAnswer, searchInsertPositionEasy.searchInsert(nums, target)
        );
    }

    @Test
    void testSolution3() {
        int[] nums = { 1,3,5,6 };
        int target = 7;
        int expectedAnswer = 4;

        SearchInsertPositionEasy searchInsertPositionEasy = new SearchInsertPositionEasy();

        Assertions.assertEquals(
                expectedAnswer, searchInsertPositionEasy.searchInsert(nums, target)
        );
    }
}
