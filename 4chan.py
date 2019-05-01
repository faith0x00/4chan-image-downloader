import requests
import json
import sys
import wget

if __name__ == '__main__':
	# try:
		# sys.argv[1]
		# sys.argv[2]
	# except:
		# print('Usage: {} {}'.format(sys.argv[0], '<board>/<thread_id>'))
		# exit(1)
		
	# board = sys.argv[1].split('/')[0]
	# thread_id = sys.argv[1].split('/')[1]
	
	i = input('<board>/<thread_id>: ')
	board = i.split('/')[0]
	thread_id = i.split('/')[1]
	
	img_url = 'https://i.4cdn.org/{}/{}{}'
	
	req = requests.get('https://a.4cdn.org/{}/thread/{}.json'.format(board, thread_id))
	data = json.loads(req.content)
	
	for x in data['posts']:
		
		try:
			wget.download( img_url.format(board, x['tim'], x['ext']) )
		except KeyError:
			pass