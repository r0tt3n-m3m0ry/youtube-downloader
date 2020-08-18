# YouTube video downloader
# Created by ObossaniyNarik
# Special for K0nCH3nN1Y

try:
    import youtube_dl
except:
    print('You have to install requirement modules via \'$ pip3 install -r requirements.txt\' before run this script.'); exit()

import os

with open(input('Enter name of file which contain the videos data: ')) as file_with_links:
    for file_string in file_with_links:
        if file_string[0] == '\n' or file_string[0] == ' ' or file_string[0] == '#':
            pass
        else:
            link = file_string.split(' <<>> ')[0]
            author = file_string.split(' <<>> ')[-1]

            try:
                os.mkdir(author)
            except OSError:
                pass

            os.chdir(author)
            os.system(f'youtube-dl -i {link}')
            os.chdir('..')
