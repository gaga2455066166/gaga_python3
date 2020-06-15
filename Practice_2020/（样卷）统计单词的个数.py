def word_len(s):
    return len([i for i in s.split(' ') if i])
def main():
    s =  str(input())
    l = word_len(s)
    print("count =",l)
main()