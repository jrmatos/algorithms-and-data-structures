class Stack {
    elements = []

    push(element) {
        this.elements.push(element);
    }

    pop() {
        if (this.size()) {
            return this.elements.pop();
        }

        throw new Error("Stack is empty");
    }

    peek() {
        if (this.size()) {
            return this.elements[this.size() - 1];
        }

        throw new Error("Stack is empty");
    }

    size() {
        return this.elements.length;
    }
}

module.exports = Stack;