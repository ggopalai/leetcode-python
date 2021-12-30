from typing import List

def evalPrefix(s: List) -> int:
    s = s[::-1]
    st = list()
    for i in range(len(s)):
        if s[i].isnumeric():      
            st.append(int(s[i]))
        else:
            a = st.pop()
            b = st.pop()
            if s[i] == '+':
                st.append(a+b)
            elif s[i] == '-':
                st.append(a-b)
            elif s[i] == '*':
                st.append(a*b)
            elif s[i] == '^':
                st.append(a**b)
            else:
                if b == 0:
                    raise ValueError('Cannot divide by 0')
                st.append(a/b)
    
    return st.pop()

if __name__ == '__main__':
    print(evalPrefix(['^', '2', '3']))