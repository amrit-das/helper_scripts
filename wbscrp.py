import time 
import sys
import urllib2
import os
search_keyword = [sys.argv[1]]

    								# search_keyword.append(raw_input("Enter the search parameter: ")) 
keywords = [' ']
download_path = 'dataset/'+ search_keyword[0]
c = 100
def download_page(url):
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    req = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(req)
    page = response.read()
    return page
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+1)
        end_content = s.find(',"ow"',start_content+1)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content
def _images_get_all_items(page):
    global c
    items = []
    d = 0
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links" or d == c:
            break
        else:
            d=d+1
            items.append(item)      #Append all the links in the list named 'Links'
            time.sleep(0.1)         #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items
t0 = time.time()   					#start the timer
i= 0
while i<len(search_keyword):

    items = []
    iteration = "Item no.: " + str(i+1) + " Item name = " + str(search_keyword[i])
    print (iteration)
    print ("Hey There! Please Wait... Just a sec")
    search_keywords = search_keyword[i]
    search = search_keywords.replace(' ','%20')
    j = 0
    while j<len(keywords):
        pure_keyword = keywords[j].replace(' ','%20')
        url = 'https://www.google.com/search?q=' + search + pure_keyword + '&espv=2&biw=1366&bih=667&site=webhp&source=lnms&tbm=isch&sa=X&ei=XosDVaCXD8TasATItgE&ved=0CAcQ_AUoAg'
        raw_html =  (download_page(url))
        time.sleep(0.1)
        items = items + (_images_get_all_items(raw_html))
        j = j + 1
    								#print ("Image Links = "+str(items))
    print ("Total Image Links = "+str(len(items)))
    print ("\n")
    i = i+1
    								#This allows you to write all the links into a test file. This text file will be created in the same directory as your code. You can comment out the below 3 lines to stop writing the output to the text file.
    info = open('output.txt', 'a')  #Open the text file called database.txt
    info.write(str(i) + ': ' + str(search_keyword[i-1]) + ": " + str(items) + "\n\n\n")         #Write the title of the page
    info.close()                    #Close the file
t1 = time.time()    				#stop the timer
total_time = t1-t0   				#Calculating the total time required to crawl, find and download all the links of 60,000 images
print ("Starting Download...")
k=0
errorCount=0
if not os.path.exists(download_path):
        os.makedirs(download_path)
while(k<len(items)):
    from urllib2 import Request,urlopen
    from urllib2 import URLError, HTTPError

    try:
        req = Request(items[k], headers={"User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"})
        response = urlopen(req)
        output_file = open(download_path+'/' + "_"+str(k+1)+".jpg",'wb')
        data = response.read()
        output_file.write(data)
        response.close();

        print("completed ====> "+str(k+1))

        k=k+1;

    except IOError:   				#If there is any IOError

        errorCount+=1
        print("Network Error "+str(k+1))
        k=k+1;

    except HTTPError as e:  		#If there is any HTTPError

        errorCount+=1
        print("HTTPError"+str(k))
        k=k+1;
    except URLError as e:

        errorCount+=1
        print("URLError "+str(k))
        k=k+1;

print("\n")
print("All are downloaded")
print("\n"+str(errorCount)+" ----> total Errors")
