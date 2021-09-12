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
        if (index >= 0 && index <= this.count) {
            let node = this.head;

            for (let i = 0; i < index && node != null; i++) {
                node = node.next;
            }

            return node;
        }
        return undefined;
    }
}