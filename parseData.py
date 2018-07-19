import pandas as pd

def parseLogs():

    df = pd.read_csv('/Users/astitvnagpal/Desktop/activity.log')
    df.rename(columns={'# Elapsed time   CPU (%)     Real (MB)   Virtual (MB)': 'Data'}, inplace=True)
    
    time = []
    cpu = []
    real = []
    vir = []
    
    for i in range(0, len(df['Data'])):
        row = df['Data'][i].split(" ")
        filterObject = filter(None, row)
        myList = list(filterObject)
        time.append(float(myList[0]))
        cpu.append(float(myList[1]))
        real.append(float(myList[2]))
        vir.append(float(myList[3]))

    newDf = pd.DataFrame()
    newDf['Time'] = time
    newDf['CPU'] = cpu
    newDf['Real'] = real
    newDf['Vir'] = vir

    print("\n_________My DataFrame__________\n\n{}\n\n".format(newDf))
    print("Maximum CPU Spike: {}".format(newDf['CPU'].max()))


if __name__ == '__main__':
	parseLogs()