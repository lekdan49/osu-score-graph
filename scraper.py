import requests


def get_URL(url):

    r = requests.get(url)

    return r


def get_osu_id():

    x = str(input("Please enter your Osu! account number "
                  
                  "this is the number at the #'s "
                  
                  "https://osu.ppy.sh/users/##### "))

    return x


def create_osu_url(osu_id):

    x = ("https://osu.ppy.sh/users/{}/scores/best?mode=osu&offset=0&limit=51".format(osu_id))

    return x



def main():

    print(get_URL(create_osu_url(get_osu_id())).text)




if __name__ == '__main__':

    main()
