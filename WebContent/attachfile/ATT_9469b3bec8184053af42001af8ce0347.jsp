<%@ page import="java.io.*" %>

<html>
<body>
<%
	String str = request.getParameter("name");
	if (str == null)
	{
		str = "JSP";
	}
%>

Hello, <%=str%>!!!

</body>
</html>