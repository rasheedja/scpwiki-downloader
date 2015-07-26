# Downloads every scp page at www.scp-wiki.net
# and stores every page in an archive.
import urllib
import urllib2
import os
import zipfile
import time


def save_wiki(i):

    while i < 3000:
        if i < 10:
            url = "http://www.scp-wiki.net/scp-00"
            page = "scp-00"
            url += str(i)
            page += str(i)
        elif i < 100:
            url = "http://www.scp-wiki.net/scp-0"
            page = "scp-0"
            url += str(i)
            page += str(i)
        else:
            url = "http://www.scp-wiki.net/scp-"
            page = "scp-"
            url += str(i)
            page += str(i)
        try:
            status = "Downloading "
            status += page
            print status
            scp_page = urllib2.urlopen(url)
            scp_page_content = scp_page.read()
        except urllib2.HTTPError, e:
            print "Download failed, page does not exist"
            i += 1
            save_wiki(i)
        else:
            print "Download Successful"
        page += '.html'
        with open(page, 'w') as foo:
            foo.write(scp_page_content)
        i += 1
        my_zip.write(page)
        os.remove(page)
my_zip = zipfile.ZipFile('SCPWiki.zip', 'w', zipfile.ZIP_DEFLATED)
save_wiki(1)
