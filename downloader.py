# YouTube video downloader
# Created by ObossaniyNarik
# Special for K0nCH3nN1Y

try:
    import youtube_dl
except:
    print('You have to install requirement modules via \'$ pip3 install -r requirements.txt\' before run this script.'); exit()

import os

try:   
    with open(input('Enter name of file which contain the videos data: ')) as file_with_links:
        for file_string in file_with_links:
            if file_string[0:4] != 'http': # if first four symbols in string not 'http', this is not link -> string is incorrect
                pass
            else:
                if len(file_string.split('<<>>')) != 4: # if after split() count of elements in string not four, string is incorrect
                    continue

                link = file_string.split('<<>>')[0].strip()
                content_type = file_string.split('<<>>')[1].strip()
                video_category = file_string.split('<<>>')[-2].strip()
                author = file_string.split('<<>>')[-1].strip()

                try:
                    os.makedirs(f'{video_category}\\{author}') if os.name == 'nt' else os.makedirs(f'{video_category}/{author}')
                except OSError:
                    pass

                os.chdir(f'{video_category}\\{author}') if os.name == 'nt' else os.chdir(f'{video_category}/{author}')

                if content_type == 'audio':
                    os.system(f'youtube-dl -i --extract-audio --embed-thumbnail --audio-format mp3 {link}')
                elif content_type == 'video':
                    os.system(f'youtube-dl -i {link}')
                else:
                    pass

                os.chdir('..\\..') if os.name == 'nt' else os.chdir('../..')

except FileNotFoundError:
    print('File with this name not found!'); exit()

except KeyboardInterrupt:
    print('Goodbye!'); exit()