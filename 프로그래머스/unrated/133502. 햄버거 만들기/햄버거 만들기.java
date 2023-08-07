import java.util.*;

class Solution {
    public int solution(int[] ingredient) {
        int answer = 0;

        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < ingredient.length; i++){
            stack.push(ingredient[i]);
            if (stack.size() >= 4) {
                int s = stack.size();
                if (stack.elementAt(s-1) == 1 && stack.elementAt(s-2) == 3 && stack.elementAt(s-3) == 2 && stack.elementAt(s-4) == 1) {
                    for (int j = 0; j < 4; j++) stack.pop();
                    answer += 1;
                }
            } 
        }
        
        
        return answer;
    }
}