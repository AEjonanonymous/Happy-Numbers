import pandas as pd

def sum_digits_squared(n):
    """Calculates the sum of the squares of the digits of a number."""
    total_sum = 0
    while n > 0:
        total_sum += (n % 10) ** 2
        n //= 10
    return total_sum

def sum_digits(n):
    """Calculates the sum of the digits of a number."""
    total_sum = 0
    while n > 0:
        total_sum += n % 10
        n //= 10
    return total_sum

def analyze_number(n):
    """
    Analyzes a number to determine if it's happy or unhappy, and returns the total sum of its
    digit sums and the sequence length.
    """
    path, sums = {n}, []
    current_num = n
    unhappy_cycle = {4, 16, 37, 58, 89, 145, 42, 20}
    
    while current_num not in {1} and current_num not in unhappy_cycle:
        sums.append(sum_digits(current_num))
        current_num = sum_digits_squared(current_num)
        if current_num in path:
            return False, sum(sums), len(sums)
        path.add(current_num)

    sums.append(sum_digits(current_num))
    is_happy = current_num == 1
    
    return is_happy, sum(sums), len(sums)

def main():
    """
    Main function to run the happy number analysis.
    """
    start, end = 1, 1000000
    happy_sums, unhappy_sums = [], []

    for num in range(start, end + 1):
        is_happy, total_sum, sequence_length = analyze_number(num)
        if is_happy:
            happy_sums.append(total_sum)
        else:
            unhappy_sums.append(total_sum)

    happy_count, unhappy_count = len(happy_sums), len(unhappy_sums)
    average_happy_sum = sum(happy_sums) / happy_count if happy_count > 0 else 0
    average_unhappy_sum = sum(unhappy_sums) / unhappy_count if unhappy_count > 0 else 0
    
    ratio = average_unhappy_sum / average_happy_sum if average_happy_sum > 0 else 0

    results_df = pd.DataFrame({
        'Metric': ['Average Happy Sum', 'Average Unhappy Sum', 'Ratio (Unhappy/Happy)'],
        'Value': [average_happy_sum, average_unhappy_sum, ratio]
    })

    print(f"Results for range {start} to {end}:")
    print(results_df)
    print(f"\nTotal Happy Numbers: {happy_count}")
    print(f"Total Unhappy Numbers: {unhappy_count}")

if __name__ == "__main__":
    main()