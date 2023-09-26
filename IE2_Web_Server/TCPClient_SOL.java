
import java.io.*;
import java.net.*;

public class TCPClient_SOL {
	public static void main(String argv[]) throws Exception {
		String sentence;
		String modifiedSentence;
		InputStreamReader isr = new InputStreamReader(System.in);
		BufferedReader inFromUser = new BufferedReader( isr);
		Socket clientSocket = new Socket("localhost", 6789);
		DataOutputStream outToServer = new DataOutputStream( clientSocket.getOutputStream());
		BufferedReader inFromServer = new BufferedReader(new InputStreamReader( clientSocket.getInputStream()));
		sentence = inFromUser.readLine();
		outToServer.writeBytes(sentence + '\n');
		modifiedSentence = inFromServer.readLine();
		System.out.println("FROM SERVER: " + modifiedSentence);
		clientSocket.close();
	}
}
