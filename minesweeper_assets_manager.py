import json

flag = "🚩"
mine = "💣"
empty = "⬜"
hidden = "⬛"
selected = "🔳"
one = "1️⃣"
two = "2️⃣"
three = "3️⃣"
four = "4️⃣"
five = "5️⃣"
six = "6️⃣"
seven = "7️⃣"
eight = "8️⃣"


def load_assets(string):
    with open(string) as json_assets:
        assets_data = json.load(json_assets)
        global flag, mine, empty, one, two, three, four, five, six, seven, eight, hidden, selected
        flag = assets_data["flag"]
        mine = assets_data["mine"]
        empty = assets_data["empty"]
        hidden = assets_data["hidden"]
        selected = assets_data["selected"]

        one = assets_data["one"]
        two = assets_data["two"]
        three = assets_data["three"]
        four = assets_data["four"]
        five = assets_data["five"]
        six = assets_data["six"]
        seven = assets_data["seven"]
        eight = assets_data["eight"]
        return True

def get_asset(string):
    if string == "flag":
        return flag
    elif string == "mine":
        return mine
    elif string == "empty":
        return empty
    elif string == "hidden":
        return hidden
    elif string == "selected":
        return selected
    elif string == "1":
        return one
    elif string == "2":
        return two
    elif string == "3":
        return three
    elif string == "4":
        return four
    elif string == "5":
        return five
    elif string == "6":
        return six
    elif string == "7":
        return seven
    elif string == "8":
        return eight
    else:
        return None



