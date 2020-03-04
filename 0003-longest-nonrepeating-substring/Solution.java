class Solution {
    public static int lengthOfLongestSubstring(String s) {
        String substr = "";
        int max_len = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            int substr_i = substr.indexOf(c);
            if (substr_i < 0) {
                substr = substr + c;
            } else {
                if (substr.length() > max_len) {
                    max_len = substr.length();
                }
                substr = substr.substring(substr_i + 1) + c;
            }
        }
        if (substr.length() > max_len) {
            max_len = substr.length();
        }    
        return max_len;
    }

    public static void main(String[] args) {
        String s = "aabaab!bb";
        int max_len = lengthOfLongestSubstring(s);
        System.out.println(max_len);
    }
}