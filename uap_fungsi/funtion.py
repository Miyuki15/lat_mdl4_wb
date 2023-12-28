def is_palindrome(s):
    cleaned_string = ''.join(s.lower().split())
    return cleaned_string == cleaned_string[::-1]

string = 'radar'
result = is_palindrome(string)
print(result)
