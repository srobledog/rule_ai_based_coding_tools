# This code contains intentional bugs that you can use to test the static analysis tools. 
# For example, the calculate_average() function returns None when the list of numbers is empty, 
# but the caller does not check for this condition. Also, the is_prime() function 
# incorrectly returns True for the number 1, which is not a prime number. Additionally, 
# the find_primes() function appends the number to the primes list even if it is not prime.

# You can use two static analysis tools to identify these bugs in the code. One tool could 
# be a rule-based tool, such as PyLint, which uses predefined rules to identify common 
# coding errors. The other tool could be an AI-based tool, such as DeepCode, which uses 
# machine learning algorithms to identify potential bugs in code.

# You can then ask the developers to run both tools on the code and identify the bugs 
# that they find. This can help you compare the effectiveness of the two types of static 
# analysis tools and evaluate the developers' perceptions of each tool.

def calculate_average(numbers):
    if len(numbers) == 0:
        return None
    total = 0
    for number in numbers:
        total += number
    average = total / len(numbers)
    return average

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def find_primes(numbers):
    primes = []
    for number in numbers:
        if is_prime(number):
            primes.append(number)
    return primes

def main():
    numbers = [3, 5, 7, 11, 15, 18, 21]
    average = calculate_average(numbers)
    print("Average: ", average)
    primes = find_primes(numbers)
    print("Primes: ", primes)

if __name__ == "__main__":
    main()
