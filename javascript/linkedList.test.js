import LinkedList from './linkedList';

describe('LinkedList', () => {
    let linkedList;

    beforeEach(() => {
        linkedList = new LinkedList();
    });

    test("should push element", () => {
        linkedList.push(1);
        linkedList.push(7);

        expect(linkedList.head.element).toBe(1);
        expect(linkedList.head.next.element).toBe(7);
    });

    test("should remove at first position", () => {
        linkedList.push(1);
        linkedList.removeAt(0);

        expect(linkedList.head).toBe(undefined);
    });

    test("should remove at position", () => {
        linkedList.push(1);
        linkedList.push(7);
        linkedList.removeAt(1);

        expect(linkedList.head.element).toBe(1);
        expect(linkedList.head.next).toBe(undefined);
        expect(linkedList.count).toBe(1);
    });
});