# Similarity Search using Permutation Based Indexing
### Implementing Similarity Search using PBI and Metric Inverted Files

This repository houses the source code and results of implementing a similarity search algortith utiling permutation based indexing with the help of metric inverted files.
The project is implemented using python and works on a dataset containing over 1 million records.


## Table of Contents

- [Project Overview](#projectoverview)
- [Data Description](#datadescription)
- [Technical Overview](#technicaloverview)
- [Results](#results)

***

<a id='projectoverview'></a>
## Project Overview

This project aims to implement a distributed architecture using python to implement similarity search on a given dataset.

Such an implementation can prove extremely useful in a variety of applications including finding similarities between genome sequences and retrieveing relevant information based on a given query.

This particular implementation works on a dataset containing Accident Information in the UK and can help businesses to search for relevant accident records based on a search criteria.

In general, this implementation is based on a Permuation Based Indexing Algortithm and generates a Metric Inverted File to perform an approximate search.
This technique is a highly efficient method however, with the increase of database sizes, a parallel and distributed computing apprach is required.

<a id='datadescription'></a>
## Data Description

The dataset used is a collection of records for accidents occuring in the United Kingdom and contain a million records.

The dataset also spans wide by gathering information across different parameters of the accident including:
* Road Information
* Intersection
* Day of the Week
* Juction Type
* Lighting Conditions
* Weather Conditions
* Speed Limit
* Road Conditions

To perform search across such a massive dataset requires a robust similarity search algorithm which is implemented using permutation based indexing.

The dataset used can be accessed using the link provided in the file [Accident Information File.txt](https://github.com/ankit-dhall/similarity_search_pbi/blob/main/Accident%20Information%20File.txt)

<a id='technicaloverview'></a>
## Technical Overview

The project has been divided into various steps which include:
* Data Exploration and Pre-Processing
* Randomizing reference Points
* Calculating Distances and Creating MIF Files
* Performing Search using MIF Files

<a id='results'></a>
## Results

The code for MIF file generation can be accessed here [mif_generation.py](https://github.com/ankit-dhall/similarity_search_pbi/blob/main/mif_generation.py)

The resultant MIF file can be accessed using the link provided here [Final Mif File.txt](https://github.com/ankit-dhall/similarity_search_pbi/blob/main/Final%20Mif%20File.txt)

The MIF file is then utilized to run similarity search and the code for searching can be found here [searching.py](https://github.com/ankit-dhall/similarity_search_pbi/blob/main/searching.py)

3 sample queries were run and the results can be viewed here [Results](https://github.com/ankit-dhall/similarity_search_pbi/tree/main/results)