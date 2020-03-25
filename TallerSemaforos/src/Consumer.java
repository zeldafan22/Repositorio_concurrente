import java.util.Random;

public class Consumer extends Thread {

	public Consumer() {
		
		start();
	}
	
	private void consume() {
		
		Random rdmNum = new Random();
		int sleepTime = rdmNum.nextInt(250 - 25 + 1) + 25;
		
		try {
			sleep(sleepTime);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		//Consumir el elemento
		int consumedNumber = Buffer.getStore().poll();
		System.out.println("Consumidor: N�mero " + consumedNumber + " consumido.");
		
	}
	
	@Override
	public void run() {
		
		while(true) {
			
			if(Buffer.getStore().size() == 0) {
				
				System.out.println("Consumidor: El buffer est� vac�o, esperando a que el productor trabaje.");
			}
			
			try {
				Buffer.getsNoVacio().acquire();
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
			
			consume();
			
			Buffer.getsNoLLeno().release();
		}
	}
	
}
