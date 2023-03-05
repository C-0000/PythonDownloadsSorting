import os
import shutil

current_dir = r'C:\Users\korne\Downloads'

for f in os.listdir(current_dir):
    filename, file_extension = os.path.splitext(f)
    
    try:
        if not file_extension:
            pass
        elif file_extension in '.mp4' or file_extension in '.mov':
            shutil.move(
                os.path.join(current_dir, f'{filename   }{file_extension}'),
                os.path.join(current_dir, 'Video', f'{filename   }{file_extension}')
            )       
        elif file_extension in '.mp3' or file_extension in '.wav':
            shutil.move(
                os.path.join(current_dir, f'{filename   }{file_extension}'),
                os.path.join(current_dir, 'Musik', f'{filename   }{file_extension}')
            )   
        elif file_extension in '.jpg' or file_extension in '.png' or file_extension in '.jpeg' or file_extension in '.webp' or file_extension in '.gif' or file_extension in '.PNG' or file_extension in '.JPG' or file_extension in '.JPEG' or file_extension in '.PNG' or file_extension in '.jfif':
            shutil.move(
                os.path.join(current_dir, f'{filename   }{file_extension}'),
                os.path.join(current_dir, 'Bild', f'{filename   }{file_extension}')
            )   
        elif file_extension in '.zip' or file_extension in '.7z' or file_extension in '.rar':
            shutil.move(
                os.path.join(current_dir, f'{filename   }{file_extension}'),
                os.path.join(current_dir, 'Zip', f'{filename   }{file_extension}')
            )   
        elif file_extension in '.exe':
            shutil.move(
                os.path.join(current_dir, f'{filename   }{file_extension}'),
                os.path.join(current_dir, 'Exe', f'{filename   }{file_extension}')
            )   
        elif file_extension in '.pdf':
            shutil.move(
                os.path.join(current_dir, f'{filename   }{file_extension}'),
                os.path.join(current_dir, 'Pdf', f'{filename   }{file_extension}')
            )   
        elif file_extension in '.ods' or file_extension in '.csv' or file_extension in '.xlsx':
            shutil.move(
                os.path.join(current_dir, f'{filename   }{file_extension}'),
                os.path.join(current_dir, 'Excel', f'{filename   }{file_extension}')
            )   
        elif file_extension in '.odt' or file_extension in '.docx' or file_extension in '.doc' or file_extension in '.rtf':
            shutil.move(
                os.path.join(current_dir, f'{filename   }{file_extension}'),
                os.path.join(current_dir, 'Word', f'{filename   }{file_extension}')
            )   
        elif file_extension in '.torrent':
            shutil.move(
                os.path.join(current_dir, f'{filename   }{file_extension}'),
                os.path.join(current_dir, 'Torrent', f'{filename   }{file_extension}')
            )   
        elif file_extension in '.txt':
            shutil.move(
                os.path.join(current_dir, f'{filename   }{file_extension}'),
                os.path.join(current_dir, 'Txt', f'{filename   }{file_extension}')
            )   
        elif file_extension in '.jar':
            shutil.move(
                os.path.join(current_dir, f'{filename   }{file_extension}'),
                os.path.join(current_dir, 'Jar', f'{filename   }{file_extension}')
            )   
        elif file_extension in '.pptx' or file_extension in '.ppt' or file_extension in '.odp':
            shutil.move(
                os.path.join(current_dir, f'{filename   }{file_extension}'),
                os.path.join(current_dir, 'Powerpoint', f'{filename   }{file_extension}')
            )   
        
        
    except    (FileNotFoundError, PermissionError):
        pass
    
    
    