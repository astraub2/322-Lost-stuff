import csv
def DC_inventory(counter):
    with open('DC_inventory.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(spamreader)
        print( "INSERT INTO facilities (facilities_pk, common_name) VALUES (1,'DC')")
            
        for p in spamreader:
            asset_tag=p[0]
            alt_description=p[1]
            product=p[1]
            print( "INSERT INTO assets (asset_pk, asset_tag, alt_description) VALUES (%s, %s, %s);" % (counter, asset_tag, alt_description)) 
            print( "INSERT INTO products (product_pk, description) VALUES (%s, %s);" % (counter, product))
            print( "INSERT INTO assets_at (asset_fk, facility_fk) VALUES (%s, 1);" % (counter))
            counter+=1
        return counter
            

def HQ_inventory(counter):
     with open('HQ_inventory.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(spamreader)
        print( "INSERT INTO facilities (facilities_pk, common_name) VALUES (2, 'HQ')")
        for p in spamreader:
            asset_tag=p[0]
            alt_description=p[1]
            product=p[1]
            print( "INSERT INTO assets (asset_pk, asset_tag, alt_description) VALUES (%s, %s, %s);" % (counter, asset_tag, alt_description)) 
            print( "INSERT INTO products (product_pk, description) VALUES (%s, %s);" % (counter, product))
            print( "INSERT INTO assets_at (asset_fk, facility_fk) VALUES (%s, 2);" % (counter))
            counter+=1
        return counter
def MB005_inventory(counter):
     with open('MB005_inventory.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(spamreader)
        print( "INSERT INTO facilities (facilities_pk, common_name) VALUES (3,'MB005')")
        
        for p in spamreader:
            asset_tag=p[0]
            alt_description=p[1]
            product=p[1]
            print( "INSERT INTO assets (asset_pk, asset_tag, alt_description) VALUES (%s, %s, %s);" % (counter, asset_tag, alt_description)) 
            print( "INSERT INTO products (product_pk, description) VALUES (%s, %s);" % (counter, product))
            print( "INSERT INTO assets_at (asset_fk, facility_fk) VALUES (%s, 3);" % (counter))
            counter+=1
        return counter
def NC_inventory(counter):
     with open('HQ_inventory.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(spamreader)
        print( "INSERT INTO facilities (facilities_pk, common_name) VALUES (4,'NC')")
        
        for p in spamreader:
            asset_tag=p[0]
            alt_description=p[1]
            product=p[1]
            print( "INSERT INTO assets (asset_pk, asset_tag, alt_description) VALUES (%s, %s, %s);" % (counter, asset_tag, alt_description)) 
            print( "INSERT INTO products (product_pk, description) VALUES (%s, %s);" % (counter, product))
            print( "INSERT INTO assets_at (asset_fk, facility_fk) VALUES (%s, 4);" % (counter))
            counter+=1
        return counter

def SPNV_inventory(counter):
 with open('SPNV_inventory.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(spamreader)
        print( "INSERT INTO facilities (facilities_pk, common_name) VALUES (5,'SPNV')")
        
        for p in spamreader:
            asset_tag=p[0]
            alt_description=p[1]
            product=p[1]
            print( "INSERT INTO assets (asset_pk, asset_tag, alt_description) VALUES (%s, %s, %s);" % (counter, asset_tag, alt_description)) 
            print( "INSERT INTO products (product_pk, description) VALUES (%s, %s);" % (counter, product))
            print( "INSERT INTO assets_at (asset_fk, facility_fk) VALUES (%s, 5);" % (counter))
            counter+=1
        return counter
##def acquisitions():
##    #with open('acquisitions.csv', newline='') as csvfile:
##    
##def convoy():
##    
##def product_list():
##    
##def security_levels():
##    
##def transit():

def main():
    counter=0
    DC_inventory(counter)
    HQ_inventory(counter)
    MB005_inventory(counter)
    NC_inventory(counter)
    SPNV_inventory(counter)
##    acquisitions()
##    convoy()
##  product_list()
##  security_level()
##  transit()
  
  
if __name__== "__main__":
  main()
