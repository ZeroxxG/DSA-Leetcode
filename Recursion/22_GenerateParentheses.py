temp = ""
res = []
openn = 0
close = 0

def generate(openn, close, temp, res, n):
    if openn == n and close == n:
        res.append(temp)
        return

    if openn < n:
        temp += '('
        generate(openn+1, close, temp, res, n)
        temp = temp[:-1]

    if close < openn:
        temp += ')'
        generate(openn, close+1, temp, res, n)
        temp = temp[:-1]
        
generate(openn, close, temp, res, n)

return res