import csv

def importcsvfiles(filepath, dest_list_name):
 
    with open(filepath,"r") as csvfile: 
        csvreader = csv.reader(csvfile,delimiter=",")
        
        nxt_12 = next(csvreader) # we are skipping one row on this step(header)
      
        for item in csvreader:  
            
            dest_list_name.append(item)



def import_csvfiles_skip(filepath, dest_list_name,noskips):
 
    with open(filepath,"r") as csvfile:  
        
        csvreader = csv.reader(csvfile,delimiter=",")
        
        if noskips == 1:
            nxt_12 = next(csvreader) # we are skipping one row on this step(header)
        else:
            nxt_12 =next(csvreader)  # we are skipping 2 rows on this step (header+ 1st row)
            nxt_22 =next(csvreader)

        
        for item in csvreader:  
            
            dest_list_name.append(item)


