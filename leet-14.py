strs = ["flower", "flow", "flight"]

sorted_strs = sorted(strs)
first = sorted_strs[0]
last = sorted_strs[-1]

prefix = ""

for i in range(len(first)):
    if i < len(last) and first[i] == last[i]:
        prefix += first[i]
    else:
        break

print(prefix)
