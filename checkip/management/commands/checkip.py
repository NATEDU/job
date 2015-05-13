from django.core.management.base import BaseCommand, CommandError
from django.db import models
import os
import random
import requests,re,urllib2,time,MySQLdb
from BeautifulSoup import BeautifulSoup
from ...models import check_all_ip
from getip.models import Allip

class Command(BaseCommand):

     def handle(self, *args, **options):
 	#f=open('HttpAgent.txt','r')
	#ip_port=f.readline().strip(' ').split('\t')
	#f.close()
	
	allip_list=[]
	okip_list=[]
	noip_list=[]
	a=Allip.objects.all()
	for x in a:
		allip_list.append(x.all_ip)
	randomNumber=raw_input('Enter TestNumber 1-6000:')
	for prox in random.sample(allip_list,int(randomNumber)):
	#for prox in allip_list[33:55]:
	    try:
	        
	        proxies = {'http':prox}
	        d={'User-Agent':'Mozilla/5.0'}
	                
	        Tm_url="http://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.1.rSdc3y&id=40272354595&skuId=79919655679&areaId=110100&cat_id=50024400&rn=e5646f8d017a52f375b52f3ba95935ab&standard=1&user_id=1714128138&is_b=1"
	        resp=requests.get(Tm_url,proxies=proxies,headers =d,timeout=0.2)
	        s=resp.content
	        
	        #bs=BeautifulSoup(s)
	        #name=bs.find('h1',{'data-spm':'1000983'}).text
	        
	        offset=s.find('tb-detail-hd')
	        name=s[offset+171:offset+197]
	        #print name
	        if  offset > -1 and name !='':
	            print name
	            print(prox, 'ok')
	            okip_list.append(prox)
	        else:
	            print(prox, 'not ok')
	            noip_list.append(prox)                            
	    except:
	     
	        pass
	print 'okip_list',okip_list
	print 'noip_list',noip_list        
	for okip in okip_list:    
		i=check_all_ip(ip=okip,test_ip=True)
		i.save()
	for noip in noip_list:
		i=check_all_ip(ip=noip,test_ip=False)
		i.save()	