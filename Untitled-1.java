import java.util.*;
class Untitled{
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int sum = 0;
for (int x=2;x<=n;x+=2) 
{
int fact =1;
for(int y=1;y<=x;y++) 
{
fact = fact*y;
}
sum = sum+fact;
}
System.out.println(sum);
    }
}