#!/usr/bin/python3

def generate_pali(s):
    dic = {}
    pali = ""
    for each in s:
        if each in dic:
            dic[each] += 1
        else:
            dic[each] = 1
    for each,value in dic.items():
        if value == 1:
            pali = each
            break
    for each,value in dic.items():
        if value == 2:
            pali = each + pali + each

    print(pali)

generate_pali("aabc")
