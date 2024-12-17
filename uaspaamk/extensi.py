import random
import time
import matplotlib.pyplot as plt

def generate_array(n, max_value, seed=42):
    random.seed(seed)
    return [random.randint(1, max_value) for _ in range(n)]

def is_unique(array):
    seen = set()
    duplicates = set()
    for num in array:
        if num in seen:
            duplicates.add(num)
        seen.add(num)
    return len(duplicates) == 0, duplicates

def measure_time(n, max_value, trials=10):
    worst_case_time = 0
    total_time = 0

    for _ in range(trials):
        arr = generate_array(n, max_value)

        # Measure time for uniqueness check
        start_time = time.perf_counter()
        unique, duplicates = is_unique(arr)
        elapsed_time = time.perf_counter() - start_time

        total_time += elapsed_time
        worst_case_time = max(worst_case_time, elapsed_time)

    average_time = total_time / trials
    return worst_case_time, average_time

# Parameters
stambuk_last_3_digits = 91  # Replace with your actual 3-digit stambuk number
max_value = 250 - int(f"{stambuk_last_3_digits:03}")
n_values = [100, 150, 200, 250, 300, 350, 400, 500]

# Data collection
worst_case_results = []
average_case_results = []

for n in n_values:
    print(f"\nArray Size: {n}")
    arr = generate_array(n, max_value)
    unique, duplicates = is_unique(arr)

    if unique:
        print("The array is unique.")
    else:
        print(f"The array is not unique. Duplicates: {sorted(duplicates)}")

    worst_case, average_case = measure_time(n, max_value)
    worst_case_results.append(worst_case)
    average_case_results.append(average_case)

    print(f"Worst Case Time: {worst_case:.6f} seconds")
    print(f"Average Case Time: {average_case:.6f} seconds")

# Plotting results
plt.figure(figsize=(10, 6))
plt.plot(n_values, worst_case_results, label="Worst Case", marker="o")
plt.plot(n_values, average_case_results, label="Average Case", marker="o")

plt.title("Performance of Uniqueness Check")
plt.xlabel("Array Size (n)")
plt.ylabel("Time (seconds)")
plt.legend()
plt.grid()
plt.show()