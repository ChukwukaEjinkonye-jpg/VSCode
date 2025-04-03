import csv 

patients = {"Elon Musk": {
        "Networth" : 20000001 , 
        "Health" : 86     
        } ,
        "Jeff Bezos": {
            "Networth" : 700122 , 
            "Health" : 100     
        } , 

        "Frank Reynolds" : {
            "Networth" : 600221 , 
            "Health" : 79
        } , 

        "Charlie Kelly" : {
            "Networth" : 444990 , 
            "Health" : 43 
        } , 

        "Ronald McDonald" : {
            "Networth" : 1204 , 
            "Health" : 40 
        }   
}

for patient, data in patients.items():
    print(f"Patient: {patient}\nNetworth: {data["Networth"]}\nHealth: {data["Health"]}")


csv_filename = "patients.csv"


with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Patient", "Networth", "Health"])  # Write the header
    
    for patient, data in patients.items():
        writer.writerow([patient, data["Networth"], data["Health"]])  # Write each row

print(f"CSV file '{csv_filename}' created successfully.")