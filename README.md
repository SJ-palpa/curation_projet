--------------------
INFORMATION GÉNÉRALE
--------------------

Titre du jeu de données: Information sur des articles scientifiques concernant les théories du complot de 2019 à 2021

Renseignements concernant l'auteur (Jermini Stéphane, HEG Genève, Rue de la Tambourine 17 1227 Carouge, stephane-alain.jermini@hesge.ch)

    Chercheur principal: Arnaud Gaudinat
    Co-chercheur ou chercheur associé: Vanessa Besson, Eléonore Crausaz, Stéphane Jermini 

Description sommaire : Résultat google scholar théories du complot 2019 à 2021 

Date de la collecte de données:  2021-04-01

Date de production des données: 2021-04-01

Date de publication des données: 2021-05-29

Localisation géographique de la collecte de données: Monde entier 

Renseignements concernant les organismes subventionnaires ou commanditaires de cette collecte de données: Google Scholar


--------------------------------------------------
INFORMATION D'ACCÈS/PARTAGE DES DONNÉES
-------------------------------------------------- 

Licences/restrictions en lien avec les données, ou limitations d'utilisation: Creative Commons licence

Référence bibliographique de ce jeu de données: -

Références bibliographiques et hyperliens des publications liées à ce jeu de données: -

Autres liens permettant le libre accès à ce jeu de données:

    https://github.com/SJ-palpa/curation_projet

    https://zenodo.org/record/4843312#.YLUeLqgzaUk

    http://5.196.70.206/data/Besson_Jermini_Crausaz/page_web.html                                

-----------------------------
APERÇU DES DONNÉES & FICHIERS
-----------------------------

Liste des fichiers:

Données brutes complètes:
    scrap_all.csv
    
    Données brut par années:
        scrap_2019.csv
        scrap_2020.csv
        scrap_2021.csv

    Données enrichie et transformé :
        conspiracy_theories_data.csv
        
  
--------------------------
INFORMATION METHODOLOGIQUE
--------------------------

Description de la méthodologie de collecte/production des données: 

Ce jeu de données correspond au scraping de 3 années depuis la plateforme web Google Scholar (https://scholar.google.com/). Voici les paramètres que nous avons utilisé pour Google Scholar:

-exclure brevet

-exclure citations

Notre recherche a été faite avec les termes suivants : "social media" AND "conspiracy theories"

Ce jeu de données se concentre sur les années 2019, 2020 et 2021. Pour chaque années 700 résultats de Google Scholar on été scrapé.

Pour chacun de ces résultats nous avons récupéré 7 champs que nous avons mis dans les 7 colonnes de notre fichier dataset:

-Titre

-Lien

-Citation

-Lien pdf du document

-Auteur, éditeur, année, site internet

-Nombre de citations

-Nombre de versions


Description des opérations de traitement des données: Pour l'extraction de meta données nous avons utilisé TIKA, pour l'extraction des PDF nous avons utilisé un script python.

Identifier les personnes impliquées dans la collecte, le traitement, l'analyse et/ou la diffusion des données: Vanessa Besson, Eléonore Crausaz, Stéphane Jermini


------------------------------------------------------------
RENSEIGNEMENTS CONCERNANT LE CONTENU DES FICHIERS DE DONNÉES 

------------------------------------------------------------
scrap_all.csv (identique pour les autres fichiers de données brut)

    Nombre de variables: 7

    Nombre d'enregistrements/lignes: 2160

    Liste des variables, définitions et abréviations: 
        titre : Titre de l'article
        lien : Lien vers sa page web
        citation : Court extrait
        pdflink : Lien pdf
        auteurEditeur : Information sur l'auteur, l'éditeur et l'année (Information incomplète)
        cite : Nombre de citations
        version : Nombre de version

    Format des données:
        titre : Texte
        lien : Texte
        citation : Texte
        pdflink : Texte
        auteurEditeur : Texte
        cite : Texte
        version : Texte    

conspiracy_theories_data.csv

    Nombre de variables: 20

    Nombre d'enregistrements/lignes: 2160

    Liste des variables, définitions et abréviations:
    titre : Titre de l'article
    lien : Lien vers sa page web
    citation : Court extrait
    pdflink : Lien pdf
    contenu_pdf : Contenu de l'article
    illuminati : Présence du terme "illuminati" ou qui s'en rapproche dans l'article
    crop circle : Présence du terme "crop circle" ou qui s'en rapproche dans l'article
    reptilian : Présence du terme "reptilian" ou qui s'en rapproche dans l'article
    moon landing : Présence du terme "moon landing" ou qui s'en rapproche dans l'article
    chemtrails : Présence du terme "chemtrails" ou qui s'en rapproche dans l'article
    Alska mind-control : Présence du terme "alska mind-control" ou qui s'en rapproche dans l'article
    Area 51 aliens : Présence du terme "Area 51" ou qui s'en rapproche dans l'article
    kennedy assassination : Présence du terme "Kennedy assassination" ou qui s'en rapproche dans l'article
    CoronaTrueFalse : Présence du terme "corona" ou qui s'en rapproche dans l'article
    meta : meta données du pdf de l'article
    Author : Auteur de l'article réconcilié à partir de TIKA
    auteurEditeur : Information sur l'auteur, l'éditeur et l'année (Information incomplète)
    cite : Nombre de citations
    version : Nombre de version
    year : Année de publication de l'article
   
    Format des données:

    titre : Texte
    lien : Texte
    citation : Texte
    pdflink : Texte
    contenu_pdf : Texte
    illuminati : Texte
    crop circle : Boolean
    reptilian : Boolean
    Moon landing : Boolean
    chemtrails : Boolean
    Alska mind-control : Boolean
    Area 51 aliens : Boolean
    Kennedy assassination : Boolean
    CoronaTrueFalse : Boolean
    meta : Json
    Author : Texte
    auteurEditeur :Texte
    cite : Texte
    version : Texte
    year: Number
