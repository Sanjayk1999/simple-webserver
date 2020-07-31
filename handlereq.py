
def getheader(data):
	res_data = data.split(' ',maxsplit=2)
	return res_data


header_temp = "HTTP/1.1 200 OK\r\nContent-type: {}\r\n\r\n"
static_dir = 'static/'


def getresponsedata(data):
	response = ""
	if(data[1]=='/'):
		f = open("index.html",'rb')
		res_body = f.read()
		header = header_temp.format('text/html')
		response = header.encode('utf-8') + res_body
		return response
	elif(data[1].endswith('.css')):
		f = open(data[1][1:],'rb')
		res_body = f.read()
		header = header_temp.format('text/css')
		response = header.encode('utf-8')+res_body
		return response
	elif(data[1].endswith('.html')):
		f = open(data[1][1:],'rb')
		res_body = f.read()
		header = header_temp.format('text/html')
		response = header.encode('utf-8')+res_body
		return response

	elif(data[1].endswith('.js')):
		f = open(data[1][1:],'rb')
		res_body = f.read()
		header = header_temp.format('text/javascript')
		response = header.encode('utf-8')+res_body
		return response
