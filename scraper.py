import glob
import json

import requests


def get_URL(url):
    r = requests.get(url).json()

    return r


def get_osu_id():
    x = str(input("Please enter your Osu! account number "

                  "this is the number at the #'s "

                  "https://osu.ppy.sh/users/##### "))

    return x


def create_osu_url(osu_id):
    x = ("https://osu.ppy.sh/users/{}/scores/best?mode=osu&offset=0&limit=51".format(osu_id))

    return x


def parse_json_pp(file_name):
    x = []

    with open(file_name, "r") as content:
        parsed_json = json.load(content)
        for i in parsed_json:
            # print(i['beatmapset']['title'], i['created_at'])    # Prints beatmap name and and date played.
            x.append(i['pp'])

        return x


def parse_json_date(file_name):
    y = []
    with open(file_name, "r") as content:
        parsed_json = json.load(content)
        for i in parsed_json:
            y.append(i['created_at'])

        return y


def parse_user_name(file_name):
    y = []
    with open(file_name, "r") as content:
        parsed_json = json.load(content)
        for i in parsed_json:
            if len(y) > 0:
                return y
            else:
                y.append(i['user']['username'])





def write_json_to_file(json_name, created_osu_url):
    with open(json_name, "w") as json_output:  # When using 'with' we don't need to close the file! "

        json.dump(get_URL(created_osu_url), json_output)


def create_plot(json_name):
    if json_name in glob.glob("*.json"):

        print("ID already queried, parsing json... ")

        pp = parse_json_pp(json_name)
        score_date = parse_json_date(json_name)
        score_date = format_score_date(score_date)
        user_name = parse_user_name(json_name)

        # print(pp)
        # print(score_date)
        # print(user_name)
        if len(pp) != len(score_date):
            print("Error! lists not equal! ")
        else:
            print("Lists seem good! proceeding with graph! ")
        return pp, score_date, user_name


def format_score_date(score_date):
    y = []
    for x in score_date:
        # score_date.index(x)  # Gets list position
        x = x[:10]
        y.append(x)
    return y



def main():
    osu_id = get_osu_id()

    created_osu_url = create_osu_url(osu_id)

    # print(created_osu_url)

    json_name = osu_id + ".json"

    if json_name not in glob.glob("*.json"):
        print("new ID, getting scores...")

        write_json_to_file(json_name, created_osu_url)

    pp, score_date, user_name = create_plot(json_name)

    return pp, score_date, user_name




if __name__ == '__main__':
    main()
