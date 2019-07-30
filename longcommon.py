from difflib import SequenceMatcher

string1 = str(input(""))
string2 = str(input(""))

match = SequenceMatcher(None, string1, string2).find_longest_match(0, len(string1), 0, len(string2))

print(string1[match.a: match.a + match.size]) 
