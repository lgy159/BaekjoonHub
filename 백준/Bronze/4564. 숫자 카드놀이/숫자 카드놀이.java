import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        while (true) {
            int n = sc.nextInt();
            if (n == 0) break;
            List<Integer> numbers = new ArrayList<Integer>();
            numbers.add(n);
            while (true) {
                int answer = 1;
                String temp = Integer.toString(n);

                if (temp.length() == 1) break;
                for (char num : temp.toCharArray()){
 
                    answer *= (int)num - '0';
                }
                numbers.add(answer);
                n = answer;

            }
            for (int item: numbers){
                System.out.print(item+" ");
            }
            System.out.println("");
        }
    }
}
