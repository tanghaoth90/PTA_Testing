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
	/** 
	 * java -jar runnable.jar [StudentJarName] [StudentJarDirectory] 
	 * 		[AnalyzedCodeDirectory] [AnalyzedMainClass] [SafeRunningDirectory]
	 */
	public static void main(String[] args) throws IOException, InterruptedException {
		// TODO catch throw exceptions
		// TODO run all student projects		
		// TODO copy test cases and student projects to safe directories
		// TODO clear the directories
		String studentJarName = args[0];
		String studentJarPath = args[1];
		String analyzedCodePath = args[2];
		String analyzedMainClass = args[3];
		String safeRunningDirectory = args[4]; // TODO deal with the case when the safe path is not '.'
		String studentJarFullName = studentJarPath + File.separator + studentJarName;
		
		final Runtime re = Runtime.getRuntime();
		//new File(safeRunningDirectory).mkdirs();
		// TODO using Files (Java 7) to copy and delete files
		
		re.exec("cp " + studentJarFullName + " " + safeRunningDirectory).waitFor();		
		
		String jarCommand = "java -jar " + studentJarName + " " + analyzedCodePath + " " + analyzedMainClass;
		System.out.println(jarCommand);
		Process studentProcess = re.exec(jarCommand);
		//TODO set time out limit
		studentProcess.waitFor();
		
		File resultFile = new File("result.txt");
		if (resultFile.exists() && !resultFile.isDirectory()) {
			
			
		}
		
	}

}
