import java.util.Scanner;

public class Main {
        public static void main(String[] args) throws Exception {
            Scanner sc = new Scanner(System.in);
            while (true) {
                String input = sc.nextLine();
                if (input.charAt(0) == '#') break;
                

                String answer = "";
                Boolean flag = false;
                for (int i = input.length() - 1; i >= 0; i--) {
                    char c = input.charAt(i);
                    if (c == 'd') answer += 'b';
                    else if (c == 'b') answer += 'd';
                    else if (c == 'p') answer += 'q'; 
                    else if (c == 'q') answer += 'p'; 
                    else if (c == 'i' || c == 'o' || c == 'v' || c == 'w' || c == 'x') answer += input.charAt(i);
                    else {
                        System.out.println("INVALID");
                        flag = true;
                        break;
                    }
                }
                if (flag == true) continue; 
                System.out.println(answer);
            }
    }
}
