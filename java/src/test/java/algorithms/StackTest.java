package algorithms;

import algorithms.interfaces.IStack;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;


public class StackTest {
    @Test
    public void testPush() {
        IStack<Integer> stack = new Stack<>();

        stack.push(1);
        stack.push(100);

        assertEquals(stack.size(), 2);
    }

    @Test
    public void testPop() {
        IStack<Integer> stack = new Stack<>();

        stack.push(1);
        stack.push(100);
        stack.push(1000);

        assertEquals(stack.size(), 3);

        stack.pop();
        stack.pop();

        assertEquals(stack.size(), 1);
    }

    @Test
    public void testPeek() {
        IStack<Integer> stack = new Stack<>();

        stack.push(1);
        stack.push(100);
        stack.push(777);

        assertEquals(stack.peek(), 777);
    }

    @Test
    public void testSize() {
        IStack<Integer> stack = new Stack<>();

        stack.push(1);
        stack.push(100);
        stack.push(1000);
        stack.push(1000);
        stack.push(1000);

        assertEquals(stack.size(), 5);
    }

    @Test
    void isEmpty() {
        IStack<Integer> stack = new Stack<>();

        assertEquals(stack.isEmpty(), true);
        stack.push(1);
        assertEquals(stack.isEmpty(), false);
        stack.pop();
        assertEquals(stack.isEmpty(), true);
    }
}