import requests, bs4 
while True: print(bs4.BeautifulSoup(requests.get(f'https://www.ecs.soton.ac.uk/people/{input("Enter an ID: ")}').text, "lxml").head.find('meta', property="og:title")['content'])
