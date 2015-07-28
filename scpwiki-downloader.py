# Downloads every scp page at www.scp-wiki.net
# and stores every page in an archive.
import urllib
import urllib.error
import urllib.request
import os
import zipfile
import datetime
import time


def main():
    scp_zip = create_zip()
    i = 1
    while i < 3000:
        page = select_page(i)
        url = set_url(page)
        try:
            status = "Downloading "
            status += page
            print(status)
            download_page(url, page)
        except urllib.error.URLError:  # Move on to next page if the current page does not exist.
            print("Download failed, moving on to next page...")
            i += 1
        else:
            print("Download Successful")
            compress_page(scp_zip, page)
            i += 1
        time.sleep(0.35)  # Wikidot allows 3 requests per second.


def create_zip():
    current_date = datetime.date.today().strftime("%d-%B-%Y")
    zip_name = "SCPWiki_"
    zip_name += str(current_date)
    zip_name += ".zip"
    print(zip_name)
    scp_zip = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
    return scp_zip


def select_page(i):  # Format the page correctly depending on the number of digits of the selected SCP.

    if i < 10:
        page = "scp-00"
        page += str(i)
    elif i < 100:
        page = "scp-0"
        page += str(i)
    else:
        page = "scp-"
        page += str(i)
    return page


def set_url(page):

    url = "http://www.scp-wiki.net/"
    url += page
    return url


def download_page(url, page):

    page += '.html'
    urllib.request.urlretrieve(url, page)  # Download and save page as scp-x.html.


def compress_page(scp_zip, page):

    page += ".html"
    scp_zip.write(page)
    os.remove(page)


if __name__ == '__main__':
    main()

