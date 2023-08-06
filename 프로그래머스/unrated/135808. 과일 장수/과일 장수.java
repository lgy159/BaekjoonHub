import java.util.*;

class Solution {
    public int solution(int k, int m, int[] score) {
        int answer = 0;
        Arrays.sort(score);
        for (int idx = score.length - 1; idx >= m - 1; idx -= m){
            int mininum = score[idx - m + 1];
            answer += mininum * m;
        }
        return answer;
    }
}