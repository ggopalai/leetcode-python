from typing import List

def evalPostfix(s: List) -> int:
    st = list()
    for i in range(len(s)):
        if s[i].isnumeric():      
            st.append(int(s[i]))
        else:
            b = st.pop()
            a = st.pop()
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
    print(evalPostfix(['20', '50', '3', '6', '+', '*', '*', '300', '/', '2', '-']))