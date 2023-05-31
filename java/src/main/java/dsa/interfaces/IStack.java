package dsa.interfaces;

public interface IStack<E> {
    void push(E element);
    void pop();
    E peek();
    Integer size();
    Boolean isEmpty();
}
