from pytube import YouTube

def download(url, path):
    YouTube(url).streams.first().download(path)

def main():
    url = input("Enter the youtube video URL: ")
    path = input("Enter the path where you want to save your video: ")
    download(url, path)   

if __name__ == '__main__':
    main()  