def count_vowels(s):
    vowels = "aeiouAEIOU"  # строка, содержащая все гласные буквы
    return sum(1 for char in s if char in vowels)
