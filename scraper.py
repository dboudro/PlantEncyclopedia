import wikipedia
import csv
from bs4 import BeautifulSoup
import re

counter = 0

allPlants = wikipedia.page("List_of_garden_plants")
soup = BeautifulSoup(allPlants.html(), 'html.parser')
# if the link is red
# if the link title contains the word page does not exist

items = soup.find_all('li')
plants = []
for li in items:
    if li.find('i') and re.search("^\S*$", li.find('a')['title']):
        plants.append(li.find('a')['title'])


def loadPage(plant):
    if plant in skipplants:
        print 'skipped'
        return 'skipped'
    else:
        global counter
        print "scraping " + str(plant) + " " + str(counter)
        counter += 1
        plantPage = wikipedia.page(plant)
        soup = BeautifulSoup(plantPage.html(), 'html.parser')

        # image
        imageSpan = soup.find("a", class_="image")
        if imageSpan:
            imageTag = imageSpan.find('img')
            if imageTag:
                image = 'https:' + imageTag['src']
            else:
                image = 'none'
        else:
            image = 'none'

        # intro paragraph
        bodyContent = soup.find('p')
        if bodyContent:
            secondP = bodyContent
            if secondP:
                print secondP
                paragraph = secondP
            else:
                paragraph = 'there are not 2 paragraphs'
        else:
            paragraph = 'there is not a paragraph'

        # order
        orderSpan = soup.find("span", class_="order")
        if orderSpan:
            orderAnchor = orderSpan.find('a')
            orderItalic = orderSpan.find('i')
            if orderAnchor:
                order = orderAnchor.contents[0]
            elif orderItalic:
                order = orderItalic.contents[0]
            else:
                order = 'none'
        else:
            order = 'none'

        # family
        familySpan = soup.find("span", class_="family")
        if familySpan:
            familyAnchor = familySpan.find('a')
            familyItalic = familySpan.find('i')
            if familyAnchor:
                family = familyAnchor.contents[0]
            elif familyItalic:
                family = familyItalic.contents[0]
            else:
                family = 'none'
        else:
            family = 'none'

        # genus
        genusSpan = soup.find("span", class_="genus")
        if genusSpan:
            genusAnchor = genusSpan.find('a')
            genusItalic = genusSpan.find('i')
            genusBold = genusSpan.find('b')
            if genusAnchor:
                genus = genusAnchor.contents[0]
            elif genusItalic:
                if genusBold:
                    genus = genusBold.contents[0]
                else:
                    genus = genusItalic.contents[0]
            else:
                genus = 'none'
        else:
            genus = 'none'

        # species
        speciesSpan = soup.find("span", class_="species")
        if speciesSpan:
            speciesAnchor = speciesSpan.find('a')
            speciesItalic = speciesSpan.find('i')
            if speciesAnchor:
                species = speciesAnchor.contents[0]
            elif speciesItalic:
                species = speciesItalic.contents[0]
            else:
                species = 'none'
        else:
            species = "none"

        # scientific name
        scientificSpan = soup.find("span", class_="binomial")
        if scientificSpan:
            scientificAnchor = scientificSpan.find('a')
            scientificItalic = scientificSpan.find('i')
            if scientificAnchor:
                scientific = scientificAnchor.contents[0]
            elif scientificItalic:
                scientific = scientificItalic.contents[0]
            else:
                scientific = 'none'
        else:
            scientific = 'none'
            return ['myid', plant.encode('utf-8'), scientific.encode('utf-8'),
                    order.encode('utf-8'), family.encode('utf-8'),
                    genus.encode('utf-8'), species.encode('utf-8'),
                    image.encode('utf-8'), paragraph.encode('utf-8')]


csvData = []

# header
csvData.append(['id', 'name', 'scientific', 'order', 'family', 'genus',
                'species', 'image', 'paragraph'])

# list of plants to skip due to irregular formatting
skipplants = ['Bursaria', 'Carnegiea', 'Hohenbergiopsis', 'Ledum', 'Rochea',
              'Sollya', 'Wigginsia', 'Borago', 'Bracteantha', 'Dizygotheca',
              'Homeria', 'Lemboglossum', 'Urginea']

# for testing
# plants = ['Adonis', 'Adromischus', 'Aechmea', 'Aegopodium', 'Aeonium']

for plant in plants:
    csvData.append(loadPage(plant))
    print 'loaded ' + str(plant)

with open('plantOutput.csv', 'wb') as f:
    wtr = csv.writer(f, delimiter=',')
    wtr.writerows(csvData)
