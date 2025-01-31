import java.util.*;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        Map<String, Integer> map = new HashMap<>();
        for (int i = 0; i < players.length; i++) {
            map.put(players[i], i);
        }
        
        for (String s: callings) {
            int idx = map.get(s);
            
            players[idx] = players[idx - 1];
            map.put(players[idx], idx);
            players[idx - 1] = s;
            map.put(s, idx - 1);
        }
        return players;
    }
}