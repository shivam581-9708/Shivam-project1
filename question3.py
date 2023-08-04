def count_words(text, word):
    return text.lower().split().count(word)
user_input = input("Enter a string to be checked: ")
cat_count = count_words(user_input, "cat")
dog_count = count_words(user_input, "dog")

if cat_count == dog_count:
    print("True")
else:
    print("False")
