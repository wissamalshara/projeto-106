import os
import cv2

path = "imagens105-main/"
images = []

for file in os.listdir(path):
  name, ext = os.path.splitext(file)
  if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)

count = len(images)
frames = cv2.imread(images[0])

height, width, channels = frames.shape
size = (width, height)
print(size)
out = cv2.VideoWriter("project.avi", cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)
for i in range(count-1, 0, -1):
 frame = cv2.imread(images[i])
 out.write(frame)

out.release()
print("Concluído")

