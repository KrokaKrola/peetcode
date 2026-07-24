class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False

    chars_of_s = {}
    chars_of_t = {}

    for i in range(len(t)):
      chars_of_s[s[i]] = 1 + chars_of_s.get(s[i], 0)
      chars_of_t[t[i]] = 1 + chars_of_t.get(t[i], 0)

    return chars_of_s == chars_of_t

print(Solution().isAnagram("anagram", "nagaram"))
print(Solution().isAnagram("rat", "car"))
