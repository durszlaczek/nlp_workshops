# Downloads text of parliamentary speeches from Polish Sejm and writes in csv in a format (text, name, date)
import json, urllib.request, re, csv, argparse
from bs4 import BeautifulSoup

POSIEDZENIE_URL = 'https://api-v3.mojepanstwo.pl/dane/sejm_wystapienia.json?conditions[sejm_wystapienia.posiedzenie_id]='
POSIEDZENIA_ID = range(1, 155)

def get_wystapienie(data_object):
    html = data_object['static']['html']
    soup = BeautifulSoup(html, 'html.parser')

    paragraphs = soup.find_all(['p'])
    cleaned_paragraphs = ''

    for paragraph in paragraphs:
        paragraph = re.sub(r'\([^)]*\)', '', paragraph.text)
        if paragraph != '':
            cleaned_paragraphs += ' ' + str(paragraph)

    return cleaned_paragraphs, \
           data_object['data']['ludzie.nazwa'], \
           data_object['data']['sejm_wystapienia.data']

def parse_posiedzenie(data_object):
    data = []
    for object in data_object:
        try:
            data.append(get_wystapienie(object))
        except KeyError:
            print('Something went wrong :(')
        except TypeError:
            print('Something went wrong :(')

    return data

def process(outfile):
    with open(outfile, 'w') as file:

        writer = csv.writer(file)
        writer.writerow(['text', 'name', 'date'])

        for posiedzenie_id in POSIEDZENIA_ID:
            wystapienia = []

            print('Starting processing {} posiedzenie.'.format(posiedzenie_id))

            with urllib.request.urlopen(POSIEDZENIE_URL + str(posiedzenie_id)) as url:
                data = json.loads(url.read().decode())

            wystapienia.append(parse_posiedzenie(data['Dataobject']))

            if 'next' in data['Links'].keys():
                next_url = data['Links']['next']
                while True:
                    with urllib.request.urlopen(next_url) as url:
                        data = json.loads(url.read().decode())

                    wystapienia.append(parse_posiedzenie(data['Dataobject']))
                    if not 'last' in data['Links'].keys():
                        break
                    next_url = data['Links']['next']

            for posiedzenie in wystapienia:
                for wystapienie in posiedzenie:
                    writer.writerow(wystapienie)

            print('Yay! Posiedzenie {} processed!'.format(posiedzenie_id))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--outfile', type=str,
                        help='A csv file where data will be downloaded.',
                        default='../data/wystapienia.csv')
    args = parser.parse_args()
    process(args.outfile)

