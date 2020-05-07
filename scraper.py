import glob
import json

import requests


def get_URL(url):
    r = requests.get(url).json()

    return r


def get_osu_id():
    # x = str(input("Please enter your Osu! account number "
    #
    #               "this is the number at the #'s "
    #
    #               "https://osu.ppy.sh/users/##### "))

    x = "7575434"
    return x


def create_osu_url(osu_id):
    x = ("https://osu.ppy.sh/users/{}/scores/best?mode=osu&offset=0&limit=51".format(osu_id))

    return x


def parse_json(file_name):
    with open(file_name, "r") as content:
        parsed_json = json.load(content)
        for i in parsed_json:
            print(i['beatmapset']['title'], i['created_at'])    # Keep in mind indentation in .json!


def write_json_to_file(json_name, created_osu_url):
    with open(json_name, "w") as json_output:  # When using 'with' we don't need to close the file! "

        json.dump(get_URL(created_osu_url), json_output)


def main():
    osu_id = get_osu_id()

    created_osu_url = create_osu_url(osu_id)

    print(created_osu_url)

    json_name = osu_id + ".json"

    if json_name in glob.glob("*.json"):

        print("ID already queried, parsing json... ")

        parse_json(json_name)

    elif json_name not in glob.glob("*.json"):

        print("new ID, getting scores...")

        write_json_to_file(json_name, created_osu_url)

    parse_json(json_name)


if __name__ == '__main__':
    main()
