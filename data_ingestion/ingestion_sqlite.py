import pandas as pd
import sqlite3

# Establish connection to SQLite database
con = sqlite3.connect('../data/database.db')

cursor = con.cursor()

def calculate_efforts_score(data):
    weights = {
        'Recycling Rate (%)': 0.4,
        'Remanufacturing Potential (%)': 0.3,
        'Life Cycle Assessment Score': 0.3
    }
    
    # Calculate the efforts score for each part
    data['Efforts Score'] = sum([data[attribute] * weight for attribute, weight in weights.items()])
    lst = [data[attribute] * weight for attribute, weight in weights.items()]
    print(lst)
    return data



def getSustainibilityScore(row):
    data = {
        'New Parts Carbon Footprint (kg CO2e)': 0.2,
        'Recycled Parts Carbon Footprint (kg CO2e)': 0.2,
        'Water Usage - New Parts (liters)': 0.1,
        'Water Usage - Recycled Parts (liters)': 0.1,
        'Landfill Waste - New Parts (kg)': 0.1,
        'Landfill Waste - Recycled Parts (kg)': 0.1,
        'Energy Consumption - New Parts (kWh)': 0.1,
        'Energy Consumption - Recycled Parts (kWh)': 0.1,
        'Recycling Rate (%)': 0.05,
        'Toxicity Score - New Parts': 0.025,
        'Toxicity Score - Recycled Parts': 0.025,
        'Remanufacturing Potential': 0.025,
        'Life Cycle Assessment Score': 0.025
    }
    sustainScore = sum(row[value] * weight for value, weight in data.items())
    return sustainScore

def getRecycleEffort(row):
    data = {
        'Recycling Rate (%)' : 0.4,
        'Remanufacturing Potential (%)': 0.3,
        'Life Cycle Assessment Score':0.3
    }
    effort = sum(row[value] * weight for value, weight in data.items())
    return effort


### whole database ingestion ####

df = pd.read_excel('aircraft_parts_data.xlsx')
df = df.head(100)

for index, row in df.iterrows():
    part_name = row['Part Name']
    mat_comp = row['Material Composition']
    age = row['Age (years)']
    condition = row['Condition'] != 'Used'
    location = row['Location']
    manufacturer = row['Manufacturer']
    aircraft_mod = row['Aircraft Model']
    recycleEfforts = getRecycleEffort(row)
    sustainScore = getSustainibilityScore(row)
    cost = row['Recycled Parts Carbon Footprint (kg CO2e)'] - row['New Parts Carbon Footprint (kg CO2e)']
    # Insert into part_tb
    cursor.execute('INSERT INTO part_tb (part_name, mat_comp, age, condi, location, manufacturer, aircraft_mod, recycle_effort, SustainData, cost) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (part_name, mat_comp, age, condition, location, manufacturer, aircraft_mod, recycleEfforts, sustainScore, cost))
    con.commit()

    last_id = cursor.lastrowid

    pot_usecase = row['Potential Use Cases']
    remanufacPotential = row['Remanufacturing Potential']
    renewableContent= row['Renewable Material Content (%)']
    recycleRate = row['Recycling Rate (%)']
    lca = row['Life Cycle Assessment Score']

    # Insert into sustain_data
    cursor.execute('INSERT INTO sustain_data (sid, pot_usecase, remanufacPotential, renewableContent, recycleRate, lca) VALUES (?, ?, ?, ?, ?, ?)', (last_id, pot_usecase, remanufacPotential, renewableContent, recycleRate, lca))
    con.commit()

    nCarbonFP = row['New Parts Carbon Footprint (kg CO2e)']
    nWaterUsage = row['Water Usage - New Parts (liters)']
    nLandFill = row['Landfill Waste - New Parts (kg)']
    nEneConsum = row['Energy Consumption - New Parts (kWh)']
    nToxicScore = row['Toxicity Score - New Parts']

    # Insert into new_manu_data
    cursor.execute('INSERT INTO new_manu_data (sid, nCarbonFP, nWaterUsage, nLandFill, nEneConsum, nToxicScore)  VALUES (?, ?, ?, ?, ?, ?)', (last_id, nCarbonFP, nWaterUsage, nLandFill, nEneConsum, nToxicScore))
    con.commit()

    rCarbonFP = row['Recycled Parts Carbon Footprint (kg CO2e)']
    rWaterUsage = row['Water Usage - Recycled Parts (liters)']
    rLandFill = row['Landfill Waste - Recycled Parts (kg)']
    rEneConsum = row['Energy Consumption - Recycled Parts (kWh)']
    rToxicScore = row['Toxicity Score - Recycled Parts']
    
    # Insert into recycle_data
    cursor.execute('INSERT INTO recycle_data (sid, rCarbonFP, rWaterUsage, rLandFill, rEneConsum, rToxicScore)  VALUES (?, ?, ?, ?, ?, ?)', (last_id, rCarbonFP, rWaterUsage, rLandFill, rEneConsum, rToxicScore))
    con.commit()




############################################# not required ######################################

# for index, row in df.iterrows():
#     pid = row['pid']
#     part_name = row['Part Name']
#     effort = row['Efforts Score']

#     # Insert into recycleEffortScore
#     cursor.execute('INSERT INTO recycleEffortScore (pid, part_name, effort) VALUES (?, ?, ?)', (pid, part_name, effort))
#     con.commit()

#### cost database ingestion ####

# df = pd.read_excel('cost_final.xlsx')
# df = df.head(100)

# for index, row in df.iterrows():
#     pid = row['pid']
#     part_name = row['Part Name']
#     score = row['Cost']

#     # Insert into costscore
#     cursor.execute('INSERT INTO costScore (pid, part_name, score) VALUES (?, ?, ?)', (pid, part_name, score))
#     con.commit()

### sustainibilityScore database ingestion ####

# df = pd.read_excel('sustainability_score_final.xlsx')
# df = df.head(100)

# for index, row in df.iterrows():
#     pid = row['pid']
#     part_name = row['Part Name']
#     score = row['Sustainability Score']

#     # Insert into sustainabilityScore
#     cursor.execute('INSERT INTO sustainibilityScore (pid, part_name, score) VALUES (?, ?, ?)', (pid, part_name, score))
#     con.commit()