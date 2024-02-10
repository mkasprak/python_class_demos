def is_palindrome(s):
    """
    Check if a string is a palindrome using recursion.

    :param s: str - The string to check.
    :return: bool - True if the string is a palindrome, False otherwise.
    """
    # Base case: A string of length 0 or 1 is a palindrome
    if len(s) <= 1:
        return True

    # Check if the first and last characters are the same
    if s[0] != s[-1]:
        return False

    # Recursive step: Call is_palindrome with the middle section of the string
    return is_palindrome(s[1:-1])


"""
Main function to get user input and check if it's a palindrome.
"""
# Ask the user to enter a word
word = input(
    "Enter a word to check if it's a palindrome: ").strip().lower()

# Check if the word is a palindrome
if is_palindrome(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")
