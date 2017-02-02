#!/usr/bin/env python

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os

rootdir = '/webapp/' #file location

#Create custom HTTPRequestHandler class
class HTTPRequestHandler(BaseHTTPRequestHandler):
    #handle GET command
    def do_GET(self):
        try:
            if (self.path=='/') or (self.path=='index.html'):
                create_index(list_html(rootdir+'/html'))
                f = open(rootdir + 'html/'+ 'index.html') #open requested file
                mimetype='text/html'
                self.send_response(200)
                self.send_header('Content-type',mimetype)
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
                return

            sendReply = False
            subfolder = ''
            if self.path.endswith(".html"):
                subfolder='html'
                mimetype='text/html'
		sendReply = True
            if self.path.endswith(".jpg"):
		mimetype='image/jpg'
                subfolder='images/'
	        sendReply = True
            if self.path.endswith(".png"):
                mimetype='image/png'
                subfolder='images/'
                sendReply = True
	    if self.path.endswith(".gif"):
		mimetype='image/gif'
                subfolder='images/'
		sendReply = True
            if self.path.endswith(".js"):
		mimetype='application/javascript'
                subfolder='js/'                
		sendReply = True
	    if self.path.endswith(".css"):
                subfolder='css/'
		mimetype='text/css'
		sendReply = True
            if self.path.endswith(".mp4"):
                print("video!")
                subfolder='video/'
                mimetype='video/mp4'
                sendReply = True
            if self.path.endswith(".ogv"):
                subfolder='video/'
                mimetype='video/ogv'
                sendReply = True

            if sendReply == True:
		#Open the static file requested and send it
		f = open(rootdir+subfolder + self.path) 
		self.send_response(200)
		self.send_header('Content-type',mimetype)
		self.end_headers()
		self.wfile.write(f.read())
		f.close()
            return

        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)

def list_html(dir):
    htmls=[]
    for l in os.listdir(dir):
        if l.endswith('.html') and l!='index.html':
            htmls.append(l)
    return htmls

def create_index(htmls):
    f = open(rootdir +'html/index.html', 'w')
    f.write(
            '<head>\n'
            '<title> NLWA crawl test-site</title>\n'
            '<h1>NLWA crawl test-site</h1>\n'
            '</head>\n'
            '<body>\n'
            )
    for u in htmls:
        title=u.replace('.html', '')
        f.write('<a href=%s>%s</a> <br>\n' % (u, title))
    f.write('</body>')
    f.close()

def run():
    print('http server is starting...')
    #ip and port of servr
    server_address = ('', 3000)
    httpd = HTTPServer(server_address, HTTPRequestHandler)
    print('http server is running...')
    httpd.serve_forever()
    
if __name__ == '__main__':
    run()
