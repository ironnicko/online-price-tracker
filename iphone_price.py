from bs4 import BeautifulSoup
import requests,smtplib
URL = "https://www.apple.com/shop/product/FT0D2LL/A/Refurbished-iPhone-XR-256GB-White-Unlocked?fnode=14d6ecae3bb40ee5774383e5cba11af0a6a70701f35c1456fafa05985cdce94955461d4ec63175147156252cdea1b132783eeedc1b9afec984e6e807349eb13703d82200c1bc54a4f122c41f96d89cf84c6ac83835d834ab0a7c40679216c56e"
HEADERS = {"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}
LIMIT = int(input('Enter the limit:\t'))

def check():
    global URL, HEADERS, LIMIT
    s = []
    PAGE = requests.get(URL).text
    soup = BeautifulSoup(PAGE,'lxml')
    for i in soup.find_all('span',class_='current_price'):
        price = i.find('span').text.strip()
        print(price)
        price = price.split('$')
        price = float(price[1])*73.25
    if price < LIMIT:
        sendm()
        pass
    print(price)

def sendm():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    email = input('Enter your Email:\n')
    password = input('Enter your password:\n')
    to_email = input('Enter To Email:\n')
    server.login(email,password)

    subject = 'Price of XR fell'
    body = f"Check the link:\n{URL}"
    msg = f'Subject: {subject}\n\n{body}'

    server.sendmail(
        email,
        to_email,
        msg
    )
    print('sent!')
    server.quit()

print()
check()
