import requests 

url = input("Enter Url :")


def file_name(url):
    url = url.strip()
    if "/" in url :
        file_name = url.split("/")[-1]
        return file_name 
    else:
        print("Enter a valid URL")

def download():
    name = file_name(url)
    response = requests.get(url)
    if response.ok: 
        with open (name , "wb") as download_file :
            download_file.write(response.content)
        
            
if __name__ == "__main__":
    download()

    
