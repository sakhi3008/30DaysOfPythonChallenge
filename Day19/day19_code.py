# Challenge - Download multiple files concurrently using threads
import threading
import requests

urls = [
    "https://www.gutenberg.org/files/1342/1342-0.txt",
    "https://www.gutenberg.org/files/84/84-0.txt"]
def download_file(url, index):
    print(f"🔽 Starting download {index+1}")
    response = requests.get(url)
    filename = f"book_{index+1}.txt"
    
    with open(filename, "wb") as f:
        f.write(response.content)
    print(f"✅ Download {index+1} complete: {filename}")

# Create and start threads
threads = []
for i, url in enumerate(urls):
    thread = threading.Thread(target=download_file, args=(url, i))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("🚀 All downloads completed.")
