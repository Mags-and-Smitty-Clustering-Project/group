This repository contains python code and functions for project 3, wine data quality, at Codeup, San Antonio, Noether data science cohort, February 2023.

**Authors :** Shawn Smith, Magdalena Rahn

**Project Title :** _________

**Project Description :**    
1. This project aims to create a model that will predict wine quality on a scale of 1 to 10, with 10 being the best, based on physiochemical aspects of exisiting Portuguese wines and their numeric data.  

2. The data was obtained on 01 February 2023 from Data.World via the author's donation to UCI, downloaded as two .cvs files (one for red wines, one for white wines), combined into a single file, then cleaned, explored, visualised and modelled. According to the original authors of the database, who were at the University of Minho in Portugal, the data comes from red and white wines in the Vinho Verde region of Portugal.  

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

_Feature                     Definition_

fixed_acidity             - the acids naturally occuring in grapes (tartaric, malic, citric) or produced by yeast during 
                            fermentation (succinic)  

volatile_acidity          - measure of the wines gaseous (volatile) acids, the primary one being acetic acid, which is 
                            asociated with vinegar ; overall, pronounced volatile acidity is a negative characteristic  
                            
citric_acid               - often added to post-fermentation wine to balance sugar levels and / or to create a sense 
                            of vibrancy 

rs                        - residual sugar : the amount of sugar remaining in the wine after fermentation   

chlorides                 - indication of the presence of sodium chloride (salinity) of a wine  

free_s02                  - sulphur dioxide is an anti-oxidant (preservative) ; free sulphur dioxide is S02 added to the 
                            wine that has not reacted with other chemical compounds in the wine ; too much added S02 
                            will produce a sulphury smell in the wine  
                            
total_s02                 - free and bound S02 ; bound S02 has combined with chemical compounds in the wine  

density                   - a description of the viscosity, related to alcohol, sugar, glycerol and other dissolved 
                            solids in the wine ;  
                          - related to a wine's mouthfeel ;  
                          - specifically, 'the mass per unit volume of wine or must at 20°C. It is expressed in grams 
                            per milliliter, and denoted by the symbol ρ' (OIV) ;  
                          - alternately, a measurement of the sugar content of the grapes before fermentation
                          
pH                        - a measure of the relative alkilinity vs the relative acidity of a wine ; usually between 
                            3 and 4 pH ; typically, a wine with a high level of acidity will have a low pH level  
                            
alcohol                   - percentage alcohol by volume in the finished wine  

quality (TARGET)          - rating / score for each wine, between 0 and 10, with 10 being the best  



**The Process / Project Plan :   
1. Obtain, explore and analyse wine chemical composition and wine quality data from Data.World, created by University of Minha in Portugal, with 'quality' as the target variable. Do this using simple Python coding.  

2. Analyse features in the tidied data based on (1) the relationship between free and total sulphur dioxide, (2) the levels of citric acid and residual sugar in the wine, (3) the density of the wine and (4) total residual sugar in and the density of the wine. These were analysed against the target variable of wine 'quality'.  

3. Model the data using comparative visualisations in Python (Seaborn and MatPlotLib).  

4. Apply statistical modelling in Python to select data to determine mathematical probability as compared with visual indications.  

5. Run the unsupervised machine learning methodology of clustering on select hypotheses.  

5. Run classification and linear regression models on the data based on earlier findings. Analyse these results.  

6. Provide suggestions and indicate next steps that could be performed. 



**For Further Exploration :    


**For Further Modelling :  


**Steps To Reproduce :   
1. Assure the presence of a Python environment on your computer.

2. Import :  
- Python libraries pandas, numpy, matplotlib, seaborn and scipy,   
- The red and white Wine Quality databases from https://data.world/food/wine-quality and save the file locally, and  
- Pre-existing or self-created data 'acquire' and 'prepare' modules.

3. Tidy the data.

4. Explore using graphs, statistical evaluation, clustering and modelling.

5. Evaluate, analyse and form conclusions and recommendations and indicate next steps.
