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
                let previous;

                for (let i = 0; i < index; i++) {
                    previous = current;
                    current = current.next;
                }

                // skip current in the list
                previous.next = current.next;
            }
        
            this.count--;
            return current.element;
        }

        return undefined;
    }
}