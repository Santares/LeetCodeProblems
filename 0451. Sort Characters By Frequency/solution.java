class Solution {
    public static void main(String[] args) {
        System.
    }

    public String frequencySort(String s) {
        int[] charDic = new int[52];

        // store the frequency of the characters
        for(int i  = 0; i < s.length(); i++){
            int c = s.charAt(i);
            charDic[c - 65] += 1;
//            System.out.println(c);
        }

        String output = "";

        // "sort"
        while (true) {
            int maxFrequency = 0;
            char c = 0;
            for (int i = 0; i < charDic.length; i++) {
                int f = charDic[i];
                if (f > maxFrequency){
                    maxFrequency = f;
                    c = (char) (i + 65);
                }
            }

            if (maxFrequency == 0){
                break;
            }

            while(maxFrequency > 0){
                output += c;
                maxFrequency -= 1;
            }


        }

        return output;
    }
}