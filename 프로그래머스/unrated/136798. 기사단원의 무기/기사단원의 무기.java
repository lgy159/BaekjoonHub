import java.util.*;

class Solution {
    public int solution(int number, int limit, int power) {
        int answer = 0;
        for (int num = 1; num <= number; num++){
            List<Integer> nums = new ArrayList<Integer>();
            for (int q = 1; q <= Math.sqrt(num); q++){
                if (num % q == 0){
                    nums.add(q);
                    if (num / q != q) nums.add(num / q);                    
                }
            }
            if (nums.size() <= limit) answer += nums.size();
            else answer += power;
        }
        return answer;
    }
}