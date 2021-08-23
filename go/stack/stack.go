package stack

import "errors"


type Stack struct {
	elements []interface{}
}

func (s *Stack) push(element interface{}) {
	s.elements = append(s.elements, element)
}

func (s *Stack) pop() (interface{}, error) {

	if !s.isEmpty() {
		topIndex, topElement := s.getTop()
		s.elements = s.elements[:topIndex]
	
		return topElement, nil
	}

	return nil, errors.New("Stack is empty")
}

func (s Stack) isEmpty() bool {
	return s.size() == 0
}

func (s Stack) size() int {
	return len(s.elements)
}

func (s Stack) getTop() (int, interface{}) {
	lastIndex := s.size() - 1

	return lastIndex, s.elements[lastIndex]
}
