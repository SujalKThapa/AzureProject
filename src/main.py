import pandas as pd
from pyscript import document
from pyodide.http import open_url
def sayHello():
    urlCSV = open_url("https://raw.githubusercontent.com/Articuano/ProfanityCsv/main/profanity_en.csv")
    df = pd.read_csv(urlCSV)
    dfset = df["text"]
    resultList = Element('mainContent').value
    resultList = resultList.lower()
    mystr = ""
    ans =[]
    ParaList = resultList.split("\n")
    print("The profane themes present in the above text are:")
    for i in ParaList:
        explicitWords = []
        for j in range(0,len(dfset)):
            if dfset[j] in i:
                print(df.loc[j]["category_1"])
                print("due to the presence of the word " + dfset[j])