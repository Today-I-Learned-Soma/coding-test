import java.util.*;
import java.util.regex.Pattern;
class Solution {
    static int bannedLen;
    static List<String> [] list;
    static Set<Set<String>> resultSet;
    public int solution(String[] user_id, String[] banned_id) {
        bannedLen = banned_id.length;
        list = new List[bannedLen];
        resultSet = new HashSet<>();
        for (int i = 0; i < bannedLen; i++) {
            list[i] = new ArrayList<>();
            String pattern = banned_id[i].replace("*",".");
            for (String userId : user_id) {
                if (Pattern.matches(pattern, userId)) {
                    list[i].add(userId);
                }
            }
        }

        dfs(0, new HashSet<>());
        return resultSet.size();
    }
static void dfs(int idx, HashSet<String> set) {
        if (idx == bannedLen) {
            resultSet.add(new HashSet<>(set));
            return;
        }

        for (String id : list[idx]) {
            if (!set.contains(id)) {
                set.add(id);
                dfs(idx + 1, set);
                set.remove(id);
            }
        }
    }
}