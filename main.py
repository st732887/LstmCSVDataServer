from fastapi import FastAPI
import pandas as pd
import io

app = FastAPI()

raw_data = """Price Date	Unnamed: 0	Min Price (Rs./Quintal)	Max Price (Rs./Quintal)	Modal Price (Rs./Quintal)	temperature_C	rainfall_mm
8/11/2025	1405	300	1300	800	25.38	13.8
8/12/2025	1406	1100	1450	1450	24.31	1.87
8/13/2025	1406	940	1440	1360	25.8	7.12
8/14/2025	1406	780	1430	1270	26.34	7.11
8/15/2025	1406	620	1420	1180	27.29	7.23
8/16/2025	1406	460	1410	1090	27.25	4.91
8/17/2025	1407	300	1400	1000	27.5	5.91
8/18/2025	1407	329	1429	1000	27.37	5.31
8/19/2025	1407	357	1457	1000	27.15	9.26
8/20/2025	1407	386	1486	1000	25.98	16.04
8/21/2025	1407	414	1514	1000	24.48	17.81
8/22/2025	1407	443	1543	1000	24.02	20.98
8/23/2025	1407	471	1571	1000	23.94	14.25
8/24/2025	1408	500	1600	1000	23.94	14.25
8/25/2025	1408	540	1420	940	23.94	14.25
"""

@app.get('/data')
def get_data():
    # Load with tab separator
    df = pd.read_csv(io.StringIO(raw_data.strip()), sep='\t')
    
    # Remove the column
    df = df.drop(columns=['Unnamed: 0'], errors='ignore')
    
    # Return last 5 rows as JSON
    return df.tail(15).to_dict(orient="records")
