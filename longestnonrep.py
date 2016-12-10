# this program finds the longest non repeating substring (not sub sequesnce ) in the given string

class Res:
    def __init__(self, l, s = ""):
        self.length = l
        self.string = s

    def copy_obj(src):
        self.length = src.length
        self.string = src.string


def find_largest_substring(string):
    cur_max = Res(0)
    all_max = Res(0)
    for each in string:
        if each in cur_max.string:
            cur_max.length = 0
            cur_max.string = ""
        else:
            cur_max.length += 1
            cur_max.string += each

            if cur_max.length > all_max.length:
                all_max.length = cur_max.length
                all_max.string = cur_max.string

    return all_max

res = find_largest_substring("pwwkew")
print(res.length, res.string)
