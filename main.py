from bs4 import BeautifulSoup as bs
import requests
import lxml
import re
import database
import telegram_bot

headers = {'user_agent': 'Mozilla/5.0'}
url = "https://app.estateguru.co/investment/show/"
page = requests.get(url)
page.raise_for_status() #if error it will stop the program

soup = bs(page.text, 'lxml')

investments = soup.find_all('div', class_="project-item-body")
# est_investments = investments.split()

#print(investments)

est_id = []
for investment in investments:
    #print(investment)
    est = investment.find('h6', class_="project-item-title").text.split()[-1].replace('(','').replace(')','')
    if est == "Estonia":
        # Here should have an if statement, that would need to check if loan is active or not, somehow it works right now...
        #It might be because inactive listings have a different html class
        # if investment.find('a', class_="btn btn-regular w-100").text == 'Investeeri':
        investment_id = investment.find('a', class_="btn btn-regular w-100")
        if investment_id != None:
            investment_id = str(investment_id)
            #print(investment_id)
            id_regex = re.split("\s", investment_id)[-3].split('/')[-1].replace('"','')
            if id_regex not in database.show_all():
                next_url = f"https://app.estateguru.co/investment/single/{id_regex}?uniqueId=&lang=ee"
                next_page = requests.get(next_url)
                next_soup = bs(next_page.text, 'lxml')
                # est_id.append(id_regex)
                #This below is only useful for finding Government backed investments
                # description = next_soup.find('ul', class_="main-list").text
                #preview = next_soup.find('div', class_="pr-box-content pb-4")
                database.add_one(id_regex, next_url)
                telegram_bot.telegram_bot_sendtext(next_url)



# if len(est_id) != 0:
#     for ID in est_id:
#         print(ID)
#         next_url = f"https://app.estateguru.co/investment/single/{ID}?uniqueId=&lang=ee"
#         next_page = requests.get(next_url)
#         next_soup = bs(next_page.text, 'lxml')

#         description = next_soup.find('ul', class_="main-list").text
#         print(description)



"""This is a feature to find Government backed investments"""

# keywords = ['Riik', 'Kohalik omavalitsus']

# desc = 'Laenu kasutatakse olemasoleva kohalik omavalitsus Estateguru laenu refinantseerimiseks ja ettevõtte käibekapitali suurendamiseks.Laen tagastatakse tagatisvara müügist laekuvate tulude arvelt või refinantseerimisel pikaajalise pangalaenuga.Laen on tagatud esimese järgu hüpoteegiga. Laenuvõtja juhatuse liige annab kogu hüpoteegisumma ulatuses isikliku käenduse.Laenuvõtja jätab omale võimaluse kaasata vajadusel täiendavat finantseeringut tagatisvara väärtuse kasvamisel.Hüpoteek seati varasema rahastusetapi käigus ja tagab ka kõiki järgnevaid rahastusetappe.Järgnevate rahastusetappide eelduseks on ehitusjärelevalve kinnitus ehitustööde teostamise kohta (juhul kui ehitustöödega on alustatud ja töid on teostatud arvestatavas mahus) ning kolmanda osapoole hinnang tagatisvara turuväärtuse kohta.LTV  30 etapis on 55.3% ja võib kasvada maksimaalselt kuni 65.0%-ni järgnevate rahastusetappide käigus.Laen refinantseeritakse oodatust pikema müügiperioodi tõttu. Laenusaaja maksab eelmise laenuperioodi eest kogunenud intressid (sealhulgas hüvitised ja viivistasud, kui neid on riik).'
# desc_ = desc.split()
# print(desc_)

# keyword_finder = re.compile('|'.join(keywords),re.IGNORECASE).search(desc) #re.IGNORECASE makes the search case-insensitive
# if keyword_finder:
#     print(f"Words found: {keywords}")

# [
#     {
#     'Loan name': 'Arenduslaen - 19.Etapp',
#     'url': 'https://app.estateguru.co/investment/show/EE3772-19',
#     'keyword': 'riik',
#     'Interest': '10.0%',
#     'Target': '€63,000',
#     'Collateral value': '€3,000,905',
#     'Loan Period': '12 months'
#     },
#     {
#     'Loan name': 'Sildlaen - 30.Etapp',
#     'url': 'https://app.estateguru.co/investment/single/EE-5312?uniqueId=&lang=ee',
#     'keyword': 'riik',
#     'Eesmärk': '€63,000'
#     },
#     {
#     'Loan name': 'Sildlaen - 30.Etapp',
#     'url': 'https://app.estateguru.co/investment/single/EE-5312?uniqueId=&lang=ee',
#     'keyword': 'riik',
#     'Eesmärk': '€63,000'
#     }
# ]

