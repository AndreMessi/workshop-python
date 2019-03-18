from collections import deque

queue = deque(["andre","ilham","avio"])
#menambahkan data pada queue
queue.append("ramdani")
queue.append("naya_safitri")
queue.append("nurmayana")

#menghapus data pada queue =>popleft 
queue.popleft()
queue.popleft()