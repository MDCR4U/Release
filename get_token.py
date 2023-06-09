import csv
import requests
import os

def get_run_command(url ,wstoken):
    wurl = url + "token.csv"
    print("get_token " + wurl + "-" + wstoken)
    response = requests.get(wurl)
    if response.status_code != 200:
        return "Error: Cannot fetch data from the server."

    content = response.content.decode('utf-8')
    csv_reader = csv.reader(content.splitlines(), delimiter=',')

    header = next(csv_reader)
    if header != ["code", "description"]:
        return "Error: Invalid CSV header."

    for row in csv_reader:
        code, description = row
        if code == wstoken:
            print("get token return " + description)
            return description

    return "NF"
def get_continue(line_id):

    wfn = 'continue/' + line_id + '.txt'

    print("get_continue  " + wfn)

    try:
        with open(wfn, "r", encoding="utf-8") as f:
            wslast= f.readline()
            print("get continue last token = " + wslast)
            return f.readline()
    except FileNotFoundError:
            print("not found last ")
            write_continue(line_id,'@cbd')
            return('@cbd')

def write_continue(line_id,wstoken):
    subdir_name = "continue"

# 檢查子目錄是否已存在，如果不存在，則建立子目錄
    if not os.path.exists(subdir_name):
        os.makedirs(subdir_name)
       
    
    wfn = 'continue/' + line_id + '.txt'

    with open( wfn, "w", encoding="utf-8") as f:
        f.write(wstoken[2:])     
# 使用範例
#wstoken = "a001_1"
#print(get_token(wstoken)