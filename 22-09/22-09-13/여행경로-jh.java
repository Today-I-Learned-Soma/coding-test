import java.util.*;

class Solution {
    static Map<String, List<String>> map;
    static Map<String, Integer> ticketCount;
    static String resultString;
    static int resultSize;
    static boolean isDone;
    public String[] solution(String[][] tickets) {
        String[] answer;
        map = new HashMap<>();
        ticketCount = new HashMap<>();

        resultSize = tickets.length;

        for (String[] ticket : tickets) {
            String from = ticket[0];
            String to = ticket[1];
            String sum = from.concat(to);
            ticketCount.put(sum, ticketCount.getOrDefault(sum, 0) + 1);

            List<String> list = new ArrayList<>();
            if (map.containsKey(from)) {
                list = map.get(from);
            }
            list.add(to);
            map.put(from, list);
        }

        for (String key : map.keySet()) {
            Collections.sort(map.get(key));
        }

        dfs("ICN", "ICN", 1);

        answer = resultString.split(" ");
        return answer;
    }
    static void dfs(String from, String result, int resultCount) {
        if (!isDone) {
            if (resultCount == resultSize + 1) {
                resultString = result;
                isDone = true;
                return;
            }

            if (map.containsKey(from)) {
                List<String> getDest = map.get(from);
                for (String to : getDest) {
                    String ticket = from.concat(to);
                    int curCount = ticketCount.get(ticket);
                    if (curCount > 0) {
                        ticketCount.put(ticket, curCount - 1);
                        dfs(to, result + " " + to, resultCount + 1);
                        ticketCount.put(ticket, curCount);
                    }
                }
            }
        }
    }
}