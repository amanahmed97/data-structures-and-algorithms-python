import java.lang.*;
import java.util.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Inputs {
    public static void main(String[] args) throws IOException {
        
        //your code goes here
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int ip1 = Integer.parseInt(br.readLine());
        int ip2 = Integer.parseInt(br.readLine());
        
        System.out.println(ip1+" "+ip2);
        
    }
}