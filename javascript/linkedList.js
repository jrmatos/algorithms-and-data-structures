import { defaultEquals } from './utils';

class Node {
    constructor(element) {
        this.element = element;
        this.next = undefined;
    }
}

export default class LinkedList {
    constructor(equalsFn = defaultEquals) {
        this.count = 0;
        this.head = undefined;
        this.equalsFn = equalsFn;
    }

    push(element) {
        const node = new Node(element);
        let current = this.head;

        if (this.head == null) {
            this.head = node;
        } else {
            current = this.head;

            while (current.next != null) { // get the last node
                current = current.next;
            }

            current.next = node; // create connection with new node
        }

        this.count++;
    }

    removeAt(index) {
        if (index >= 0 && index < this.count) {
            let current = this.head;

            if (index === 0) {
                this.head = current.next;
            } else {
                const previous = this.getElementAt(index - 1);
                current = previous.next;
                // skip current in the list
                previous.next = current.next;
            }
        
            this.count--;
            return current.element;
        }

        return undefined;
    }

    getElementAt(index) {
        if (this.isValidIndex(index)) {
            let node = this.head;

            for (let i = 0; i < index && node != null; i++) {
                node = node.next;
            }

            return node;
        }
        return undefined;
    }

    insert(element, index) {
        if (this.isValidIndex(index)) {
            const node = new Node(element);

            if (index === 0) {
                const current = this.head;
                node.next = current;
                this.head = node;
            } else {
                const previous = this.getElementAt(index - 1);
                const current = previous.next;
                previous.next = node;
                node.next = current;
            }

            this.count++;
            return true;
        }

        return false;
    }

    indexOf(element) {
        let current = this.head;

        for (let i = 0; i < this.count && current != null; i++) {
            if (this.equalsFn(element, current.element)) {
                return i;
            }

            current = current.next;
        }

        return -1;
    }

    remove(element) {
        const index = this.indexOf(element);
        return this.removeAt(index);
    }

    size() {
        return this.count;
    }

    isEmpty() {
        return this.size() === 0;
    }

    getHead() {
        return this.head;
    }

    isValidIndex(index) {
        return index >= 0 && index <= this.count;
    }
}