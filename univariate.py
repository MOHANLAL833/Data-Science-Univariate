class univariate():

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