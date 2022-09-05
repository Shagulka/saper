import json

flag = "🚩"
mine = "💣"
empty = "⬜"
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
        global flag, mine, empty, one, two, three, four, five, six, seven, eight
        flag = assets_data["flag"]
        mine = assets_data["mine"]
        empty = assets_data["empty"]
        one = assets_data["one"]
        two = assets_data["two"]
        three = assets_data["three"]
        four = assets_data["four"]
        five = assets_data["five"]
        six = assets_data["six"]
        seven = assets_data["seven"]
        eight = assets_data["eight"]
        return True



