from django.core.management.base import BaseCommand, CommandError
from django.db import models
import os
import requests,re,time
from ...models import Allip    
class Command(BaseCommand):


    def handle(self, *args, **options):


    	fp=open('HttpAgent.txt','w') 
	head={'User-Agent':'Mozilla/5.0'}

	i=0
	for i in xrange(1,60):#page 1 to page 60
	    url='http://www.xici.net.co/nt/'+str(i) 

	    resp=requests.get(url,headers = head)

	    s=resp.content

	    ip_re = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).+\n.+>(\d{1,5})<')
	    ip_port = re.findall(ip_re,s)


	    for x in ip_port:
	        all_ip=x[0]+':'+x[1]   
	        print all_ip
	        a=Allip(all_ip=all_ip)
		a.save()

	        #fp.write(all_ip+"\t")
	        #time.sleep(0.005)
	fp.close()
	

