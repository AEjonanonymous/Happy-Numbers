import pandas as pd

def sum_digits_squared(n):
    """Calculates the sum of the squares of the digits of a number."""
    total_sum = 0
    while n > 0:
        total_sum += (n % 10) ** 2
        n //= 10
    return total_sum

def analyze_number(n):
    """
    Analyzes a number to determine if it's happy or unhappy and returns the sequence length.
    """
    path = {n}
    sequence_length = 0
    current_num = n
    unhappy_cycle = {4, 16, 37, 58, 89, 145, 42, 20}
    
    while current_num not in {1} and current_num not in unhappy_cycle:
        current_num = sum_digits_squared(current_num)
        sequence_length += 1
        if current_num in path:
            return False, sequence_length
        path.add(current_num)

    is_happy = current_num == 1
    return is_happy, sequence_length

def main():
    """
    Main function to run the happy number sequence length analysis.
    """
    start, end = 1, 500000
    happy_lengths, unhappy_lengths = [], []

    for num in range(start, end + 1):
        is_happy, sequence_length = analyze_number(num)
        if is_happy:
            happy_lengths.append(sequence_length)
        else:
            unhappy_lengths.append(sequence_length)

    happy_count, unhappy_count = len(happy_lengths), len(unhappy_lengths)
    
    average_happy_length = (sum(happy_lengths) / happy_count if happy_count > 0 else 0)
    average_unhappy_length = (sum(unhappy_lengths) / unhappy_count if unhappy_count > 0 else 0)
    
    ratio = (average_unhappy_length / average_happy_length if average_happy_length > 0 else 0)

    results_df = pd.DataFrame({
        'Metric': ['Average Happy Length', 'Average Unhappy Length', 'Ratio (Unhappy/Happy)'],
        'Value': [average_happy_length, average_unhappy_length, ratio]
    })

    print(f"Results for sequence length analysis from {start} to {end}:")
    print(results_df)
    print(f"\nTotal Happy Numbers: {happy_count}")
    print(f"Total Unhappy Numbers: {unhappy_count}")

if __name__ == "__main__":
    main()
