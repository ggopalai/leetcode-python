class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        if (n == 0){return 0;}
        Map<Character, Integer> hm = new HashMap();
        int l = 0; 
        int r = 0;
        int maxLength = 1;
        while (r < n){
            // move left pointer, delete from in map
            while (hm.containsKey(s.charAt(r)) && l < r){
                hm.remove(s.charAt(l));
                l++;
            }
            hm.put(s.charAt(r), 1);
            maxLength = Math.max(maxLength, r - l + 1);
            r++;
        }
        return maxLength;
    }
}