import java.lang.*;
import java.util.*;

public class Arrays {
    public static void main(String[] args) {

        Scanner ip = new Scanner(System.in);
        int n = ip.nextInt();
        int[] array = new int[n];
        for (int i=0; i<n; i++){
            // System.out.println(i);
            array[i] = ip.nextInt();
        }
        // ArrayUtils.reverse(array);
        for (int i=n-1; i>=0; i--){
            System.out.println(array[i]);
        }
        
    }
    
}