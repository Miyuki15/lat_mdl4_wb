def is_palindrome(s):
    cleaned_string = ''.join(s.lower().split())
    return cleaned_string == cleaned_string[::-1]

string = 'Ada apa dengan si Anna'
nama_lengkap = 'Anna'  # Ganti dengan nama lengkap kalian
filtered_data = filter(lambda word: is_palindrome(word), string.split())

palindrome = list(filtered_data)
non_palindrome = [word for word in string.split() if word not in palindrome]

print("Data:", string.split())
print("Palindrome:", palindrome)
print("Non-Palindrome:", non_palindrome)
