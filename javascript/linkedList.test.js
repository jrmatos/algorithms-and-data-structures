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

    test("should get node at position", () => {
        linkedList.push(1);
        linkedList.push(7);

        expect(linkedList.getElementAt(0).element).toBe(1);
        expect(linkedList.getElementAt(1).element).toBe(7);
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

    test("should remove at non existing position", () => {
        linkedList.push(1);
        linkedList.push(7);
        const removeAtResult = linkedList.removeAt(10);

        expect(removeAtResult).toBe(undefined);
    });

    test("should insert at first position", () => {
        const insertResult = linkedList.insert(555, 0);

        expect(insertResult).toBe(true);
        expect(linkedList.getElementAt(0).element).toBe(555);
    });

    test("should insert at middle position", () => {
        linkedList.push(1);
        linkedList.push(7);
        linkedList.push(3);
        const insertResult = linkedList.insert(555, 1);

        expect(insertResult).toBe(true);
        expect(linkedList.getElementAt(1).element).toBe(555);
    });

    test("should indexOf existing element", () => {
        linkedList.push(1);
        linkedList.push(7);
        linkedList.push(3);
        const indexOfResult = linkedList.indexOf(7);

        expect(indexOfResult).toBe(1);
    });

    test("should indexOf non existing element", () => {
        linkedList.push(1);
        linkedList.push(7);
        linkedList.push(3);
        const indexOfResult = linkedList.indexOf(999);

        expect(indexOfResult).toBe(-1);
    });

    test("should remove existing element", () => {
        linkedList.push(1);
        linkedList.push(7);

        const removeResult = linkedList.remove(7);

        expect(removeResult).toBe(7)
    });

    test("should calculate size", () => {
        linkedList.push(1);
        linkedList.push(7);
        linkedList.push(9);
        linkedList.push(2);

        expect(linkedList.size()).toBe(4);
    });

    test("should calculate isEmpty ", () => {
        expect(linkedList.isEmpty()).toBe(true);
        linkedList.push(2);
        expect(linkedList.isEmpty()).toBe(false);
    });

    test("should calculate getHead", () => {
        linkedList.push(2);
        expect(linkedList.getHead().element).toBe(2);
    });
});