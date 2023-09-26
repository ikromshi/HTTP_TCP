
public class JavaThreadCreator {
	public static void demo1() throws Exception {
		JavaThreadLogic brain = new JavaThreadLogic(2);
		Thread t1 = new Thread(brain);
		t1.start();
	}
	public static void demo2() throws Exception {
		JavaThreadLogic brain = new JavaThreadLogic(10);
		Thread t1 = new Thread(brain);
		t1.start();
		Thread t2 = new Thread(brain);
		t2.start();
	}
	public static void demo3() throws Exception {
		JavaThreadLogic brain = new JavaThreadLogic(10);
		Thread t1 = new Thread(brain);
		t1.start();
		JavaThreadLogic brain2 = new JavaThreadLogic(15);
		Thread t2 = new Thread(brain2);
		t2.start();
	}

	public static void main(String[] args) throws Exception {
		demo3();
	}
}
