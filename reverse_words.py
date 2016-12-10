#!/usr/bin/python3

sentence = input()
words = sentence.split()

start = 0
end = len(words) - 1

while(start < end):
    tmp = words[start]
    words[start] = words[end]
    words[end] = tmp
    start += 1
    end -= 1

sentence = " ".join(words)
print(sentence)
