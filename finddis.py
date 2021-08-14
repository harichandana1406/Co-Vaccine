import pandas as pd
import math
import numpy as np
import haversine as hs
AadhaarNo=input("Enter your Adhaar Number: ")
people =  pd.read_excel("plp.xlsx",dtype = object)
hos = pd.read_excel("PMJAYPRIVATEHOSPITALSCONSOLIDATED.xlsx",dtype = object)
def dist(lat1, long1, lat2, long2):
    loc1=(lat1,long1)
    loc2=(lat2,long2)
    return (hs.haversine(loc1,loc2))
def Nearest(lat,long): 
    distances = hos.apply(
        lambda row: dist(lat, long, row['Latitude*'], row['Longitude*']),axis=1)
    return hos.loc[distances.idxmin(), 'Name of the Vaccination Site*'] 
  
def main(AadhaarNo):
    for i in people.index:
        if (np.where(people.iloc[i,[4]]== AadharNo ,'T', 'F')=='T'):
          lat3=people.iloc[i,[5]]
          long3=people.iloc[i,[6]]
          #state=people.iloc[i,[9]]
          people['Name of the Vaccination Site*'] = Nearest(lat3,long3)
    
          #print("HEY",(people.iloc[i,[0]]).to_string(index=False),"here's your Vaccination Hospital")
          hospital=people.iloc[i,[9]]
          print((people.iloc[i,[9]]).to_string(index=False))
          
          print(people.head())
          Address(hospital)
          print(people.head())
          #people = pd.merge(people,hos[['Name of the Vaccination Site*','Address','District*']],on='Name of the Vaccination Site*', how='left')
          #print((hos.iloc[i,[7]]+" "+hos.iloc[i,[8]]+" "+hos.iloc[i,[10]]))
    #print(people.head())
def Address(hospital):
  for i in hos.index:
     if (np.where(hos.iloc[i,[1]]==hospital,'T', 'F')=='T'):
      return (hos.iloc[i,[6]].to_string(index=False)," ",hos.iloc[i,[7]].to_string(index=False)," ",hos.iloc[i,[9]].to_string(index=False))
        
main(AadharNo)