import urllib.request
import json
import re

titles = list()
times = ['time', 'times']
spaces = ['space', 'spaces']
timeResult = list()
spaceResult = list()
if __name__ == '__main__':
    ######### Pull data from api
    url = 'https://www.sfmoma.org/api/collection/artworks/?page='
    all_page = 0
    for pageNumber in range(1,2):
        response = urllib.request.urlopen(urllib.request.Request(url+str(pageNumber), headers={'Authorization': 'Token 3b05f066aeef64644d259f651eee06c148a86ee0', 'Range': 'bytes=100-'}))
        data = json.loads(response.read())
        all_page = data['count']
    all_page = int((all_page-1)/20)+1
    for pageNumber in range(1,all_page+1):
        print(pageNumber)
        response = urllib.request.urlopen(urllib.request.Request(url+str(pageNumber), headers={'Authorization': 'Token 3b05f066aeef64644d259f651eee06c148a86ee0', 'Range': 'bytes=100-'}))
        data = json.loads(response.read())
        for artwork in data['results']:
            titles.append(artwork['title']['display'])
            title = str(artwork['title']['display']).lower()
            
            ## Check for 'time'
            re_pattern = r'\btime.*?\b'
            check = re.findall(re_pattern, title)
            for ele in check:
                if ele in times:
                    artists = ''
                    for artist in artwork['artists']:
                        artists+=str(artist['artist']['name_display'])+','
                    data = str(artwork['title']['display']) + ',' + str(artwork['date']['display']) + ',' +artists +str(artwork['origin']['country']) + '\n'
                    timeResult.append(data)
                    break

            ## Check for 'space'
            re_pattern = r'\bspace.*?\b'
            check = re.findall(re_pattern, title)
            for ele in check:
                if ele in spaces:
                    artists = ''
                    for artist in artwork['artists']:
                        artists+=str(artist['artist']['name_display'])+','
                    data = str(artwork['title']['display']) + ',' + str(artwork['date']['display']) + ',' +artists +str(artwork['origin']['country']) + '\n'
                    spaceResult.append(data)
                    break
    with open('titles.txt', 'w', encoding="utf8") as writer:
        for ele in titles:
            writer.write(ele+'\n')
    with open('timeResult.txt', 'w', encoding="utf8") as writer1:
        for ele in timeResult:
            writer1.write(ele)
    with open('spaceResult.txt', 'w', encoding="utf8") as writer2:
        for ele in spaceResult:
            writer2.write(ele)