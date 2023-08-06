class Solution {
    public String solution(int[] food) {
        String answer = "";
        String temp = "";
        for (int num = 0; num < food.length; num++) {
            for (int i = 0; i < food[num] / 2; i ++) temp += Integer.toString(num);
        }
        answer += temp + "0";
        for (int idx = temp.length() - 1; idx >= 0; idx --) answer += temp.charAt(idx);
        return answer;
    }
}