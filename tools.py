import json

def read_json(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(f"Ошибка чтения файла: {e}")

def write_json(filename, data, mode = "w"):
    try:
        with open(filename, mode, encoding='utf-8') as f:
            json.dump(data,f)
    except Exception as e:
        print(f"Ошибка записи файла: {e}")


data = {"братец кролик": 23433263245,
        "братец лис": 32456786756345}
write_json("data.json", data,'w')