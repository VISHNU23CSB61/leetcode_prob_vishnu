class Solution {
    public boolean isPalindrome(int x) {
        int num=x;
        if(x<0){
            return false;

        }
        int reverse=0;
        while(x!=0){
            int lastdigit=x%10;
            reverse=(reverse*10)+lastdigit;
            x/=10;

        }if(reverse==num){
            return true;
        }
        return false;
    }
}
