/* NWERC 2006
 * Sample solution to Pie
 * By Mikael Goldmann
 */
import java.util.*;

class pie_mg 
{
    static Scanner in = new Scanner(System.in);
    static  java.text.NumberFormat format = 
	new  java.text.DecimalFormat("0.000");
    
    public static void main(String[] args)
    {
	for (int n=in.nextInt(); n>0; --n) {
	    int N=in.nextInt(), F=in.nextInt();
	    double[] area = new double[N];
	    double r,lo=0, hi=0;
	    
	    for (int i=0; i<N; ++i) {
		r=in.nextDouble();
		area[i]=r*r*Math.PI;
		if (area[i]>hi) hi=area[i];    
	    }

	    while (hi-lo>1e-5) {
		double mid=(hi+lo)/2;
		double x=0;
		for (int i=0; i<N; ++i) x += Math.floor(area[i]/mid);
		if (x<F+1) hi=mid;
		else lo=mid;    
	    }
	    System.out.println(format.format(lo));    
	}
	
    }
}
