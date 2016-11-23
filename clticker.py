import sys, re, os, datetime, requests
from bs4 import BeautifulSoup

# data interested:
# price
# % increase
# previous close

to_monitor = sorted(sys.argv[1:])
to_monitor_and_indices = []

# find indices of stocks to monitor
url = requests.get('http://www.pesobility.com/stock')
soup = BeautifulSoup(url.text, 'lxml')
tr_list = soup.select('table > tbody > tr')
for index,tr in enumerate(tr_list):
	name = tr.select('a')[0].text
	if name in to_monitor:
		to_monitor_and_indices.append((name, index))

to_monitor_and_indices.sort()

start_time = datetime.datetime.now()
while True:
	curr_time = datetime.datetime.now()
	if (curr_time - start_time).seconds % 30 == 0: # modify 30 to change rate of updating data
		# print header
		os.system('clear') #for windows: os.system('cls')
		print('Symbol'.ljust(10),'Price'.ljust(10),'% Change'.ljust(10), 'Prev Close'.ljust(10))
		url = requests.get('http://www.pesobility.com/stock')
		soup = BeautifulSoup(url.text, 'lxml')
		tr_list = soup.select('table > tbody > tr')
		for name, index in to_monitor_and_indices:
			price_string = tr_list[index].select('td')[2].text
			price = re.search('[0-9.]+', price_string).group()
			percent = re.search('[-0-9.]+%', price_string).group()
			prev = tr_list[index].select('td')[3].text
			print(name.ljust(10),price.ljust(10),percent.ljust(10),prev)
