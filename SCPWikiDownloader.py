# Downloads every scp page at www.scp-wiki.net
# and stores every page in an archive.
import urllib
import urllib.error
import urllib.request
import os
import zipfile
my_zip = zipfile.ZipFile('SCPWiki.zip', 'w', zipfile.ZIP_DEFLATED)


def save_wiki(i):

    while i < 3000:  # The wiki has up to 2999 SCPs as of 26/07/2015.
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
            print(status)
            page += '.html'
            urllib.request.urlretrieve(url, page)  # Download and save page as scp-x.html.
        except urllib.error.URLError:
            print("Download failed, page does not exist")
            i += 1
            save_wiki(i)  # If page does not exist, move on to next page.
        else:
            print("Download Successful")
        i += 1
        my_zip.write(page)
        os.remove(page)
save_wiki(1)
