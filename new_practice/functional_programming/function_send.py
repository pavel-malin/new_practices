def shorten(string_list):
    length = len(string_list[0])
    for s in string_list:
        length = yield s[:length]


mystringlist = ['loremipsum', 'dolorsit', 'ametfoobar']
shortstringlist = shorten(mystringlist)
result = []
try:
    s = next(shortstringlist)
    result.append(s)
    while True:
        lists = list(filter(lambda letter: letter in 'aeiou', s))
        number_of_vowels = len(lists)
        # Truncated next line
        # depending on the number of vowels in the last line
        s = shortstringlist.send(number_of_vowels)
        result.append(s)
except StopIteration:
    pass

print(result)
