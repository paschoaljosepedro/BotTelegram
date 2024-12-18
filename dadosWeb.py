import requests
from bs4 import BeautifulSoup
import re
from bancoDeDados import Database


class Scraping:
    def __init__(self):
     pass

    def fazerScrapingAsura(self):
        
        response = requests.get("https://asuracomic.net")
        soup = BeautifulSoup(response.content, 'html.parser')

        titles = soup.find_all("span", class_="text-[15px] font-medium hover:text-themecolor hover:cursor-pointer")
        chapters = soup.find_all("div", class_="flex text-sm text-[#999] font-medium hover:text-white")

        for i in range(len(titles)):
            titleText = titles[i].text.strip().lower()
            latestChapter = chapters[i * 3].text.strip()
            # Usa uma expressão regular para pegar apenas o primeiro número encontrado na string
            match = re.search(r'\b\d+\b',latestChapter)
            if match:
                chapterNumber = match.group()
            else:
                chapterNumber = "N/A"
            print(f"{titleText} - {chapterNumber}")
            existingChapter = self.bancoDeDados.verificaSeExiste("asura", titleText)
            if existingChapter is not None:
                if float(existingChapter) < float(chapterNumber):
                    self.bancoDeDados.update("asura",titleText,chapterNumber)

    # def fazerScrapingMangaBuddy(self):
    #     response = requests.get("https://mangabuddy.com/home")
    #     soup = BeautifulSoup(response.content,'html.parser') 
    #     titles = [div for div in soup.find_all("div",class_="title") if div.find("h3")]
    #     chapters = soup.find_all("div", class_="chap-item")

    #     for i in range (len(titles)):
    #         titleText = titles[i].text.strip().lower()
    #         latestChapter = chapters[i * 3].text.strip()
    #         match = re.search(r'\b\d+\b',latestChapter)
    #         if match:
    #             chapterNumber = match.group()
    #         else:
    #             chapterNumber = "N/A"
    #         print(f"{titleText} - {chapterNumber}")

