class Solution {
    public double solution(int[] arr) {
        int s=0;
        int a=0;
        for(int j=0; j<arr.length; j++) {
            s = arr[j]+s;
            a++;
        }
        double result = s / (double)a;
        return result;
    }
}