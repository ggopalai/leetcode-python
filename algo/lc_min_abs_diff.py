def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        mindif = 99999
        arr = sorted(arr)
        res = []
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] < mindif:
                mindif = arr[i+1] - arr[i]
                
        for i in range(len(arr)-1):
            if arr[i] + mindif == arr[i+1]:
                res.append([arr[i], arr[i+1]])
                
        return res