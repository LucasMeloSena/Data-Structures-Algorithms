def reverse_words_manual(input: str) -> str:
    res = ''
    l, r = 0, 0
    while r < len(input):
        if (input[r] != ' '):
            r += 1
        else:
            res += input[l:r+1][::-1]
            r += 1
            l = r
    res += ' '
    res += input[l:r+2][::-1]
    return res[1:]

result = reverse_words_manual("Hello World Bob")
print(result)