import java.util.*;
class Main
{
    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        while(t>0)
        {
            t--;
            int n=sc.nextInt();
            int[] a=new int[n];
            for(int i=0;i<n;i++)
                a[i]=sc.nextInt();
            int count=0;
            int[] s=new int[n];
            s[n-1]=0;
            for(int i=n-2;i>=0;i--)
            {
                int min=Integer.MAX_VALUE;
                for(int j=i+1;j<n && j<=i+a[i];j++)
                    if(s[j]<min)
                        min=s[j];
                s[i]=min+1;
            }
            System.out.println(s[0]);
        }
    }
}
