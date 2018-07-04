import java.io.File;
import java.io.IOException;
import java.io.InputStream;

public class Main {
	
	private static void showStudentProcess(Process studentProcess) throws IOException {		
		InputStream in = studentProcess.getInputStream();
		InputStream err = studentProcess.getErrorStream();
		byte b[] = new byte[in.available()];
		in.read(b,0,b.length);
		System.out.println(new String(b));
	}
	
	public static void main(String[] args) throws IOException, InterruptedException {
		// TODO catch throw exceptions
		// TODO run all student projects
		
		// TODO copy test cases and student projects to safe directories
		// TODO clear the directories
		String studentJarName = "pta-by-th.jar";
		String studentJarDirectory = "/root/Desktop";
		String studentJarFullName = studentJarDirectory + File.separator + studentJarName;
		
		final Runtime re = Runtime.getRuntime();
		re.exec("cp " + studentJarFullName + " .").waitFor();		
		
		String jarCommand = "java -jar " + studentJarName + " /root/workspace/code_original/ test.Hello";
		System.out.println(jarCommand);
		Process studentProcess = re.exec(jarCommand);
		//TODO set time out limit
		studentProcess.waitFor();
		
		File resultFile = new File("result.txt");
		if (resultFile.exists() && !resultFile.isDirectory()) {
			
			
		}
		
	}

}
