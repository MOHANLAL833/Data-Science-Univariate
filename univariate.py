class univariate():
     #Function to seperate the data into quan and qual
    def quanqual(data):
        qual=[]
        quan=[]
        for columnname in data.columns:
            #print(columnname)
            if (data[columnname].dtype=='O'):
                #print("Qual")
                qual.append(columnname)
            else:
                #print("Quant")
                quan.append(columnname)
        return qual,quan
    #Function to find Mean,mdeian,mode,IQR,Percentile,Range
    def univariate_table(data,quan):
        import pandas as pd
        import numpy as np
        descriptive=pd.DataFrame(index=["Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%","99%","Q4:100%","IQR","1.5Rule",
                                    "Lesser","Greater","Min","Max"],columns=quan)
        for columnname in quan:
            descriptive[columnname]["Mean"]=data[columnname].mean()
            descriptive[columnname]["Median"]=data[columnname].median()
            descriptive[columnname]["Mode"]=data[columnname].mode()[0]
            descriptive[columnname]["Q1:25%"]=data.describe()[columnname]["25%"]
            descriptive[columnname]["Q2:50%"]=data.describe()[columnname]["50%"]
            descriptive[columnname]["Q3:75%"]=data.describe()[columnname]["75%"]
            descriptive[columnname]["99%"]=np.percentile(data[columnname],99)
            descriptive[columnname]["Q4:100%"]=data.describe()[columnname]["max"]
            descriptive[columnname]["IQR"]=descriptive[columnname]["Q3:75%"]-descriptive[columnname]["Q1:25%"]
            descriptive[columnname]["1.5Rule"]=1.5*descriptive[columnname]["IQR"]
            descriptive[columnname]["Lesser"]=descriptive[columnname]["Q1:25%"]-descriptive[columnname]["1.5Rule"]
            descriptive[columnname]["Greater"]=descriptive[columnname]["Q3:75%"]+descriptive[columnname]["1.5Rule"]
            descriptive[columnname]["Min"]=data[columnname].min()
            descriptive[columnname]["Max"]=data[columnname].max()
        return descriptive
        #Function to find outliers
    def findoutlier(descriptive,quan):
        lesser=[]
        greater=[]
        for colname in quan:
            if(descriptive[colname]["Min"]<descriptive[colname]["Lesser"]):
                lesser.append(colname)
            if(descriptive[colname]["Max"]>descriptive[colname]["Greater"]):
                greater.append(colname)
        return lesser,greater
    #Function to replace outlier
    def insertoutlier(data,lesser,greater,descriptive):
        for columnName in lesser:
            data[columnName][data[columnName]<descriptive[columnName]["Lesser"]]=descriptive[columnName]["Lesser"]
        for columnName in greater:
            data[columnName][data[columnName]>descriptive[columnName]["Greater"]]=descriptive[columnName]["Greater"]
        return data
    #Function to find frequency of the data
    def FreqTable(columnName,data):
        import pandas as pd
        import numpy as np
        frequencytable=pd.DataFrame(columns=["Unique_values","Frequency","Relative Frequency","cusum"])
        frequencytable["Unique_values"]=data[columnName].value_counts().index
        frequencytable["Frequency"]=data[columnName].value_counts().values
        frequencytable["Relative Frequency"]=(frequencytable["Frequency"]/103)
        frequencytable["cusum"]=frequencytable["Relative Frequency"].cumsum()
        return frequencytable