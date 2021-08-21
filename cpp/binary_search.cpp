#include <iostream>
#include <vector>

// O(n)
void print_numbers(std::vector<int> list) {
  for (int n : list) {
    std::cout << n << " ";
  }

  std::cout << std::endl;
}

// O(logn)
int binary_search(std::vector<int> list, int search) {
  int bottom = 0;
  int top = list.size() - 1;
  int middle, guess;

  while (bottom <= top) {
    middle = (bottom + top) / 2;

    guess = list[middle];

    if (guess == search) {
      return middle;
    }

    if (guess > search) {
      top = middle - 1;
    } else {
      bottom = middle + 1;
    }
  }

  return -1;
}

int main() {
  std::vector<int> numbers = {3, 7, 10, 25, 50, 123, 500};
  int search;

  std::cout << "Numbers: " << std::endl;
  print_numbers(numbers);
  std::cout << "Find number: ";
  std::cin >> search;
  std::cout << "Result: " << binary_search(numbers, search) << std::endl;

  return 0;
}
