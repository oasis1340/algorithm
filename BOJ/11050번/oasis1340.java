import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int nCount = n;
        int k = sc.nextInt();
        int kCount = k;
        int df = n - k;
        int dfCount = df;
        int nF = 1;
        int kF = 1;
        int dF = 1;
        
        for (int i = 1; i < nCount; i++) {
        	nF *= n;
        	n--;
        }
        
        for (int i = 1; i < kCount; i++) {
        	kF *= k;
        	k--;
        }
        
        for (int i = 1; i < dfCount; i++) {
        	dF *= df;
        	df--;
        }
        
        System.out.println(nF/(kF*dF));
    }
}
