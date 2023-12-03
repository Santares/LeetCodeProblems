import java.util.ArrayList;
import java.util.Deque;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;
import java.util.Set;
import java.util.Stack;

public class TestJava{
    public static void main(String[] args){
        // char[] myCharArray = {'H', 'e', 'l', 'l', 'o'};
        // String testString = "hello world";
        // System.out.println(myCharArray.length);
        // System.out.printf("%s\n", testString);

        // StringBuilder str = new StringBuilder();
        // str.append("hello");
        // System.out.printf("%s\n", str);
        // str.append(" ");
        // System.out.printf("%s\n", str);
        // str.append("world");
        // System.out.printf("%s\n", str);
        // str.insert(0, "test ");
        // System.out.printf("%s\n", str);
        // str.delete(0, 5);
        // System.out.println(str);

        // String testString = "hello world";
        // for (int i = 0; i < testString.length(); i++){
        //     char c = testString.charAt(i);
        //     System.out.println(c);
        // }   
        // for (char c:testString.toCharArray()){
        //     System.out.println(c);
        // }

        // ArrayList<Integer> list = new ArrayList<>();
        // list.add(1);
        // list.add(2);
        // System.out.println(list.size());
        // list.remove(1);
        // System.out.println(list.size());

        // String s1 = "test1";
        // String s2 = s1 + "test2";
        // String s3 = s1.concat(s2);
        // // System.out.println("hello " + s1 + " world");
        // // System.out.println(s2);
        // // System.out.println(s3);

        // char a = 'a';
        // int x = a;
        // System.out.println(x);

        // String test1 ="1234567890";
        // System.out.println(test1.substring(2,8));
        // // String[] strs = test1.split("5");
        // // System.out.println(strs[0]);
        // // System.out.println(strs[1]);
        // System.out.println(test1 == "123");


        // Map<Integer, String> myMap = new HashMap<>();
        // myMap.put(1, "one");
        // myMap.get(1);
        // myMap.getOrDefault(2, "null");

        // myMap.keySet();
        // myMap.values();
        // myMap.isEmpty();
        // myMap.remove(1);
        // myMap.size();
        // myMap.containsKey(2);
        // myMap.containsValue("two");


        // Set<Integer> mySet = new HashSet<>();
        // mySet.add(1);
        // mySet.remove(1);
        // mySet.contains(100);

        // char[] chars = "abcdefg".toCharArray();


        Stack<Integer> myStack = new Stack<>();
        myStack.push(1);
        myStack.pop();
        myStack.peek();
        myStack.isEmpty();


        Queue<Integer> queue=new LinkedList<>();
        queue.offer(100);
        queue.poll();
        queue.isEmpty();
        queue.peek();


        Deque<String> deque = new LinkedList<>();
        deque.offerLast("A"); // A
        deque.offerLast("B"); // A <- B
        deque.offerFirst("C"); // C <- A <- B
        deque.peek();
        deque.peekFirst();
        deque.peekLast();
        deque.isEmpty();
        deque.poll();
        deque.pollFirst();
        deque.pollLast();
    }
}

