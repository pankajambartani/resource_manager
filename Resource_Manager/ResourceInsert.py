#!C:\Python27\python.exe -u
#!/usr/local/bin/python
import cgi
import cgitb
cgitb.enable()
import MySQLdb as db
print "Content-type: text/html"
print """
"""
# Opening  database connection
conn = db.connect(host= "localhost", user = "root", passwd= "Stripes*team", db= "checklist")
# preparing a cursor object using cursor() method
cursor = conn.cursor()
form = cgi.FieldStorage()

if (form.getvalue("DBaction") == 'Update'):
	srNo = form.getlist("srNo")
	category = form.getlist("category")
	hostName = form.getlist("hostName")
	os = form.getlist("os")
	physvm = form.getlist("physvm")
	model = form.getlist("model")
	serialNumber = form.getlist("serialNumber")
	location = form.getlist("location")
	uSpace = form.getlist("uSpace")
	project = form.getlist("project")
	resourceUser = form.getlist("resourceUser")
	secondaryUser = form.getvalue("secondaryUser")
	ip1 = form.getlist("ip1")
	ip2 = form.getlist("ip2")
	conIolIp = form.getlist("conIolIp")
	macAddress = form.getlist("macAddress")
	OVFTemplate = form.getvalue("OVFTemplate")
	bachupDate = form.getvalue("bachupDate")
	remark = form.getlist("remark")

	i = len(category)	
	for x in range(0, i):
		# Preparing SQL query to INSERT a record into the database.
		sql = "UPDATE resource SET category='%s', hostName='%s', os='%s', physvm='%s', model='%s', serialNumber='%s', location='%s', uSpace='%s', project='%s', resourceUser='%s',secondaryUser='%s', ip1='%s', ip2='%s', conIolIp='%s', macAddress='%s', OVFTemplate='%s', bachupDate='%s', remark='%s' WHERE srNo= %s" % (category[x], hostName[x], os[x], physvm[x], model[x], serialNumber[x], location[x], uSpace[x], project[x], resourceUser[x], secondaryUser[x], ip1[x], ip2[x], conIolIp[x], macAddress[x], OVFTemplate[x], bachupDate[x], remark[x], srNo[x])
		try:
			# Execute the SQL command
			cursor.execute(sql)
			# Commit your changes in the database
			conn.commit()
			print "<script type='text/javascript'>"
			print "alert('Updated the Values in Database!!')"
			print "window.location.href = 'http://gen88.in.rdlabs.hpecorp.net/cgi-bin/stripes-res-mgr/Resource_Manager/ResourceMain.py'"
			print "</script>"
			
		except:
			print "Error: unable to fetch data."
	# disconnect from server
	conn.close()	
	
if (form.getvalue("DBaction") == 'Insert'):
	category = form.getvalue("category")
	hostName = form.getvalue("hostName")
	os = form.getvalue("os")
	physvm = form.getvalue("physvm")
	model = form.getvalue("model")
	serialNumber = form.getvalue("serialNumber")
	location = form.getvalue("location")
	uSpace = form.getvalue("uSpace")
	project = form.getvalue("project")
	resourceUser = form.getvalue("resourceUser")
	secondaryUser = form.getvalue("secondaryUser")
	ip1 = form.getvalue("ip1")
	ip2 = form.getvalue("ip2")
	conIolIp = form.getvalue("conIolIp")
	macAddress = form.getvalue("macAddress")
	OVFTemplate = form.getvalue("OVFTemplate")
	bachupDate = form.getvalue("bachupDate")
	remark = form.getvalue("remark")

	# getValueList = [category, hostName, os, physvm, model, serialNumber, location, uSpace, project, resourceUser,secondaryUser ,ip1, ip2, conIolIp, macAddress,OVFTemplate, bachupDate, remark]
	# flag = True
	# for x in getValueList:
	# 	if x == None:
	# 		flag = False
	# 		print "<script type='text/javascript'>"
	# 		print "alert('Please Fill all the Fields!')"
	# 		# print "return false"
	# 		# print "window.location.href = 'http://localhost:81/cgi-bin/Resource_Manager/ResourceMain.py?sortField=0&sortFieldFilter=&action=Add+New+System'"
	# 		print "</script>"
	# 		break
	
	sql = "INSERT INTO resource(category, hostName, os, physvm, model, serialNumber, location, uSpace, project, resourceUser, secondaryUser, ip1, ip2, conIolIp, macAddress, OVFTemplate, bachupDate, remark) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (category, hostName, os, physvm, model, serialNumber, location, uSpace, project, resourceUser,secondaryUser, ip1, ip2, conIolIp, macAddress, OVFTemplate, bachupDate, remark)
	print sql
	try:
		#Execute the SQL command
		cursor.execute(sql)
		# Commit your changes in the database
		conn.commit()
		print "<script type='text/javascript'>"
		print "alert('Inserted the Values in Database!!')"
		print "window.location.href = 'http://gen88.in.rdlabs.hpecorp.net/cgi-bin/stripes-res-mgr/Resource_Manager/ResourceMain.py'"
		print "</script>"
	except:
		print "Error: unable to fecth data"
	# disconnect from server
	conn.close()