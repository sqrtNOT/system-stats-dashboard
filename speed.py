#!/usr/bin/python
import speedtest as sp
import os
#create speedtest object and run tests
s = sp.Speedtest()
s.download()
s.upload()

#extract data we care about to local variables
data=s.results.dict()
download = data['download']
upload = data['upload']
ping = data['ping']
timestamp = data['timestamp'] #only used when writing to backup file

#print result to stdout for running oneoff tests from the cli in gbps
print(f'ping:{ping}\tup:{int(upload)/1024**3}\tdown:{int(download)/1024**3}\ttimestamp:{timestamp}')

#add results to locally hosted database
try:
	import mysql.connector
	conn=mysql.connector.connect(user='speedy',password='htI3V03xesIcATC8gsuTVd5eM5ImyddgxrvNw3bVjcat3QtK',host='localhost',database='stats')
	cursor=conn.cursor()
	insert=f'INSERT INTO speedtest (ping, download, upload) values ({ping},{download},{upload});'
	cursor.execute(insert)
	conn.commit()
	conn.close()

#if database is down or store the results in a local file
except:
	folder="speedtestbackup/"
	filename="speeddata"
	filepath=folder+filename
	if(not os.path.exists(filepath)):
		#first run case: create path and add header to tsv
		print("file does not exist")
		os.makedirs(folder,exist_ok=True)
		with open(filepath,"w") as outfile:
			outfile.write("ping\tupload\tdownload\ttimestamp\n")
			outfile.write(f'{ping}\t{upload}\t{download}\t{timestamp}\n')

	else:
		#otherwise just append data to existing file
		print("file does exist")
		with open(filepath,"a") as outfile:
			outfile.write(f'{ping}\t{upload}\t{download}\t{timestamp}\n')
