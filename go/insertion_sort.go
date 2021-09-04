package main

import "fmt"

func main() {
	var arr []int = []int{1,5,6,4,2,8,9}

	fmt.Println(insertion_sort(arr))
}

func insertion_sort(arr []int) []int {
	for i := 1; i < len(arr); i++ {
		for j := i; j > 0 && arr[j - 1] > arr[j]; j--  {
			arr[j - 1], arr[j] = arr[j], arr[j - 1]
		}
	}

	return arr
}
