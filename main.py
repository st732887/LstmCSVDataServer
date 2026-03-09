from fastapi import FastAPI
import pandas as pd
import io

app = FastAPI()

raw_data = """Price Date	Unnamed: 0	Min Price (Rs./Quintal)	Max Price (Rs./Quintal)	Modal Price (Rs./Quintal)	temperature_C	rainfall_mm
2/2/2026,20.419,Soyabeen,2550,5600,5600,25.8,7.12
3/2/2026,3.518,Soyabeen,3901,5700,5700,26.34,7.11
4/2/2026,16.034,Soyabeen,3500,5692,5692,27.29,7.23
5/2/2026,33.276,Soyabeen,2566,5807,5651,27.25,4.91
6/2/2026,327.135,Soyabeen,4237.1,6000.03,5500,27.5,5.91
7/2/2026,63.331,Soyabeen,3500,5698,5636,27.37,5.31
9/2/2026,73.991,Soyabeen,3302,5666,5471,27.15,9.26
10/2/2026,54.179,Soyabeen,3657,5411,5320,25.98,16.04
11/2/2026,55.523,Soyabeen,3596,5240,5100,24.48,17.81
12/2/2026,38.679,Soyabeen,2200,5336,5280,24.02,20.98
13/02/2026,53.655,Soyabeen,3812,5470,5291,23.94,14.25
16/02/2026,32.478,Soyabeen,3720,5304,5304,23.94,14.25
17/02/2026,26.697,Soyabeen,3501,5256,5256,23.94,14.25
18/02/2026,31.058,Soyabeen,4250,5344,4250,23.94,14.25
19/02/2026,19.145,Soyabeen,4150,5600,4150,23.94,14.25
20/02/2026,41.261,Soyabeen,4125,5220,4277,23.94,14.25
21/02/2026,27.657,Soyabeen,4152,5110,5090,23.94,14.25
"""

@app.get('/data')
def get_data():
    # Load with tab separator
    df = pd.read_csv(io.StringIO(raw_data.strip()), sep='\t')
    
    # Remove the column
    df = df.drop(columns=['Unnamed: 0'], errors='ignore')
    
    # Return last 5 rows as JSON
    return df.tail(15).to_dict(orient="records")

