form bs4 import *
import requests 
import os

#create forlder 
 def folder_create(images) :   #function
     try:
            folder_ name == input("Enter folder name :- ")
            #folder creation 
            os.mkdir(folder_name)

    # if folder exists with that name , ask another name 
    except:
        print("folder exist with that name!")
        folder_create()

    #image downloading start 
     download-image(image,folder_name)

#dowload all images from that url
def download_images(images, folder_name):

        #initial count is zero
        count=0
        #print total images found in url
        print(f"Total {len(images)} Image found!")

        #checking if images is not zero
        if len(images) != 0:
            for i,image in enumerate(images):
                #from image tag,fetch image dource url
                 #data-srcset
                 #data-src
                 #data-fallback-src
                 #src
                #here we will use exceptional handling
                # first we will search for "data-srcset" in img tag 
                try:
                    # in image tag, searching for "data-srcset"
                    image_link = image["data-srcset"]
                     # then we will search for "data-src" in img  
                     # tag and so on.. 
                     except:
                         try:
                              # In image tag ,searching for "data-src"
                              image_link = image["data-src"]
                         except:
                             try:
                                  # In image tag ,searching for "src" 
                                    image_link = image["data-fallback-src"] 
                             except: 
                                try: 
                                    # In image tag ,searching for "src" 
                                    image_link = image["src"] 
        
                                # if no Source URL found 
                                except: 
                                    pass           

            # After getting Image Source URL 
            # We will try to get the content of image 

             try:
                 r = requests.get(image_link).content
                 try:
                     #responsibility of decode
                     r = str(r,'utf-8')

                 except UnicodeDecodeError:
                     # After checking above condition, Image Download start 
                     with open(f"{folder_name}/images{i+1}.jpg","wb+") as f:
                        f.write(r)
 # counting number of image downloaded 
                    count +=1
            except:
                pass

       # There might be possible, that all 
        # images not download 
        # if all images download 

        if count == len(images):
            print("All Images Downloaded!")

          # if all images not download   
        else:
            print(f"Total {count} Images Downloaded out of {len(images)}")

# MAIN FUNCTION START 
def main(url):
    # content of URL 
    r = request.get(url)

    #parse html code
    soup = BeautifullSoup(r.text,'html.parse')

    # find all images in URL 
    images = soup.findAll('img')

    #   # Call folder create function 
    folder_create(images)


# take url 
url = imput("Enter URL :- ")

# CALL MAIN FUNCTION 
main(url)