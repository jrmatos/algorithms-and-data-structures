package main

import "fmt"

func main() {
	var arr []int = []int{1,5,6,4,2,8,9}

	fmt.Println(selection_sort(arr))
}

func selection_sort(arr []int) []int {
	len := len(arr)
    for i := 0; i < len-1; i++ {
        minIndex := i
        for j := i + 1; j < len; j++ {
            if arr[j] < arr[minIndex] {
                arr[j], arr[minIndex] = arr[minIndex], arr[j]
            }
        }
    }

	return arr
}
