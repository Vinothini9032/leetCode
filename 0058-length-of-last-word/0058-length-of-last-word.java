class Solution {
    public int lengthOfLastWord(String s) {
        s=s.trim();
        int lastspace=s.lastIndexOf(' ');
        if(lastspace==-1)return s.length();
        return s.length()-lastspace-1;
        
    }
}