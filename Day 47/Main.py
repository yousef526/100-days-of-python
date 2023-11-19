import lxml
import requests
from bs4 import BeautifulSoup
import smtplib as smtp

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.31",
    "Accept-Language":"en-US,en;q=0.9",
}

NEEDED_PRICE = 220
URL = "https://www.amazon.com/dp/B0CCJYVRPH/ref=syn_sd_onsite_desktop_0?ie=UTF8&psc=1&pf_rd_p=364912db-e534-48ad-9b87-1666e0a1ca2b&pf_rd_r=AXHAJ3CQP7CK6QKYDPDN&pd_rd_wg=Bf2lk&pd_rd_w=69AR9&pd_rd_r=f6b2485c-f317-41f4-9f60-306444106362"

res = requests.get(url=URL,headers=header)

soup = BeautifulSoup(res.text,"lxml")

#price
price_tag = soup.find(name="span",class_="a-offscreen")
price = float(price_tag.get_text(strip=True).split("$")[1])

#msg content
msg = soup.select(selector="h1 span")[0].get_text(strip=True)


if price <= NEEDED_PRICE:
    email = "20191700920@cis.asu.edu.eg"
    password = 'Wtdbe6A92pU7Rm9'
    with smtp.SMTP("outlook.office365.com",port=587) as connection:
        connection.starttls()
        connection.login(user=email,password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs="yousefalaa8190@gmail.com",
            msg=f"subject:Amazon price Alert\n\n {msg} is now ${price} \n {URL}"
        )