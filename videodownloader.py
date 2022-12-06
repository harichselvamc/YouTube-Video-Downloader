def Downloader():
  import pytube # Import library
  url=input("Please paste your youtube link : ") # Take url from user
  MediaType=input("Mp3 or Mp4 ? : ") # I add two option Mp3 and mP4 
  path="/" # My video or Mp3 file will dowload ths path.
  if MediaType=='mp4': # Case 1 if my mediatype is Mp4
    print("Mp4 file is downloading...")
    pytube.YouTube(url).streams.get_highest_resolution().download(output_path=path,filename="video.mp4") # then download Mp4 file.
  else:
    print("Mp3 file is downloading...") #İf is not Mp4 so if is it mp3
    pytube.YouTube(url).streams.get_audio_only().download(output_path=path,filename="video.mp3") # then download Mp3 file.
  return('Download finished.')  


Downloader()