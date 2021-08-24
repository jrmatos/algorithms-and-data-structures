const Stack = require('./stack.js');

describe("Stack", () => {
    let stack;

    beforeEach(() => {
        stack = new Stack();
    });

    test("should push items", () => {
        stack.push(1);
        stack.push(2);
        stack.push(3);
        stack.push(5);

        expect(stack.size()).toBe(4);
    });

    test("should pop items", () => {
        stack.push(1);
        stack.push(5);
        stack.push(5);
        stack.push(100);

        const removedElement = stack.pop();

        expect(stack.size()).toBe(3);
        expect(removedElement).toBe(100);
    });

    test("should peek", () => {
        stack.push(1);
        stack.push(20);
        stack.push(30);

        const expectedElement = 30;

        const element = stack.peek();

        expect(element).toBe(expectedElement);
    });

    test("should not pop empty stack", () => {
        const wrapper = () => {
            stack.pop();
        }

        expect(wrapper).toThrow('Stack is empty');
    });

    test("should not peek empty stack", () => {
        const wrapper = () => {
            stack.peek();
        }

        expect(wrapper).toThrow('Stack is empty');
    });
});