import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        String a = sc.nextLine();
        int n = Integer.parseInt(a);
        for (int i = 0; i < n; i++) {
            String s = sc.nextLine();
            String[] strings = s.split(" ");
            String newString = "god";
            for (int j = 1; j < strings.length; j++){
                newString += strings[j];
            }
            System.out.println(newString);
        } 

    }
}
