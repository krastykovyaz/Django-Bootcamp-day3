import requests
import sys
from bs4 import BeautifulSoup



def looking_for_philosophistic(intent, step_link, step):
    if len(sys.argv) == 2:
        query = [sys.argv[1].replace(" ", "_")]
        if step == 0:
            step_link[step] = query[-1].capitalize()
        while True:
            if intent != None:
                url = "https://en.wikipedia.org/wiki/" + intent
            else:
                url = "https://en.wikipedia.org/wiki/" + query[-1]
            response = requests.get(url)
            if response.status_code != 200: 
                print("It's a dead end !")
                exit(1)
            else:
                response = response.text
            soup = BeautifulSoup(response, "html.parser")
            soup.prettify()
            
            titre_page = soup.title.string[:-12] 
            if titre_page == "Philosophy":
                return step_link

            paragraphes = soup.find_all('p')
            for p in paragraphes:
                if "may refer to" in str(p):
                    print("This article doesn't have the paragraphes!")
                    exit(1)
                refs = p.find_all('a')
                for a in refs:
                    if a.has_attr('href'):
                        if "/wiki/Help" not in a['href'] and "/wiki/" in a['href'][0:6] and a['href'].startswith("/wiki/File:") == False:
                            if a.get('href')[6:] in list(step_link.values()):
                                print('It leads to an infinite loop !')
                                exit(1)
                            step += 1
                            step_link[step] = a.get('href')[6:]
                            # print(step_link.items())
                            return looking_for_philosophistic(a.get('href')[6:], step_link, step)
                    else:
                        print("There isn't references in the paragraph!")
                        exit(1)



def launch_octopus():
    step_link = {}
    step_link = looking_for_philosophistic(None, step_link, 0)
    try:
        for k, v in step_link.items():
            print(v)
        print(len(step_link), "roads from " + sys.argv[1] + " to philosophy !")
    except:
        print("Something went wrong!")

if __name__ == "__main__":
    launch_octopus()
    