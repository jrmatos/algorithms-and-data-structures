package stack

import (
	"testing"
)

func TestStackPush(t *testing.T) {
	var s Stack

	s.push(1)
	s.push("hello")
	s.push(10.2)
	s.push(false)
	s.push([]interface{}{})

	if s.size() != 5 {
		t.Fatalf("Did not push items correctly")
	}
}


func TestStackPop(t *testing.T) {
	var s Stack

	s.push("hello")

	removedElement, erro := s.pop()

	if erro != nil {
		t.Fatalf("Did not pop item")
	}

	if removedElement != "hello" {
		t.Fatalf("Did not return correct removed item")
	}

	if !s.isEmpty() {
		t.Fatalf("Did not empty stack")
	}
}

func TestStackPopWhenEmpty(t *testing.T) {
	var s Stack

	if _, erro := s.pop(); erro == nil {
		t.Fatalf("Stack should had thrown an error")
	}
}
