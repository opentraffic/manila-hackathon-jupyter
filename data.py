import urllib2
import StringIO
import gzip
import os

# set of fuctions for loading data from hackathon S3 site

baseURL = "https://s3-ap-southeast-1.amazonaws.com/ph-opentraffic-data/"

# stores data locally in this directory
dataDirectory = "data/"


# call with city name ("cebu" or "manila" YYYY-MM-DD for first day (monday) of week to downalod
# e.g. getData("cebu" "2015-12-28") -> "data/week_
# returns path to decompressed file

def getData(city, week):
    
    cityUrl = baseURL + city + "/"
    filename = "week_" + week + ".csv.gz"

    cityDataDirectory = dataDirectory + city + "/"
    if not os.path.exists(cityDataDirectory):
        os.makedirs(cityDataDirectory)

    outFilePath = cityDataDirectory + filename[:-3]

    if os.path.exists(outFilePath):
        print "File " + outFilePath + " already downloaded."
        return outFilePath

    print "Downloading " + outFilePath + "..."

    response = urllib2.urlopen(cityUrl + filename)
    compressedFile = StringIO.StringIO(response.read())
    decompressedFile = gzip.GzipFile(fileobj=compressedFile)

    with open(outFilePath, 'w') as outfile:
        outfile.write(decompressedFile.read())

    num_lines = sum(1 for line in open(outFilePath))
    print "Downloaded " + outFilePath + " (" + str(num_lines) + " lines)"

    return outFilePath

def getGeoData(city):
    
    cityUrl = baseURL + city + "/"
    zipFilename = city + "_geometry.zip"
    shpFilename = city + "_geometry.shp"

    cityDataDirectory = dataDirectory + city + "/"
    if not os.path.exists(cityDataDirectory):
        os.makedirs(cityDataDirectory)

    if os.path.exists(cityDataDirectory + shpFilename): 
        print "File " + shpFilename + " already downloaded."
        return cityDataDirectory + shpFilename

    import urllib

    print "Downloanding " + shpFilename + "..."

    getFile = urllib.URLopener()
    getFile.retrieve(cityUrl + zipFilename, cityDataDirectory + zipFilename)

    import zipfile
    zip_ref = zipfile.ZipFile(cityDataDirectory + zipFilename, 'r')
    zip_ref.extractall(cityDataDirectory)
    zip_ref.close()

    os.remove(cityDataDirectory + zipFilename)

    print "Downloaded " + shpFilename 
    
    return cityDataDirectory + shpFilename
