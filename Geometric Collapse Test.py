import collections
import math
import sys

# Set higher recursion limit for deep happy number sequences
# This is often necessary for long sequence analysis up to 1,000,000 or more.
sys.setrecursionlimit(2000)

def sum_digits_squared(n):
    """Calculates the sum of the squares of the digits of a number."""
    total_sum = 0
    while n > 0:
        total_sum += (n % 10) ** 2
        n //= 10
    return total_sum

def analyze_number(n):
    """
    Analyzes a number to determine if it's happy or unhappy and returns the sequence length (L).
    The length is the number of steps taken before hitting {1} or the unhappy cycle.
    """
    path = {n}
    sequence_length = 0
    current_num = n
    unhappy_cycle = {4, 16, 37, 58, 89, 145, 42, 20}
    
    # Loop until the sequence hits an attractor
    while current_num not in {1} and current_num not in unhappy_cycle:
        current_num = sum_digits_squared(current_num)
        sequence_length += 1
        
        # Check for non-attractor cycles (shouldn't happen for the small number domain, but necessary)
        if current_num in path:
            # We've hit a cycle other than the standard unhappy one
            return False, sequence_length
            
        path.add(current_num)

    is_happy = current_num == 1
    return is_happy, sequence_length

def calculate_consecutive_ratios(counts):
    """
    Calculates the ratio of consecutive counts: Count(L) / Count(L-1).
    This ratio should converge to 1/phi (approx 0.618) as L increases.
    """
    if not counts:
        return []

    # Get sorted list of lengths L
    sorted_lengths = sorted(counts.keys())
    ratios = []
    
    # Iterate from the second element (L) to calculate the ratio with the previous one (L-1)
    for i in range(1, len(sorted_lengths)):
        L = sorted_lengths[i]
        L_minus_1 = sorted_lengths[i-1]
        
        # Ensure the counts are non-zero to prevent division by zero
        if counts[L_minus_1] > 0 and counts[L] > 0:
            ratio = counts[L] / counts[L_minus_1]
            ratios.append({
                'L': L,
                'L-1': L_minus_1,
                'Count(L)': counts[L],
                'Count(L-1)': counts[L_minus_1],
                'Ratio (L / L-1)': ratio
            })

    return ratios

def main():
    """
    Main function to run the geometric factor analysis and print results.
    """
    # Start and End range for N to analyze. Set to 500,000 for a robust sample size.
    start, end = 1, 500000 
    
    # Use dictionaries to store counts of sequences that required exactly L steps.
    happy_counts = collections.defaultdict(int)
    unhappy_counts = collections.defaultdict(int)

    print(f"--- Starting Geometric Collapse Test for N = {start} to {end} ---")
    
    # 1. Run the analysis and populate counts
    for num in range(start, end + 1):
        is_happy, sequence_length = analyze_number(num)
        
        if is_happy:
            happy_counts[sequence_length] += 1
        else:
            unhappy_counts[sequence_length] += 1
            
    print(f"Analysis complete. Max Happy Length found: {max(happy_counts.keys()) if happy_counts else 0}")
    print(f"Analysis complete. Max Unhappy Length found: {max(unhappy_counts.keys()) if unhappy_counts else 0}")

    # 2. Calculate consecutive ratios for both Happy and Unhappy sequences
    happy_ratios = calculate_consecutive_ratios(happy_counts)
    unhappy_ratios = calculate_consecutive_ratios(unhappy_counts)

    # 3. Print the results (Focus on the longest lengths L for asymptotic behavior)
    
    # The target ratio is 1/phi (the geometric collapse rate)
    phi_inverse = (math.sqrt(5) - 1) / 2
    phi = (1 + math.sqrt(5)) / 2
    
    print("\n---------------------------------------------------------------------------------------------------------------------------------")
    print(f"Theoretical Target Ratio (1/phi or phi^-1): {phi_inverse:.6f} (~0.618034)")
    print("---------------------------------------------------------------------------------------------------------------------------------")
    
    def print_ratios(title, ratios, count_limit=5):
        print(f"\n--- {title} (Last {count_limit} Ratios) ---")
        if not ratios:
            print("No data available for this sequence type.")
            return

        print(f"{'L':<5}{'Count(L)':<10}{'Count(L-1)':<12}{'Ratio (L/L-1)':<18}{'Deviation from 1/phi':<20}")
        print("-" * 65)
        
        # Print the last 'count_limit' ratios, which represent the longest lengths (L -> infinity)
        for r in ratios[-count_limit:]:
            deviation = r['Ratio (L / L-1)'] - phi_inverse
            print(f"{r['L']:<5}{r['Count(L)']:<10,}{r['Count(L-1)']:<12,}{r['Ratio (L / L-1)']:<18.6f}{deviation:<+20.6f}")

    print_ratios("Happy Sequence Collapse Rate (H(L) / H(L-1))", happy_ratios, 10)
    print_ratios("Unhappy Sequence Collapse Rate (U(L) / U(L-1))", unhappy_ratios, 10)

if __name__ == "__main__":
    main()