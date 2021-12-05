## 2,1,4,3,6,5... 이렇게 되어 있는 파일명을 1,2,3,4,5,6... 이렇게 바꾼다.
import os


file_path = 'xxx' # 원본파일들이 있는 폴더
dest_path = 'xxx_after' # 변환된 이후 파일들이 생성되는 폴더.
file_names = os.listdir(file_path)
print(file_names.sort())

i = 1
before = ''
for name in file_names:
  
  # 파일확장자는 jpg로 지정.
  temp = name.rstrip('.jpg').lstrip('0')
  print(int(temp))

  if(int(temp)%2==1):
    # 홀수 인경우, 앞에 4자리까지 0으로 채움. 예: 0001.jpg
    dst = os.path.join(dest_path, str(i+1).zfill(4) +'.jpg')
  else:
    dst = os.path.join(dest_path, str(i-1).zfill(4) +'.jpg')

  src = os.path.join(file_path, name)

  os.rename(src, dst)
  print(dst)
  i += 1
