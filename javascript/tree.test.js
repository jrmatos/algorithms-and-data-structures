import BinarySearchTree from './tree';

describe("BinarySearchTree", () => {
    let tree;

    beforeEach(() => {
        tree = new BinarySearchTree();
    });

    test("should in order traverse", () => {
        tree.insert(11);
        tree.insert(3);
        tree.insert(77);
        tree.insert(1);
        tree.insert(500);

        const arr = [];

        const printNode = (value) => arr.push(value);
 
        tree.inOrderTraverse(printNode)
 
        expect(arr).toStrictEqual([1, 3, 11, 77, 500]);
    });

    test("should pre order traverse", () => {
        tree.insert(11);
        tree.insert(3);
        tree.insert(77);
        tree.insert(1);
        tree.insert(500);

        const arr = [];

        const printNode = (value) => arr.push(value);
 
        tree.preOrderTraverse(printNode)
 
        expect(arr).toStrictEqual([11, 3, 1, 77, 500]);
    });

    test("should post order traverse", () => {
        tree.insert(11);
        tree.insert(3);
        tree.insert(77);
        tree.insert(1);
        tree.insert(500);
        tree.insert(4);

        const arr = [];

        const printNode = (value) => arr.push(value);
 
        tree.postOrderTraverse(printNode)
 
        expect(arr).toStrictEqual([1, 4, 3, 500, 77, 11]);
    });

    test("should get min node", () => {
        tree.insert(11);
        tree.insert(3);
        tree.insert(5);

        const minNode = tree.min();
 
        expect(minNode.key).toBe(3);
    });

    test("should get max node", () => {
        tree.insert(11);
        tree.insert(3);
        tree.insert(5);

        const maxNode = tree.max();
 
        expect(maxNode.key).toBe(11);
    });

    test("should search node", () => {
        tree.insert(11);
        tree.insert(5);
        tree.insert(5);
        tree.insert(7);

        expect(tree.search(11)).toBe(true);
        expect(tree.search(5)).toBe(true);
        expect(tree.search(7)).toBe(true);
        expect(tree.search(12)).toBe(false);
        expect(tree.search(15)).toBe(false);
    });


    test("should remove node", () => {
        tree.insert(11);
        tree.insert(5);
        tree.insert(7);
        tree.insert(12);
        tree.insert(15);
        tree.insert(2);
        tree.insert(300);

        tree.remove(5);
        tree.remove(15);
        tree.remove(300);

        expect(tree.search(11)).toBe(true);
        expect(tree.search(5)).toBe(false);
        expect(tree.search(7)).toBe(true);
        expect(tree.search(12)).toBe(true);
        expect(tree.search(15)).toBe(false);
        expect(tree.search(2)).toBe(true);
        expect(tree.search(300)).toBe(false);
    });
});
