import http.client
import json


class quote_random():

    def __init__(self):
        pass

    def quote_random(self):

        conn = http.client.HTTPSConnection("quotes15.p.rapidapi.com")

        headers = {
            'x-rapidapi-key': "a7a175b6bamsh8339c629c780adcp13e39ejsn81854824e677",
            'x-rapidapi-host': "quotes15.p.rapidapi.com"
        }

        conn.request("GET", "/quotes/random/?language_code=it", headers=headers)
        # conn.request("GET", "/quote/image")

        res = conn.getresponse()
        data = res.read()

        # print(data.decode("utf-8"))
        return data.decode("utf-8")

    def quote_and_author(self):
        testo_json = self.quote_random()
        python_obj = json.loads(testo_json)
        print(python_obj)
        return (python_obj['originator']['name'], python_obj['content'])
    

def main():
    res = quote_random()
    resx = res.quote_and_author()
    print(resx[0])
    print(resx[1])

# main()