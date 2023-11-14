import java.util.ArrayList;
import java.util.Collections;

class Solution2785 {
    public String sortVowels(String s) {
        ArrayList<Character> vowels = new ArrayList<>();

        for(int i =0; i < s.length(); i++){
            char c = s.charAt(i);
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' 
            || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U' ){
                vowels.add(c);
            }
        }

        Collections.sort(vowels);
        StringBuilder str = new StringBuilder();

        int j = 0;
        for(int i =0; i < s.length(); i++){
            char c = s.charAt(i);
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' 
            || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U' ){
                str.append(vowels.get(j++));
            } else {
                str.append(c);
            }
        }

        return str.toString();
    }
}