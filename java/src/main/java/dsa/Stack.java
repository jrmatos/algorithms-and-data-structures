package dsa;


import dsa.interfaces.IStack;

class StackNode<E> {
    E element;
    StackNode<E> previous;

    StackNode(E element, StackNode<E> previous) {
        this.element = element;
        this.previous = previous;
    }
}

public class Stack<E> implements IStack<E> {
    private StackNode<E> head = null;

    @Override
    public void push(E element) {
        head = new StackNode<>(element, head);
    }

    @Override
    public void pop() {
        if (head != null) {
            head = head.previous;
        }
    }

    @Override
    public E peek() {
        return head.element;
    }

    @Override
    public Integer size() {
        StackNode headAux = head;
        Integer size = 0;

        while (headAux != null) {
            size++;
            headAux = headAux.previous;
        }

        return size;
    }

    @Override
    public Boolean isEmpty() {
        return size() == 0;
    }
}
