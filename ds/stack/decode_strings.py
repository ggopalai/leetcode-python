def decompress(s: str) -> str:
    stack = []
    cur = ""
    num = ""
    for c in s:
        if c == ']':
            # keep reading until you find [
            while stack[-1] != '[':
                cur = stack.pop() + cur
            
            # pop the opening bracket
            stack.pop()
            
            # read in number
            while stack and stack[-1].isnumeric():
                num = stack.pop() + num
            
            # form string
            inter = cur * int(num)
            num = ""
            cur = ""

            # push back into string
            for i in inter:
                stack.append(i)
        else:
            stack.append(c)
    
    return ("".join(stack))

if __name__ == '__main__':
    
    # test case 1     
    if decompress('3[abc]4[ab]c') == 'abcabcabcababababc':
        print('Test 1 PASSED!!!')
    else:
        print('Test 1 failed')
    
    # test case 2 - edge case 
    if decompress('0[abc]4[ab]c') == 'ababababc':
        print('Test 2 PASSED!!!')
    else:
        print('Test 2 failed')
    
    # test case 3 - edge case
    if decompress('4[abc]4[]c') == 'abcabcabcabcc':
        print('Test 3 PASSED!!!')
    else:
        print('Test 3 failed')

    # test case 4, with recursive decompression
    if decompress('2[3[a]b]') == 'aaabaaab':
        print('Test 4 PASSED!!!')
    else:
        print('Test 4 failed')
