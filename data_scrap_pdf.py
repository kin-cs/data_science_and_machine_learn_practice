'''
Scrap the Stanford CS224n lecture notes
Thank you for Professor to provide such good material on the internet
'''

from urllib.request import urlopen as uReq

def main():
	for i in range(1,9):
		download_url = "http://web.stanford.edu/class/cs224n/lecture_notes/cs224n-2017-notes{}.pdf".format(i)
		response = uReq(download_url)
		file = open("cs224n-2017-notes{}.pdf".format(i), 'wb')  # remember to use 'wb', which b means 'binary'
		file.write(response.read())
		file.close()
		print("Completed")

if __name__ == "__main__":
    main()