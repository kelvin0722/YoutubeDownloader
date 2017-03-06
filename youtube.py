import pafy
url = "https://www.youtube.com/watch?v=Z9eMk051dYg"
myvid = pafy.new(url)
path = "/Users/Badmind/Downloads"
 
print(myvid.viewcount)

try:
    best_vid = myvid.getbest()
   
    best_vid.download(filepath=path,quiet=False)    
except (WinError, FileExistsError) as e:
    print("%s"%e)




