# prime_numbers.py

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_primes_up_to(limit):
    print(f"Prime numbers up to {limit}:")
    for num in range(2, limit + 1):
        if is_prime(num):
            print(num, end=' ')
    print()  # for newline

# Example usage
if __name__ == "__main__":
    try:
        limit = int(input("Enter the upper limit: "))
        print_primes_up_to(limit)
    except ValueError:
        print("Please enter a valid integer.")
