class Solution172{
    public int trailingZeroes(int n) {
        int res = 0;
        int m = 5;
        while (m <= n){
            res += n / m;
            m *= 5;
        }

        return res;
    }
}