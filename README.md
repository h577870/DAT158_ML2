# ML 2: Customer Revenue Prediction:
Konkurransen og data settene er henter fra Kaggle-konkurransen: [Google Analytics Customer Revenue Prediction](https://www.kaggle.com/c/ga-customer-revenue-prediction). Datasettene som er brukt er train og test.  
Vi har i denne oppgaven vært igjennom følgende trinn: 
1.	Problemstilling
2.	Hente data
3.	Utforske og visualisere data
4.	Forbedrede data til maskinlæringsalgoritmer 
5.	Velge en modell og trene denne
6.	Fin-tuning
7.	Presentasjon av løsning
8.	Utrulling, overvåkning og vedlikehold av systemet

De 7 første trinnene vil være beskrevet i [notebooken](Customer-revenue-prediction.ipynb) og det er derfor kun utrulling, overvåkning og vedlikehold av systemet (trinn 8) som presenteres i README-filen.
## 8. Utrulling, overvåkning og vedlikehold av systemet
Vi har laget en [flask-applikasjon](pred_rev_web/ver1/) som predikerer antatt inntekt generert ut i fra feølgende features:
- Country
- socialEngagementType
- Browser
- operatingSystem
- isMobile
- Continent

Fordi det er mange så mange features i datasettet, og mange av disse (eksempelvis channelGrouping) som ikke gir mening for brukeren å legge inn manuelt, er disse hardkodet manuelt i applikasjonen. Det er mulig å gjøre modellen mer presis ved å hente ut informasjon om blant annet land, region, nettleser og lignende fra nettleserens header, men dette er ikke gjort i vår flask-applikasjon. 

Vi har laget en video som demonstrerer bruken av applikasjonen [her](https://www.youtube.com)
## Kilder
Kaggle-konkurransen: https://www.kaggle.com/c/ga-customer-revenue-prediction 

Data fra konkurransen: https://www.kaggle.com/c/ga-customer-revenue-prediction/data

For å flate ut JSON: https://www.kaggle.com/julian3833/1-quick-start-read-csv-and-flatten-json-fields 

Normalisering av JSON: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.json_normalize.html?highlight=json_normalize 

Fletting av DF: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html?highlight=merge#pandas.DataFrame.merge 

Dokumentasjon for PyCaret: https://pycaret.org/ 

Dokumentasjon for Flask: https://flask.palletsprojects.com/en/1.1.x/ 
