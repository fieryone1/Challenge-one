import requests, bs4 
while True: 
    try: 
        print(bs4.BeautifulSoup(requests.get(f'https://www.ecs.soton.ac.uk/people/{input("Enter an ID: ")}').text, "lxml").head.find('meta', property="og:title")['content'])
    except:
        print("name cannot be found")
