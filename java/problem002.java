
public class problem002 {
	static int result;

	public static void main(String[] args) {
		int sum=0;
		int a=1;
		int b=2;

		while (a<=4000000){
			if (a%2==0) sum+=a;
			int temp=a;
			a=b;
			b=temp+a;
		}



		System.out.println(sum);
	}
}