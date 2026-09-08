# Recursion
# Write a recursive function

def reverse_string(s):
  if len(s)==0:
    return ""
  return reverse_string(s[1:]) + s[0]
print(reverse_string("hello"))




# reverse("hello")
# → reverse("ello") + "h"
# → reverse("llo") + "e" + "h"
# → reverse("lo") + "l" + "e" + "h"
# → reverse("o") + "l" + "l" + "e" + "h"
# → "o" + "l" + "l" + "e" + "h"
# → "olleh"


def reverse(s):
  if len(s)==0:
    return""
  return reverse(s=[1:]) + s[0]
print(reverse("hello"))