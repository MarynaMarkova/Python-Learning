# is_even checks if a number is even
# def is_even(num):
#     return num % 2 == 0

# slugify returns a phrase ready for url
# def slugify(phrase):
#     return phrase.lower().strip().replace(" ", "-")


# count_vowels counts the vowels in a given phrase
def count_vowels(phrase):
    num = 0
    for char in phrase:
        if char in "aeiou":
            num += 1
    return num


n = count_vowels("apple")
print(n)
