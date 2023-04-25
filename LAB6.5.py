#Question1

def common_elements(list1, list2):
    common = []
    for i in list1:
        if i in list2:
            common.append(i)
    return common

list1 = [9,10,15,20,25]
list2 = [15,25,9,35,50]
common = common_elements(list1, list2)
print(common)
#Question2

def palindromes(list):

    palindromes = []
    for string in list:
        if string == string[::-1]:
            palindromes.append(string)

    return palindromes

a=["kek","pop","love","ses"]
b=palindromes(a)
print(b)
#Question3

def sieve_of_eratosthenes(numbers):
    primes = [True] * len(numbers)

    for i in range(len(numbers)):
        if primes[i]:
            for j in range(i + numbers[i], len(numbers), numbers[i]):
                primes[j] = False

    result = [numbers[i] for i in range(len(numbers)) if primes[i]]

    return result
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10,13,20]
primes = sieve_of_eratosthenes(numbers)
print(primes)

#Question4
def anagrams(word, word_list):

    sorted_word = sorted(word.lower())
    anagrams = []
    for string in word_list:

        sorted_string = sorted(string.lower())

        if sorted_word == sorted_string:

            anagrams.append(string)
    return anagrams

word = "listen"
word_list = ["enlists", "google", "inlets", "banana"]
anagrams_list = anagrams(word, word_list)
print(anagrams_list)




