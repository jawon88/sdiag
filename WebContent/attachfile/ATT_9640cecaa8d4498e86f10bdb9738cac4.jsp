<html>
<body>
<%
	String str = request.getParameter("name");
	if(str == null)
	{
		str = "JSP";
	}
	HEllo, <%=str %>!!!
%>
</body>
</html>