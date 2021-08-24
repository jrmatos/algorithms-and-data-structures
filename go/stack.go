package stack

import "errors"


type Stack struct {
	elements []interface{}
}

func (s *Stack) push(element interface{}) {
	s.elements = append(s.elements, element)
}

func (s *Stack) pop() (interface{}, error) {
	topIndex, topElement, erro := s.peek()

	if erro != nil {
		return nil, erro
	}

	s.elements = s.elements[:topIndex]

	return topElement, nil
}

func (s Stack) isEmpty() bool {
	return s.size() == 0
}

func (s Stack) size() int {
	return len(s.elements)
}

func (s Stack) peek() (int, interface{}, error) {
	if s.isEmpty() {
		return 0, nil, errors.New("empty stack")
	}

	lastIndex := s.size() - 1

	return lastIndex, s.elements[lastIndex], nil
}
