class Solution:
  def isValid(self, s: str):

    bracket_map = {"(": ")", "{": "}", "[": "]"}
    open_par = set(["(", "{", "["])
    stack = []

    for i in s:
      if i in open_par:
        stack.append(i)
      elif stack and i  == bracket_map[stack[-1]]:
        stack.pop()
      else:
        return False
    return stack == []

result = Solution()
print(result.isValid("[]"))


# stack = [{, (, ]
# bracket_map[]

# リストの最後の要素のインデックスは-1

# pop()は要素の最後を削除する

# append()は末尾に要素を追加できる（末尾以外に追加するときはinsert()）

