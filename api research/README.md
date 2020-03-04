# UNEP Environmental Data Explorer API

## Installation

Since UNEP Environmental Data Explorer API is hosted on the UNEP website, there is no need to download any content to make API calls. Data can be downloaded, however, in order to continuously update a site using the API, calls to the server will be needed instead. This document will serve as a guide as to how to make calls to the server.

## API Calls

This is the base for API calls:
```url
http://geodata.grid.unep.ch/api/
```

Every call starts from here!

### List all countries
```url
http://geodata.grid.unep.ch/api/countries
```
This returns a list of every country in the UNEP database with information on the country.

### List all regions
```url
http://geodata.grid.unep.ch/api/regions
```
This returns a list of every region in the UNEP database with information on the region.

### List all subregions
```url
http://geodata.grid.unep.ch/api/subregions
```
This returns a list of every country in the UNEP database with information on the region.

### Sample API Call
```url
http://geodata.grid.unep.ch/api/countries/DE;FR;CH/variables/1;480/years/2000:2003
```
This returns data from the countries (/countries/) Germany, France, and Switzerland (DE;FR;CH) for Agricultural Area and Water Use - Industrial W… Total Water Withdrawal (1;480) for the years 2000-2003 (2000:2003).

To form an API call, first put the type of area being called from (country, global, etc.), then the actual identifiers of those places, then the variables being viewed, then the period of time needed.

### List all Variables
```url
http://geodata.grid.unep.ch/api/variables
```
This returns a list of every variable in the UNEP database with information on the variable.
