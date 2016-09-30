#!C:\Python27\python.exe -u
#!/usr/local/bin/python 
import cgi
import cgitb
cgitb.enable()
import MySQLdb as db
print "Content-type: text/html"
print """
<!DOCTYPE html5>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<title>Resource Manager</title>
	<!-- CSS and JS are in C:\wamp\www\Resource_Manager -->
	<link rel="stylesheet" type="text/css" href="/Resource_Manager/css/jquery-ui.css">
	<link rel="stylesheet" type="text/css" href="/Resource_Manager/css/resourceManager.css">
	<script  src="/Resource_Manager/js/jquery.js"></script>
	<script  src="/Resource_Manager/js/jquery-ui.js"></script>
	<script  src="/Resource_Manager/js/pankaj.js"></script>	
</head>
<body>
	<div id="topbar"><h2>Resource Manager</h2></div>
	<div id="w">
		<div id="content">
			<div>
				<p style="text-align: center; margin-bottom: 20px; font-size: 20px;">BITS System Usage Pool</p>
			</div>
		<!-- //////////////////////////////////////////////////////////////////////////////////////////// -->
		<form id="selectForm" name="selectForm" method="get" action="ResourceMain.py">
		<div class="form-group cb-col-100" style="margin-left: 30%;">
				<div class="form-group">
					<strong>Sort Field</strong>
					<select class="form-control" name="sortField" id="sortField" >
						<option value="0" selected="selected">Select</option>
						<option value="category">Category</option>
						<option value="hostName">Host Name</option>
						<option value="os">Operating System</option>
						<option value="physvm">Physical/VM</option>
						<option value="model">Model</option>
						<option value="serialNumber">Serial Number</option>
						<option value="location">Location</option>
						<option value="uSpace">U Space</option>
						<option value="project">Project</option>						
						<option value="resourceUser">Resource user</option>
						<option value="ip1">IP Address 1</option>
						<option value="ip2">IP Address 2</option>
						<option value="conIolIp">Console/ILO IP</option>
						<option value="macAddress">Mac Address</option>
					</select>
				</div>
				<div class="form-group">
					<strong>Search Field</strong>
					<input class="form-control" type="textarea" name="sortFieldFilter" id="sortFieldFilter" placeholder="Search by field"></input>	
				</div>
			</div>
			<div><center><input type="submit" class="flatbtn" name="action" id="action" value="Submit"></input></center></div>
			<div style="text-align: center;">
				<p style="text-align: center; margin-top: 22px; margin-bottom: 22px; font-size: 20px;">Click New System to Add;Fix via Reset;</p>
				<button class="flatbtn" name="reset" id="reset" value="Reset">Reset</button>
				<input type="submit" class="flatbtn" name="action" id="action" value="Add New System"></input>
			</div>
			</form>
			<!-- //////////////////////////////////////////////////////////////////////////////////////////// -->
"""
form = cgi.FieldStorage()
if form.getvalue("action") == "Submit":
	sortFieldFilter = form.getvalue("sortFieldFilter")
	sortBy = form.getvalue("sortField")
	#Creating list of column name
	columnList = ['srNo','category','hostName','os','physvm','model','serialNumber','location','uSpace',\
	'project','resourceUser','secondaryUser','ip1','ip2','conIolIp','macAddress','OVFTemplate','bachupDate','remark']
	## Opening  database connection
	conn = db.connect(host ="localhost", user="root", passwd="Stripes*team", db= "checklist")
	cursor = conn.cursor()
	#Preparing SQL query to Select a record from the database.
	sql = ("SELECT * FROM resource WHERE %s = '%s';") %(sortBy,sortFieldFilter)
	queryResult = cursor.execute(sql)

	if (sortBy == 0 or sortFieldFilter == None):
		print "<script type='text/javascript'>"
		print "alert('Please fill all the field')"
		print "</script>"
	elif (queryResult == 0):
		print "<script type='text/javascript'>"
		print "alert('Search Field is Not Present or Check the Search Value!')"
		print "</script>"
	else:
		print """
				<div id="resultTable">					
					<div class="line"><h2>Information</h2></div>
					<form name="systemForm" id="systemForm" method="post" action="ResourceInsert.py">
					<table>
						<thead>
							<tr>
								<th>Category</th>
								<th>Host Name</th>
								<th>Operating System</th>
								<th>Physical/VM</th>
								<th>Model</th>				
								<th>Serial Number</th>
								<th>Location</th>
								<th>U Space</th>		
								<th>Project</th>
								<th>Primary User</th>
								<th>Secondary user</th>
								<th>IP Address1</th>
								<th>IP Address2</th>
								<th>Console/ILO IP</th>
								<th>MAC Address</th>
								<th>OVF Template</th>
								<th>Date</th>
								<th>Remark</th>
							</tr>
						</thead>
		"""		
		results = cursor.fetchall()		
		print "<tbody>"
		for row in results:
			print "<input type='hidden' name='%s' id='%s' value='%s'></input>" % (columnList[0], columnList[0], row[0])
			print "<tr>"
			for x in xrange(1,19):
				print "<td><input type='textarea' class='txtfieldTable' name='%s' id='%s' value='%s' required=""></input></td>" % (columnList[x],columnList[x],row[x])
			print "</tr>"
		print "</tbody>"
		print "</table>"
		print "<div><center><input type='submit' class='flatbtn' id='DBaction' name='DBaction' value='Update'></input></center></div>"

if form.getvalue("action") == "Add New System":
	print """
			<div id="resultTable">
				<div class="line"><h2>Information</h2></div>
				<form name="systemForm" id="systemForm" method="post" action="ResourceInsert.py">
				<table>
					<thead>
						<tr>
							<th>Category</th>
							<th>Host Name</th>
							<th>Operating System</th>
							<th>Physical/ VM</th>
							<th>Model</th>				
							<th>Serial Number</th>
							<th>Location</th>
							<th>U Space</th>		
							<th>Project</th>
							<th>Primary User</th>
							<th>Secondary user</th>
							<th>IP Address1</th>
							<th>IP Address2</th>
							<th>Console/ ILO IP</th>
							<th>MAC Address</th>
							<th>OVF Template</th>
							<th>Date</th>
							<th>Remark</th>														
						</tr>
					</thead>
					<tbody>
						<tr>
							<td><select class="txtfieldTable" name="category" id="category" required>
								<option value="" selected="selected">Select</option>
								<option value="Storage">Storage</option>
								<option value="NED">NED</option>
								<option value="HP-UX">HP-UX</option>
							</select></td>
							<td><input type="textarea" class="txtfieldTable" name="hostName" id="hostName" required=""></input></td>
							<td><input type="textarea" class="txtfieldTable" name="os" id="os" required=""></input></td>
							<td><input type="textarea" class="txtfieldTable" name="physvm" id="physvm" required=""></input></td>
							<td><input type="textarea" class="txtfieldTable" name="model" id="model" required=""></input></td>
							<td><input type="textarea" class="txtfieldTable" name="serialNumber" id="serialNumber" required=""></input></td>
							<td><input type="textarea" class="txtfieldTable" name="location" id="location" required=""></input></td>
							<td><input type="textarea" class="txtfieldTable" name="uSpace" id="uSpace" required=""></input></td>
							<td><input type="textarea" class="txtfieldTable" name="project" id="project" required=""></input></td>
							<td><input type="textarea" class="txtfieldTable" name="resourceUser" id="resourceUser" required=""></input></td>
							<td><input type="textarea" class="txtfieldTable" name="secondaryUser" id="secondaryUser" required=""></input></td>
							<td><input type="textarea" class="txtfieldTable" maxlength="15" name="ip1" id="ip1" required=""></input></td>
							<td><input type="textarea" class="txtfieldTable" maxlength="15" name="ip2" id="ip2" required=""></input></td>
							<td><input type="textarea" class="txtfieldTable" maxlength="15" name="conIolIp" id="conIolIp" required=""></input></td>
							<td><input type="textarea" class="txtfieldTable" name="macAddress" id="macAddress" required=""></input></td>
							<td><select name="OVFTemplate" id="OVFTemplate" class="txtfieldTable" required>
								<option value="">Select</option>
								<option value="yes" name="yes" id="yes">Yes</option>
								<option value="no" name="no" id="no">No</option>								
							</select></td>
							<td><input type="date" class="txtfieldTable" name="bachupDate" id="bachupDate" style="width: 80px" required=""></input></td>
							<td><input type="textarea" rows="10" class="txtfieldTable" name="remark" id="remark" required=""></input></td>
						</tr>
					</tbody>
				</table>
				<div><center><input type="submit" class="flatbtn" name="DBaction" id="DBaction" value="Insert"></input></center></div>
				</form>
	"""
print "</div>"	
print"""
		</div>
	</div>
</body>
</html>
"""