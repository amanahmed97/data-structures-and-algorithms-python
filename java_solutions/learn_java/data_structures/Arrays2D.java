import java.lang.*;
import java.util.*;

public class Arrays2D {
    public static void main(String[] args) {

        Scanner ip = new Scanner(System.in);
        int rows = ip.nextInt();
        int cols = ip.nextInt();
        int[][] array = new int[rows][cols];
        int[] ans = new int[cols];
        
        for (int i=0; i<rows; i++){
            for (int j=0; j<cols; j++){
                array[i][j] = ip.nextInt();
            }
        }
        
        for (int j=0; j<cols; j++){
            ans[j] = 0;
            for (int i=0; i<rows; i++){
                ans[j] += array[i][j];   
            }
        }
        
        for (int j=0; j<cols; j++){
            System.out.print(ans[j]+" ");
        }
    }
}
