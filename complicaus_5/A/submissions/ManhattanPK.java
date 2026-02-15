import java.io.*;
import java.util.*;

public class ManhattanPK{
   public static void main(String [] args){
      ManhattanPK problem = readTest();
      problem.solve();
      System.out.println(10*problem.solution());
   }
   
   public static ManhattanPK readTest(){
      ManhattanPK problem = null;
      try{
         BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
         String line = in.readLine();
         Scanner ir = new Scanner(line);
         int h = ir.nextInt();
         int w = ir.nextInt();
         problem = new ManhattanPK(w, h);
         for (int k = 0; k < h; k++){
            line = in.readLine();
            problem.add(k,line);
         }
      }
      catch (IOException iox){System.out.println( iox);}
      return problem;
   }
////////////////////////////////////////////////////
   static final int SQUARE = -1;
   static final int CIRCLE = -2;
   static final double BOOG = Math.PI/2;

   int width;
   int height;
   double [][] dist;

   public ManhattanPK(int wIn, int hIn ){
      width = wIn;
      height = hIn;
      dist = new double[2 * height + 1][2 * width + 1];
   }
   
   void add(int k, String regel){
      int row = 2 * k + 1;
      for (int j = 0; j < regel.length(); j++){
         int col = 2 * j + 1;
         char c = regel.charAt(j);
         if (c == 'O')
            dist[row][col] = CIRCLE;
         else if (c == 'X')
            dist[row][col] = SQUARE;
         else
            throw new RuntimeException("wrong character :  " + c);
      }
   }

   void solve(){
     for (int j = 0; j < 2 * width + 1; j++)
        dist[0][j] = j;

     for (int k = 0; k < 2 * height + 1; k++)
        dist[k][0] = k;
        
     for (int k = 1; k < 2 * height + 1; k++){
         fillOdd(k);
         k++;
         fillEven(k);
     }
   }
     
   void fillOdd(int k){
      // k should be odd
      for (int j = 2; j < 2 * width + 1; j+=2){
         if (dist[k][j-1] == SQUARE)
            dist[k][j] = 1 + dist[k-1][j];
         else // circle
            dist[k][j] = Math.min(1 + dist[k-1][j], BOOG + dist[k-1][ j-1] );
      }
   }

   void fillEven(int k){
     // k should be even
      for (int j = 1; j < 2 * width + 1; j++){
         if (dist[k-1][j] == SQUARE)
            dist[k][j] =  1 + dist[k][ j-1] ;
         else // circle
            dist[k][j] = Math.min(1 + dist[k][j-1], BOOG + dist[k-1][ j-1] );
         j++;
         dist[k][j] = Math.min(1 + dist[k-1][j], 1 + dist[k][ j-1] );
      }
   }

   double solution(){
      return dist[2* height][2* width]/2;
   }

}