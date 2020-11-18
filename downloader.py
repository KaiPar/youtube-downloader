from pytube import YouTube

def download(url, path):
    YouTube(url).streams.first().download(path)

def main():
    url = input("Enter the youtube video URL: ")
    path = input("Enter the path where you want to save your video: ")

    try:
        download(url, path)
    except KeyboardInterrupt:
        print("Terminating Program...")
        exit()
    except:
        print ("Something went worng. Please try again.")
        print ("The possible issues are: ")
        print ("1. The path provided is invalid.")
        print ("2. The URL provided is invalid.")
        exit()

    print("Video downloaded to", path) 

if __name__ == '__main__':
    main()