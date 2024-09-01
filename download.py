import requests
import os

def file_name(url):
    url = url.strip()
    if "/" in url:
        name = url.split("/")[-1]
        # Validate and sanitize the file name
        name = name if name else "downloaded_file"
        return name
    else:
        raise ValueError("Enter a valid URL")

def download(url):
    try:
        name = file_name(url)
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        
        # Ensure the file name is safe for the file system
        name = os.path.basename(name)
        
        with open(name, "wb") as download_file:
            download_file.write(response.content)
        
        print(f"Downloaded file saved as: {name}")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while downloading the file: {e}")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    url = input("Enter URL: ")
    download(url)
