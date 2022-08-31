import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Bomb
{
    int x,y;
    int time;

    public Bomb(int x, int y, int time) {
        this.x = x;
        this.y = y;
        this.time = time;
    }
}
public class Q16918 {
    static int R,C,N;
    static char [][] map;
    static int [][] boomTime;
    static Queue<Bomb> q;
    static int [] dx = {-1,1,0,0};
    static int [] dy = {0,0,-1,1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());

        map = new char[R][C];
        boomTime = new int[R][C];
        q = new PriorityQueue<>((o1, o2) -> o1.time - o2.time);

        int curTime = 0;

        for (int i = 0; i < R; i++) {
            String str = br.readLine();

            for (int j = 0; j < C; j++) {
                char c = str.charAt(j);
                map[i][j] = c;
                if (c == 'O') {
                    q.add(new Bomb(i, j, curTime + 3));
                    boomTime[i][j] = curTime + 3;
                }
            }
        }

        // 1초 아무것도 안함
        curTime++;

        while (++curTime <= N) {
            if (curTime % 2 == 0) setBomb(curTime);
            else boom(curTime);
        }

        StringBuilder sb = new StringBuilder();
        for (char [] arr : map) {
            for (char c : arr) {
                sb.append(c);
            }
            sb.append("\n");
        }

        System.out.print(sb);
    }

    static void setBomb(int curTime) {
        int setTime = curTime + 3;
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (map[i][j] == '.') {
                    map[i][j] = 'O';
                    q.add(new Bomb(i, j, setTime));
                    boomTime[i][j] = setTime;
                }
            }
        }
    }
    static void boom(int curTime) {
        while (!q.isEmpty() && q.peek().time == curTime) {
            Bomb b = q.poll();

            if (boomTime[b.x][b.y] == 0) continue;

            boomTime[b.x][b.y] = 0;
            map[b.x][b.y] = '.';

            for (int idx = 0; idx < 4; idx++) {
                int mx = b.x + dx[idx];
                int my = b.y + dy[idx];

                if (!isValid(mx, my) || boomTime[mx][my] == curTime) continue;

                //터뜨림
                map[mx][my] = '.';
                boomTime[mx][my] = 0;
            }
        }
    }

    static boolean isValid(int x, int y) {
        return x >= 0 && y >= 0 && x < R && y < C;
    }
}
