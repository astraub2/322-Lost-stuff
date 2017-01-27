import csv
def DC_inventory(counter):
    with open('DC_inventory.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(spamreader)
        print( "INSERT INTO facilities (facilities_pk, common_name) VALUES (1,'DC');")
            
        for p in spamreader:
            asset_tag=(p[0])
            alt_description=(p[1])
            product=(p[1])
            intake=p[4]

            print( "INSERT INTO assets (assets_pk, product_fk, asset_tag, alt_description) VALUES (%s,%s, '%s', '%s');" % (counter, counter, asset_tag, alt_description)) 
            print( "INSERT INTO products (product_pk, description) VALUES (%s, '%s');" % (counter, product))
            print( "INSERT INTO asset_at (asset_fk, facility_fk, arrive_dt) VALUES (%s, 1, '%s');" % (counter, intake))
            counter+=1
        return counter
            

def HQ_inventory(counter):
     with open('HQ_inventory.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(spamreader)
        print( "INSERT INTO facilities (facilities_pk, common_name) VALUES (2, 'HQ');")
        for p in spamreader:
            asset_tag=(p[0])
            alt_description=(p[1])
            product=(p[1])
            intake=p[4]
            print( "INSERT INTO assets (assets_pk, product_fk, asset_tag, alt_description) VALUES (%s,%s, '%s', '%s');" % (counter, counter, asset_tag, alt_description)) 
            print( "INSERT INTO products (product_pk, description) VALUES (%s, '%s');" % (counter, product))
            print( "INSERT INTO asset_at (asset_fk, facility_fk, arrive_dt) VALUES (%s, 2, '%s');" % (counter, intake))
            counter+=1
        return counter
def MB005_inventory(counter):
     with open('MB005_inventory.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(spamreader)
        print( "INSERT INTO facilities (facilities_pk, common_name) VALUES (3,'MB005');")
        
        for p in spamreader:
            asset_tag=(p[0])
            alt_description=(p[1])
            product=(p[1])
            intake=p[4]
            print( "INSERT INTO assets (assets_pk, product_fk, asset_tag, alt_description) VALUES (%s,%s, '%s', '%s');" % (counter, counter, asset_tag, alt_description)) 
            print( "INSERT INTO products (product_pk, description) VALUES (%s, '%s');" % (counter, product))
            print( "INSERT INTO asset_at (asset_fk, facility_fk, arrive_dt) VALUES (%s, 3, '%s');" % (counter, intake))
            counter+=1
        return counter
def NC_inventory(counter):
     with open('HQ_inventory.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(spamreader)
        print( "INSERT INTO facilities (facilities_pk, common_name) VALUES (4,'NC');")
        
        for p in spamreader:
            asset_tag=(p[0])
            alt_description=(p[1])
            product=(p[1])
            intake=p[4]
            print( "INSERT INTO assets (assets_pk, product_fk, asset_tag, alt_description) VALUES (%s,%s, '%s', '%s');" % (counter, counter, asset_tag, alt_description)) 
            print( "INSERT INTO products (product_pk, description) VALUES (%s, '%s');" % (counter, product))
            print( "INSERT INTO asset_at (asset_fk, facility_fk, arrive_dt) VALUES (%s, 4, '%s');" % (counter, intake))
            counter+=1
        return counter

def SPNV_inventory(counter):
    with open('SPNV_inventory.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(spamreader)
        print( "INSERT INTO facilities (facilities_pk, common_name) VALUES (5,'NC');")
        
        for p in spamreader:
            asset_tag=(p[0])
            alt_description=(p[1])
            product=(p[1])
            intake=p[4]
            print( "INSERT INTO assets (assets_pk, product_fk, asset_tag, alt_description) VALUES (%s,%s, '%s', '%s');" % (counter, counter, asset_tag, alt_description)) 
            print( "INSERT INTO products (product_pk, description) VALUES (%s, '%s');" % (counter, product))
            print( "INSERT INTO asset_at (asset_fk, facility_fk, arrive_dt) VALUES (%s, 5, '%s');" % (counter, intake))
            counter+=1
        return counter
    
def acquisitions(counter):
   with open('acquisitions.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(spamreader)
        for p in spamreader:
            asset_tag=p[5]
            alt_description=(p[0])
            product=(p[0])
            print("IF NOT EXISTS ( SELECT * FROM assets WHERE asset_tag= '%s'" %(asset_tag))
            print("BEGIN")
            print( "INSERT INTO assets (assets_pk, product_fk, asset_tag, alt_description) VALUES (%s,%s, '%s', '%s');" % (counter, counter, asset_tag, alt_description)) 
            print( "INSERT INTO products (product_pk, description) VALUES (%s, '%s');" % (counter, product))
            print("END")
            counter+=1

        return counter
   
def convoy(counter):
    ccnt=0
    with open('convoy.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(spamreader)
        for p in spamreader:
            print( "INSERT INTO convoys (convoy_pk) VALUES (%s);" % (ccnt))
            i=7
            while(i<len(p)):
                alt_description=p[i]
                product=p[i]
                print( "INSERT INTO assets (assets_pk, product_fk, alt_description) VALUES (%s,%s, '%s');" % (counter, counter,alt_description))
                print( "INSERT INTO products (product_pk, description) VALUES (%s, '%s');" % (counter, product))
                i+=1
                counter+=1
            ccnt+=1
        return counter
            
def security_levels():
    with open('security_levels.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(spamreader)
        levelcnt=0
        for p in spamreader:
            level=(p[0])
            comment=(p[1])
            print( "INSERT INTO levels (level_pk, abbrv, comment) VALUES (%s, '%s', '%s');" % (levelcnt, level, comment))
            levelcnt+=1
def product_list(counter):
    with open('product_list.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(spamreader)
        for p in spamreader:
            name=(p[0])
            description=(p[1])
            print( "INSERT INTO assets (assets_pk, product_fk, alt_description) VALUES (%s,'%s','%s');" % (counter, counter, description)) 
            print( "INSERT INTO products (product_pk, description) VALUES (%s, '%s');" % (counter, name))
            counter+=1
        return counter
        
##really hard
def transit():
    with open('product_list.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(spamreader)
        ##hardcode
        print("UPDATE asset_at SET facilities_pk=3 WHERE asset_tag='CA15467287';")
        print("UPDATE asset_at SET facilities_pk=3 WHERE asset_tag='CA15467288';")
        print("UPDATE asset_at SET facilities_pk=3 WHERE asset_tag='CA15467289';")
        print("UPDATE asset_at SET facilities_pk=3 WHERE asset_tag='CA15467290';")

        print("UPDATE asset_at SET facilities_pk=4 WHERE asset_tag='CA15467291';")
        print("UPDATE asset_at SET facilities_pk=4 WHERE asset_tag='CA15467292';")
        print("UPDATE asset_at SET facilities_pk=4 WHERE asset_tag='CA15467293';")
        print("UPDATE asset_at SET facilities_pk=4 WHERE asset_tag='CA15467294';")

        print("UPDATE asset_at SET facilities_pk=5 WHERE asset_tag='CA15467295';")
        print("UPDATE asset_at SET facilities_pk=5 WHERE asset_tag='CA15467296';")

        print("UPDATE asset_at SET facilities_pk=1 WHERE asset_tag='DC15467299';")
        print("UPDATE asset_at SET facilities_pk=1 WHERE asset_tag='DC25467300';")
        print("UPDATE asset_at SET facilities_pk=1 WHERE asset_tag='DC25467301';")
        print("UPDATE asset_at SET facilities_pk=1 WHERE asset_tag='DC25467302';")
        
        
        
def facilities():
    print( "INSERT INTO facilities (facilities_pk, common_name, location) VALUES (1, 'DC', 'Washington');")
    print( "INSERT INTO facilities (facilities_pk, common_name, location) VALUES (2, 'HQ', 'CLASSIFIED');" )
    print( "INSERT INTO facilities (facilities_pk, common_name, location) VALUES (3, 'MB005', 'CLASSIFIED');" )
    print( "INSERT INTO facilities (facilities_pk, common_name, location) VALUES (4, 'NC', 'North Carolina');" )
    print( "INSERT INTO facilities (facilities_pk, common_name, location) VALUES (5, 'SPNV', 'Nevada');")
           
def main():
    facilities()
    counter=0
    counter=DC_inventory(counter)
    counter=HQ_inventory(counter)
    counter=MB005_inventory(counter)
    counter=NC_inventory(counter)
    counter=SPNV_inventory(counter)
    counter=acquisitions(counter)
##    counter=convoy(counter)
##    counter=product_list(counter)
##    security_levels()
##    transit()
  
  
if __name__== "__main__":
  main()
