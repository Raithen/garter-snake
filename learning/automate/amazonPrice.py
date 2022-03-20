import bs4, requests

def getAmazonPrice(productUrl):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    res = requests.get(productUrl, headers=headers)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#current_conditions-summary > p.myforecast-current-lrg')
    return elems

    


price = getAmazonPrice('https://forecast.weather.gov/MapClick.php?lat=42.27086000000003&lon=-83.73449999999997#.YjP7Pn_MIUE')
print(f'The Temperature is {price}')