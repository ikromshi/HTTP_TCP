
final class JavaThreadLogic implements Runnable {
	int limit;

	public JavaThreadLogic(int limit) throws Exception {
		this.limit = limit;
	}

	public void run() {
		try {
			doTheWork();
		} catch (Exception e) {
			System.out.println(e);
		}
	}

	private void doTheWork() throws Exception {
//		String name = Thread.currentThread().getName();
		long id = Thread.currentThread().getId();
		while (limit > 0) {
			System.out.println(id + ": " + limit);
			Thread.sleep(1000);
			limit--;
		}
	}
}
