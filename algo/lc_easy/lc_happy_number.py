class Solution:
    def isHappy(self, n: int) -> bool:
        
        def getNext(n: int) -> int:
            t = 0
            while n > 0:
                n, d = divmod(n, 10)
                t += d ** 2
            return t
        
        s = set()
        while n != 1 and n not in s:
            s.add(n)
            n = getNext(n)
        
        return n == 1


#Golang

# func getNext(n int) int {
#     t := 0
#     for n > 0 {
#         a := n % 10
#         n = n / 10
#         t = t + int(math.Pow(float64(a), float64(2)))
#     }
#     return t
    
# }

# func isHappy(n int) bool {
    
#     m := make(map[int]bool)
#     for (n != 1) {
#         if _, ok := m[n]; !ok {
#             m[n] = true
#             n = getNext(n)
#         } else {
#             break
#         }
#     }  
    
#     return n == 1
    
# }