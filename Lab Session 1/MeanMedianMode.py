import random

def compute_statistics():
    random_numbers = [random.randint(100, 150) for _ in range(100)]  #generate 100 random numbers between 100 and 150

    #mean
    total_sum = sum(random_numbers)
    count = len(random_numbers)
    mean_value = total_sum / count

    #median
    sorted_numbers = sorted(random_numbers)
    middle_index = count // 2

    #since count is even (100), median is average of two middle values
    median_value = (sorted_numbers[middle_index - 1] + sorted_numbers[middle_index]) / 2

    #mode
    frequency = {}
    for number in random_numbers:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1

    #find the number with maximum frequency
    max_frequency = max(frequency.values())
    mode_value = None
    for key in frequency:
        if frequency[key] == max_frequency:
            mode_value = key
            break

    return random_numbers, mean_value, median_value, mode_value


def main():
    numbers, mean_val, median_val, mode_val = compute_statistics()

    print("Generated Numbers:")
    print(numbers)

    print("\nMean =", mean_val)
    print("Median =", median_val)
    print("Mode =", mode_val)


if __name__ == "__main__":
    main()
