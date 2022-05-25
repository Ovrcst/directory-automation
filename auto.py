import os
import shutil
import sys


if len(sys.argv) < 2:
    print("Please Input Path to Directory\nExample: 'C:\\path\\to\\dir'")
    exit()

path = str(sys.argv[1])
images = ['png','jpeg','gif','jpg','jpe','jfif']
videos = ['mov','mp4','wmv','avi','flv','mkv','webm']
audio = ['m4a','mp3','flac','wav','wma','aac']
documents = ['docx','doc','pdf','odt','rtf','txt','pptx','ppt','rtf']

#while(True):
for item in os.listdir(path):
    complete_path = os.path.join(path,item)
    if(os.path.isdir(complete_path)):
        continue
    try:
        if(item.lower().endswith(tuple(images))):
            to_create = 'Images'
            os.rename(f'{path}\{item}',f'{path}\{to_create}\{item}')\

        elif(item.lower().endswith(tuple(audio))):
            to_create = 'Audio'
            shutil.move(f'{path}\{item}',f'{path}\{to_create}\{item}')

        elif(item.lower().endswith(tuple(documents))):
            to_create = 'Documents'
            shutil.move(f'{path}\{item}',f'{path}\{to_create}\{item}')

        elif(item.lower().endswith(tuple(videos))):
            to_create = 'Videos'
            shutil.move(f'{path}\{item}',f'{path}\{to_create}\{item}')
        else:
            to_create = 'Others'
            shutil.move(f'{path}\{item}',f'{path}\{to_create}\{item}')


    except FileNotFoundError:
        os.mkdir(f'{path}\{to_create}')

        
    except FileExistsError:
        if(os.path.exists(f'{path}\{to_create}\{item}') and not os.path.exists(f'{path}\{to_create}\(Copy){item}')):
            shutil.move(f'{path}\{item}', f'{path}\{to_create}\(Copy){item}')
            continue
        else:
            count = 1
            while(os.path.exists(f'{path}\{to_create}\(Copy{count}){item}')):
                count += 1
            shutil.move(f'{path}\{item}', f'{path}\{to_create}\(Copy{count}){item}')


    except PermissionError as e:
        print(e)
        continue

print("Finished Successfully")