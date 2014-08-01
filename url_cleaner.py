welcome_msg = '''url_cleaner is a poor man's CleanLinks.
See: https://itunes.apple.com/us/app/clean-links/id623671942?mt=8
It takes a shortened url and returns the lengthened, cleaned url.
The inbound shortened url can either be provided as a command line
argument or on the iOS clipboard.

url_cleaner follows all header redirects, instead of downloading
the entire webpage as CleanLinks does,
(See: https://twitter.com/gcaprio/status/418040618636435456)
which 1) saves you bandwidth and 2) doesn't register as a click (at least for bit.ly)

It also has optional support for LaunchCenterPro if it is installed.

Source code at: https://gist.github.com/HyShai/e0a83811d8c635bd226f'''

import urllib, clipboard, re, requests, webbrowser, sys

def url_lengthen(url): # recursively lengthen the url
	
	new_url = requests.head(url).headers.get('location')
	return url_lengthen(new_url) if new_url else url

url = sys.argv[1] if len(sys.argv) > 1 else clipboard.get()

if url:
	url = url_lengthen(url)
else:
	print(welcome_msg)
        sys.exit()

#strip analytics garbage
url = re.sub(r'(?<=\&)?utm\w+=[^\&]+(\&)?','',url)

if webbrowser.can_open('launch://'):
	params = urllib.quote('[prompt:Set Clipboard=%s]' % url)
	launch = 'launch://clipboard?text=%s' % params
	webbrowser.open(launch)
else: 
	print 'Copying'
        console.write_link(url, url)
        print 'to the clipboard'
	clipboard.set(url)
