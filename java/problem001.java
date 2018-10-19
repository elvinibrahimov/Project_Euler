
public class problem001 {
	static int result;

	public static void main(String[] args) {
		for (int i = 0; i < 1000; i++) {
			if (i % 3 == 0 || i % 5 == 0)
				result += i;
		}
		System.out.println(result);
	}
}