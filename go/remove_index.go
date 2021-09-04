package main

import "fmt"

func main() {
	var arr []int = []int{1,5,6,4,2,8,9}

	fmt.Println(remove_index(arr, 2))
}

func remove_index(arr []int, index int) []int {
	var new_arr []int = make([]int, 0)

	for i := 0; i < len(arr); i++ {
		if i != index {
			new_arr = append(new_arr, arr[i])
		}
	}

	return new_arr
}
