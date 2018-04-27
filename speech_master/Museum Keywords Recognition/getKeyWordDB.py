import urllib.request
import json
import re

titles = {'Las Vegas, 1989 Day Time': '',
          'One Day At A Time, from the series Advice from my 80 Year-Old-Self': '',
          'Gatun Dinner Time': '',
            'Dual Time clock': '',
            'Earthrise Seen for the First Time By Human Eyes, from the series Full Moon by Michael Light': '',
            'Leaves Frozen in Time': '',
            'Haying Time': '',
            'Who Invented Time?': '',
            'Diomedes Islands (Islands of Time)': '',
            'Long Time Ago': '',
            'Lunch Time': '',
            'Marking Time': '',
            'Now Time issue no. 2': '',
            'Sundial of Our Time': '',
            'A Portrait of Time II': '',
            'A Portrait of Time IX': '',
            'Quality Time': '',
            'Riffs on Real Time (1 of 10)': '',
            'The Refusal of Time [spool]': '',
            'The Refusal of Time [MacMini]': '',
            'The Refusal of Time': '',
            'Sculptured Time, from the portfolio, Earth Edges': '',
            'Sea, Rocks, Time': '',
            'Three Sections of Time, #1 Hoctún, Yucatan, Mexico 1994': '',
            'Two Sections of Time, #1 San Pedro, Yucatán, México': '',
            'Three Sections of Time, #2 Hoctún, Yucatan, Mexico 1996': '',
            'Three Sections of Time, #3 Hoctún, Yucatan, Mexico 1999': '',
            'Two Sections of Time, #2 San Pedro, Yucatán, México': '',
            'Mutación en Espacio-Tiempo (Mutation in Space-Time)': '',
            'Spirit of Time VII (Zeitgeist VII)': '',
            'Sonia in Time, from the portfolio Photographs from The School of The Art Institute of Chicago': '',
            'Stopping Time: The Photographs of Harold Edgerton': '',
            'Tea Time': '',
            'Caribbean Tea Time': '',
            'In Vacation Time': '',
            'Time Capsule Tryptich': '',
            'Time on a Curved Line': '',
            'Opposing Mirrors and Video Monitors on Time Delay': '',
            'Time in Blue No. 25': '',
            'Time Equals 36 Exposures': '',
            'Time Expired': '',
            'The Time Inbetween': '',
            'Time Lapse of Eclipse': '',
            'Time Line': '',
            "Time Line. Boundary between USA/Canada along St. John River; Fort Kent, Maine. 1' x 3' x 3 mile cut between the two countries": '',
            'Time Peace I': '',
            'Change in Time and Place': '',
            'Time/Life Screen: Working Model': '',
            'Time Inc. Ventures Volume/Vibe Media Kit Brochure': '',
            'Sunset on the Time Zone': '',
            'Three Time Zone clock': ''
}
result = list()
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
            title = artwork['title']['display']
            if title in titles:
                print(title)
                artists=""
                for artist in artwork['artists'][:-1]:
                    artists+=str(artist['artist']['name_display'])+'-'
                artists+=str(artwork['artists'][-1]['artist']['name_display'])
                if len(artwork['images']) == 0:
                    lst = str(artwork['title']['display']) + '#' + str(artwork['date']['display']) + '#' +artists+"#" +str(artwork['origin']['country'])
                else:
                    lst = str(artwork['title']['display']) + '#' + str(artwork['date']['display']) + '#' +artists+"#" +str(artwork['origin']['country']) +"#"+str(artwork['images'][0]['public_image'])
                result.append(lst)
            
    with open('updatedDB.txt', 'w', encoding="utf8") as writer:
        for ele in result:
            writer.write(ele+'\n')