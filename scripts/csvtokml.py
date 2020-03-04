import csv
import xml.dom.minidom
import sys

def createPlacemark(kmlDoc, row, order):
    placemarkElement = kmlDoc.createElement('Placemark')

    nameElement = kmlDoc.createElement('name')
    placemarkElement.appendChild(nameElement)
    name = kmlDoc.createTextNode(row["Name"])
    nameElement.appendChild(name)

    descElement = kmlDoc.createElement('description')
    placemarkElement.appendChild(descElement)
    desc = kmlDoc.createTextNode(row["Description"])
    descElement.appendChild(desc)

    pointElement = kmlDoc.createElement('Point')
    placemarkElement.appendChild(pointElement)
    coorElement = kmlDoc.createElement('coordinates')
    coorElement.appendChild(kmlDoc.createTextNode(row["Longitude"] + ", " + row["Latitude"]))
    pointElement.appendChild(coorElement)

    return placemarkElement

def createKML(csvReader, fileName, order):
    kmlDoc = xml.dom.minidom.Document()
    kmlElement = kmlDoc.createElementNS('http://earth.google.com/kml/2.2', 'kml')
    kmlElement.setAttribute('xmlns','http://earth.google.com/kml/2.2')
    kmlElement = kmlDoc.appendChild(kmlElement)
    documentElement = kmlDoc.createElement('Document')
    documentElement = kmlElement.appendChild(documentElement)

    next(csvReader)

    for row in csvReader:
        placemarkElement = createPlacemark(kmlDoc, row, order)
        documentElement.appendChild(placemarkElement)
    kmlFile = open(fileName, 'wb')
    kmlFile.write(kmlDoc.toprettyxml('\t', newl = '\n', encoding = 'utf-8'))

def main():
    csvFile = input("Enter name of file for conversion: ")
    if len(sys.argv) >1: order = sys.argv[1].split(',')
    else: order = ['Name', 'Description', 'Latitude', 'Longitude']
    csvreader = csv.DictReader(open(csvFile),order)
    kml = createKML(csvreader, csvFile[:-4] + ".kml", order)
    print("Saved to " + csvFile[:-4] + ".kml")
if __name__ == '__main__':
    main()
