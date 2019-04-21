
def permute(inp, i):
    # base case
    if i==len(inp):
        print(''.join(inp), end=',')
        return

    # rec case
    for j in range(i, len(inp)):
        inp[i],inp[j] = inp[j],inp[i]
        permute(inp, i+1)

        # backtracking -- to restore the original array
        inp[i],inp[j] = inp[j],inp[i]


if __name__=='__main__':
    inp = list(input())
    permute(inp,0)
