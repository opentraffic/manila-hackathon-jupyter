## Open Traffic Hackathon Data

This project contains information about Open Traffic data sets, plus example analysis techniques  using Python 
and Jupyter Notebook.

### Data

As part of the hackathon, OpenTraffic is making avaialble data from 2016 for Cebu and Manila metro regions. 
The data is availabe as CSV files with average traffic speeds by day and hour for each roadway segment. Additionally, a 
Shapefile contains the geometry for each roadway segment. The CSV and Shapefiles can be linked via the "edge_id" found in both files.

All data is avaiablle for download from Amazon AWS S3. Please refer to the "data_list.txt" file for a complete list of 
data files and corresponding URLs.

The example code in this project demonstrate methods for downloading and processing data files.

### Installation of Python / Jupyter environemnt

The examples in this project use Python 2.7 and the Jupyter Notebook. If you already have Python 
installed on your computer you can install Jupyter using [these instructions](http://jupyter.readthedocs.io/en/latest/install.html). 
Example code in this project makes use of the following python modules: numpy, pyshp, shapely and ipyleaflet. 

With Jupyter installed copy the contents of this project into your notebook working directory. 

Alternatively you can use a pre-built Docker image with Jupyter and this project pre-configured. 
With [Docker installed](https://www.docker.com/community-edition#download), run the following command from the terminal:

`docker pull opentraffic/hackathon`

Then start the docker image using:

`docker run -p 8888:8888 opentraffic/hackathon`

Once running you'll see the message:

`Copy/paste this URL into your browser when you connect for the first time, to login with a token:
    http://localhost:8888/?token=4ddef1....`
 
 Copy the complete URL into your browser to get started!

### Examples

*Example 1:* Download and process data. This example downloads a single weekly data file for Cebu, and demonstrates techniques for calculating 
average roadway speeds by day of week and hour of day.

*Example 2:* Combine CSV data with Shapefile. This example uses a GeoJSON bounding box to select a subset of street segments in Cebu, 
and calculates the average travel speed using this filtered subset of streets. This demonstates data loading and analysis, 
and geospatial analysis techniques. 



