This repository contains python code and functions for project 3, wine data quality, at Codeup, San Antonio, Noether data science cohort, February 2023.

**Authors :** Shawn Smith, Magdalena Rahn

**Project Title :** _________

**Project Description :**    
1. This project aims to create a model that will predict wine quality on a scale of 1 to 10, with 10 being the best, based on physiochemical aspects of exisiting Portuguese wines and their numeric data.  

2. The data was obtained from Data.World via UCI on 01 February 2023, downloaded as two .cvs files (one for red wines, one for white wines), combined into a single file, then cleaned, explored, visualised and modelled. According to the original authors of the database, who were at the University of Minho in Portugal, the data comes from red and white wines in the Vinho Verde region of Portugal.  

3. Credit for the data goes to :  
"P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis.  
"Modeling wine preferences by data mining from physicochemical properties.  
"In Decision Support Systems, Elsevier, 47(4):547-553. ISSN: 0167-9236.  

"Available at: [@Elsevier] http://dx.doi.org/10.1016/j.dss.2009.05.016  
"[Pre-press (pdf)] http://www3.dsi.uminho.pt/pcortez/winequality09.pdf  
"[bib] http://www3.dsi.uminho.pt/pcortez/dss09.bib "  


**Hypotheses :**
1.  
- H_0 : The overall quality of the wine has no relationship to its free sulphur dioxide and total sulphur dioxide levels.  
- H_a : The overall quality of the wine has a relationship to its free sulphur dioxide and total sulphur dioxide levels.  

2.  
- H_0 : The levels of citric acid and residual sugar in the wine have no relationship to its quality.  
- H_a : The levels of citric acid and residual sugar in the wine have no relationship to its quality.  

3.  
- H_0 : The density of the wine has no relationship to its quality.  
- H_a : The density of the wine has a relationship to its quality.  

4.  
- H_0 : The total residual sugar in and the density of the wine have no relationship to its quality.  
- H_a : The total residual sugar in and the density of the wine have a relationship to its quality.  


**Data Dictionary :**
fixed_acidity  
volatile_acidity  
citric_acid  
rs  
chlorides  
free_s02  
total_s02  
density  
pH  
sulphates  
alcohol  
quality (score between 0 and 10)  

|Feature|              Definition|
| :------|:------|
|bath|                      - tells how many half and full bathrooms in the house|
|bed|                       - tells how many bedrooms in the house|
|sqft|                      - tells the total square footage of the house itself|
|fin_sqft|                  - tells finished square footage of the house itself|
|fips|                      - tells the county code of the property| 
|full_bath|                 - tells the amount of full bathrooms only|
|lotsize|                   - tells the size of the entire property lot in square feet|
|zipcode|                       - tells what zip code the house is located |
|rooms|                     - tells how many total rooms there are in the house|
|yearbuilt|                 - tells you the year the house was built|
|taxvaluedollarcnt (TARGET)|         - tells you the value of the home|

