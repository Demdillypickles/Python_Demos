from time import sleep

separator = "#---------------#\n\n"

word = input("Give me a word!\n>>> ")

for x in word:
    print(x)
    sleep(0.5)

print('\n' + separator)

for i in range(0, 20):
    print(word[0: i % len(word) + 1])
    sleep(0.5)

