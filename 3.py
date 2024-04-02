def find_common_words(s1,s2):
    set1=set(s1.lower().split())
    set2=set(s2.lower().split())
    return (set1&set2)

s1="The quick brown fox jumps over the lazy dog"
s2="The dog is brown and the fox is quick"
print(find_common_words(s1,s2))