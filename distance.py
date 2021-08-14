import pandas as pd
import numpy as np
import haversine as hs
import openpyxl
#AadharNo=input("Enter your Adhaar Number: ")
people =  pd.read_excel("plp.xlsx")
hos = pd.read_excel("VaccinationCenters.xlsx")
AadhaarNo=str('AadhaarNo')

def dist(lat1, long1, lat2, long2):
    loc1=(lat1,long1)
    loc2=(lat2,long2) 
    return (hs.haversine(loc1,loc2))
def Nearest(lat, long):
    distances = hos.apply(
        lambda row: dist(lat, long, row['Latitude*'], row['Longitude*']),axis=1)
    return hos.loc[distances.idxmin(), 'Name of the Vaccination Site*'] 
def main(AadhaarNo):
    try:
        for i in people.index:
          if (np.where(people.iloc[i,[4]]== AadhaarNo ,'T', 'F')=='T'):
            lat3=people.iloc[i,[5]]
            long3=people.iloc[i,[6]]
            people['Name of the Vaccination Site*'] = Nearest(lat3,long3)
            hs=people.iloc[i,[9]]
            return(people.iloc[i,[9]].to_string(index=False))
            Address(hs)
            
        else:
           return "Please provide correct Aadhaar Number"
          
    except ValueError:
        return "invalid input"

def Address(hospital):
        for i in hos.index:
            if (np.where(hos.iloc[i,[1]]==hospital,'T', 'F')=='T'):
                return(hos.iloc[i,[6]].to_string(index=False))
                #return(hos.iloc[i,[6]].to_string(index=False)," ",hos.iloc[i,[7]].to_string(index=False)," ",hos.iloc[i,[9]].to_string(index=False))
  




