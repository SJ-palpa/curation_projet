from selenium import webdriver
from bs4 import BeautifulSoup
#from fake_useragent import UserAgent
import time
import csv


#urlAPI = 'http://api.proxiesapi.com/?auth_key=a5f51fa40009224a1103428100135904_sr98766_ooPq87&url=https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=conspiracy+on+social+media&btnG='
urlpartie1 = 'https://scholar.google.com/scholar?start='
urlpartie2 = '&q=%22social+media%22+AND+%22conspiracy+theories%22&hl=en&as_sdt=0,5&as_ylo=2019&as_yhi=2019&as_vis=1'

#url_settings = 'https://scholar.google.com/scholar_settings?q=conspiracy+on+social+media&hl=en&as_sdt=0,5'
chrome_options = webdriver.ChromeOptions()


#Fake user agent pour essayer d eviter les captcha
#ua = UserAgent()
#userAgent = ua.random
#chrome_options.add_argument(f'user-agent={userAgent}')
driver = webdriver.Chrome(executable_path=r"***path***"
                          ,options=chrome_options)

# Modifier viewport
driver.execute_script("return [window.innerWidth, window.innerHeight];")
articleIndex =0

# pour ecrire dans le fichier csv
row_list = []


driver.get(urlpartie1+str(articleIndex)+urlpartie2)
time.sleep(20)


while articleIndex < 10:

    driver.get(urlpartie1+str(articleIndex)+urlpartie2)
    articleIndex += 20
    #Pour afficher avoir 20 result par pages || Ne fonctionne pas
    #el = driver.find_element_by_id('gs_num-d')
    #for option in el.find_elements_by_tag_name('option'):
    #    if option.text == '"20"':
    #        option.click() # select() in earlier versions of webdriver
    #        break
    #driver.find_element_by_name('save').click()

    source = driver.page_source

    soup = BeautifulSoup(source,'lxml')

    # #Avec boucle
    for item in soup.select('[data-lid]'):

        # #Sans boucle
        #item = soup.select('[data-lid]')[0]
        time.sleep(1)  # sleep for 1 sec


        #print('----------------------------------------')
        # #item entier
        #print(item)

        # #titre
        titre = ""
        if item.find('h3'):
            titre = item.select('h3')[0].get_text()
        #print(titre)

        # #lien
        lien = ""
        if item.find('a'):
            lien = item.select('a')[0]['href']
        #print(lien)

        # #citation
        citation = ""
        if item.find('.gs_rs'):
            citation = item.select('.gs_rs')[0].get_text()
        #print(citation)


        # # link pdf
        pdflink = ""
        if item.select(".gs_or_ggsm"):
            if "[PDF]" in item.select('.gs_or_ggsm')[0].get_text():
                pdflink = item.select('.gs_or_ggsm')[0].findNext('a')['href']
            #print(pdflink)

        # #nombre de versions

        # # auteur / editeur
        auteurEditeur = ""
        if item.find('.gs_a'):
            auteurEditeur = item.select('.gs_a')[0].get_text()
        #print(auteurEditeur)

        # #cite
        cite = ""
        if item.find("a[href*='/scholar?cites']"):
            cite = item.select("a[href*='/scholar?cites']")[0].get_text()
        #print(version)

        # #version
        version = ""
        if item.find("a[href*='/scholar?cluster=']"):
            version = item.select("a[href*='/scholar?cluster=']")[0].get_text()
        #print(citation)

        # #BybText Link
        #print(item.select("a[href*='https://scholar.googleusercontent.com/scholar.bib?q']"))

        #print('----------------------------------------')

        # #Ouvre et ferme nouvel onglet
        # #obtenir le code pour ouvrir la page avec le lien bibTex
        #code = item.select('[data-clk-atid]')[0]['data-clk-atid']
        #url2 = 'https://scholar.google.com/scholar?q=info:'+code+':scholar.google.com/&output=cite&scirp=0&hl=en'
        #driver.execute_script("window.open('');")
        #driver.switch_to.window(driver.window_handles[1])
        #driver.get(url2)
        #time.sleep(1)  # sleep for 1 sec
        #source2 = driver.page_source
        #soup2 = BeautifulSoup(source2, 'lxml')
        #print(soup2.select('.gs_citi')[1])
        #driver.close()
        #driver.switch_to.window(driver.window_handles[0])
        row_list.append([titre,lien,citation,pdflink,auteurEditeur,cite,version])



    print(articleIndex)
with open('curationDonnees2020_2020_1.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(row_list)

