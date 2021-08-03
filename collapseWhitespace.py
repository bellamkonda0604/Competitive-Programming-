# Collapsewhitespaces [10 pts]
# Without using the s.replace() method, write the function 
# collapseWhitespace(s), that takes a string s and returns an 
# equivalent string except that each occurrence of whitespace 
# in the string is replaced by a single space. So, for example, 
# collapseWhitespace("a\t\t\tb\n\nc") replaces the three tabs 
# with a single space, and the two newlines with another single 
# space , returning "a b c ". Here are a few more test cases 
# for you:

# assert(cw("a\nb") == "a b")
# assert(cw("a\n   \t    b") == "a b")
# assert(cw("a\n   \t    b  \n\n  \t\t\t c   ") == "a b c ")
# Once again, do not use s.replace() in your solution. 
# You should not use a regular expression library.

def cw(s):
    # Your code goes here...
    flag = 1
    s1 = ""
    for i in s:
        if(not i.isspace()):
            s1 = s1 + i
            flag = 1
        else:
            if (flag == 1):
                s1 = s1 + " "
            flag = 0
    return s1

assert(cw("a\nb") == "a b")
assert(cw("a\n   \t    b") == "a b")
assert(cw("a\n   \t    b  \n\n  \t\t\t c   ") == "a b c ")
print ("All test cases passed...")