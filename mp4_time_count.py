# This program is used to count the total duration of all. mp4 suffix files in the specified directory
import os
from moviepy.editor import VideoFileClip         # pip install moviepy -i http://pypi.mirrors.ustc.edu.cn/simple/ --trusted-host pypi.mirrors.ustc.edu.cn

def get_all_mp4_files(directory_path):
	all_files =[]
    
	for root,dirs,files in os.walk(directory_path):
		for file in files:
			if ".mp4" in file:
				all_files.append(os.path.join(root,file))
				
	return all_files
		
def get_file_time_duration(file_name):
	clip = VideoFileClip(file_name)
	duration = clip.duration
	clip.close()
	return duration
	
if __name__ == '__main__':
	directory_path = u"./vedios/"
	mp4_files = get_all_mp4_files(directory_path)
	
	total_time = 0
	
	for file in mp4_files:
		print(file)
		total_time += get_file_time_duration(file)
	
	print("Time is {}:{}:{}.".format(
		int( total_time / 3600 ),
		int( total_time % 3600 // 60 ),
		int( total_time % 3600 % 60 )
	))
	