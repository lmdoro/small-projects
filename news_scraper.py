from bs4 import BeautifulSoup
import requests
import csv

# Scrape the Hotnews front page for news
# Save the title of the news and the time they were posted and the author
# Store the data in csv format

source = requests.get("https://hotnews.ro").text
soup = BeautifulSoup(source, "lxml")
csv_file = open("news_scraper.csv", "w") # Create and open a csv file for writing
write_to_csv = csv.writer(csv_file) # Use the "csv.writer" method to write the scraped bits to the file
write_to_csv.writerow(["Title", "Author", "Date", "Link"]) # Creating the columns for the CSV file

for data in soup.find_all("div", class_="articol_lead_full"):
    title = data.find("h2", class_="article_title").text
    author = data.find("div", class_= "autor").text
    date = data.find("span", class_="data").text
    link = data.find("a")["href"]

    write_to_csv.writerow([title, author, date, link])

csv_file.close()
