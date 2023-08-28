import random

# Set the parameters
output_filename = 'input.txt'
num_integers = 1000  # Number of integers you want to generate
min_value = 1       # Minimum value for the integers
max_value = 1000    # Maximum value for the integers

average = [0,1,5,8,7,2,3,9,6,4]
worst = [9,8,7,6,5,4,3,2,1,0]
best = [0,1,2,3,4,5,6,7,8,9]

def generate_input_file(filename, num_integers, min_value, max_value):
    with open(filename, 'w') as file:
        for _ in range(num_integers):
            random_integer = random.randint(min_value, max_value)
            file.write(str(random_integer) + '\n')

def load_integers_from_file(filename):
    integers = []
    with open(filename, 'r') as file:
        for line in file:
            integers.append(int(line.strip()))
    return integers

if __name__ == "__main__":
    # Generate the input file
    generate_input_file(output_filename, num_integers, min_value, max_value)
    print(f"{num_integers} integers generated and saved to '{output_filename}'.")
