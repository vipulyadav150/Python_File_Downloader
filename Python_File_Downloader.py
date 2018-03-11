from urllib import request





def file_down(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    destination_url = r'data.csv'
    fw = open(destination_url, "w")
    for line in lines:
        fw.write(line + "\n")
    fw.close()


get_url = input("Paste the url : \n")
file_down(get_url)
