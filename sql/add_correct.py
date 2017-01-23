import csv
import psycopg2
import sys

# Setup the database connection
conn = psycopg2.connect(dbname=sys.argv[1],host='127.0.0.1',port=int(sys.argv[2]))
cursor = conn.cursor()
#######
with open('acquisitions.csv', newline='') as csvfile:
    #parameters :product,purchase, order, number,order,
    #date,ship, date,arrive, date,asset, tag
     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
     next(spamreader)
     for p in spamreader:
         print(p[1])
##         format_str2 ="""INSERT INTO assets (assets_pk, product_fk, asset_tag, alt_description)
##         VALUES (NULL, NULL, "{asset_tag}", "{description}");"""
##         sql_command2= format_str2.format(asset_tag=p[8], description=p[0])
##with open('convoy.csv', newline='') as csvfile:
##    ##transport request #,depart time,waypoint1 time,waypoint 2 time,
##    ##waypoint 3 time,waypoint 4 time,arrive time,assigned vehicles
##     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
##     next(spamreader)
##     for p in spamreader:
##         format_str1 = """INSERT INTO convoy (convoy_pk, request,source_fk, dest_fk, depart_dt, arrive_dt)
##         VALUES (NULL, "{request}", NULL, NULL, "{depart_dt}", "{arrive_dt}");"""
##         sql_command1 = format_str1.format(request=p[0], depart_dt=p[1], arrive_dt=p[6])
##         cursor.execute(sql_command1)
##with open('DC_inventory.csv', newline='') as csvfile:
##    ##asset tag,product,room,compartments,intake date,expunged date
##     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
##     next(spamreader)
##     for p in spamreader:
##         format_str1 = """INSERT INTO assets (assets_pk, product_fk, asset_tag, alt_description)
##         VALUES (NULL, NULL, "{asset tag}", "{alt_description}");"""
##         sql_command1 = format_str1.format(asset_tag=p[0], alt_description=p[1])
##         cursor.execute(sql_command1)
##        
##########################
##with open('HQ_inventory.csv', newline='') as csvfile:
##    ##asset tag,product,room,compartments,intake date,expunged date
##     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
##     next(spamreader)
##     for p in spamreader:
##         format_str1 = """INSERT INTO assets (assets_pk, product_fk, asset_tag, alt_description)
##         VALUES (NULL, NULL, "{asset tag}", "{alt_description}");"""
##         sql_command1 = format_str1.format(asset_tag=p[0], alt_description=p[1])
##         cursor.execute(sql_command1)
##with open('MB005_inventory.csv', newline='') as csvfile:
##    ##asset tag,product,room,compartments,intake date,expunged date
##     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
##     next(spamreader)
##     for p in spamreader:
##         format_str1 = """INSERT INTO assets (assets_pk, product_fk, asset_tag, alt_description)
##         VALUES (NULL, NULL, "{asset tag}", "{alt_description}");"""
##         sql_command1 = format_str1.format(asset_tag=p[0], alt_description=p[1])
##         cursor.execute(sql_command1)
##with open('NC_inventory.csv', newline='') as csvfile:
##    ##asset tag,product,room,compartments,intake date,expunged date
##     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
##     next(spamreader)
##     for p in spamreader:
##         format_str1 = """INSERT INTO assets (assets_pk, product_fk, asset_tag, alt_description)
##         VALUES (NULL, NULL, "{asset tag}", "{alt_description}");"""
##         sql_command1 = format_str1.format(asset_tag=p[0], alt_description=p[1])
##         cursor.execute(sql_command1)        
##with open('SPNV_inventory.csv', newline='') as csvfile:
##    ##asset tag,product,room,compartments,intake date,expunged date
##     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
##     next(spamreader)
##     for p in spamreader:
##         format_str1 = """INSERT INTO assets (assets_pk, product_fk, asset_tag, alt_description)
##         VALUES (NULL, NULL, "{asset tag}", "{alt_description}");"""
##         sql_command1 = format_str1.format(asset_tag=p[0], alt_description=p[1])
##         cursor.execute(sql_command1)
###############
####product_list
##with open('product_list.csv', newline='') as csvfile:
##    ##name,model,description,unit price,vendor,compartments
##     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
##     next(spamreader)
##     for p in spamreader:
##         format_str1 = """INSERT INTO products (product_pk, vendor, description, alt_description)
##         VALUES (NULL,"{vendor}", "{description}", "{alt_description}");"""
##         sql_command1 = format_str1.format(vendor=p[5], description=p[0], alt_description=p[2])
##         cursor.execute(sql_command1)
####security_compartments
##with open('security_compartments.csv', newline='') as csvfile:
##    ##compartment_tag,compartment_desc
##     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
##     next(spamreader)
##     for p in spamreader:
##         format_str1 = """INSERT INTO compartments (compartment_pk, abbrv, comment)
##         VALUES (NULL,"{abbrv}", "{comment}");"""
##         sql_command1 = format_str1.format(abbrv=p[1], comment=p[2])
##         cursor.execute(sql_command1)
##        
####security_levels
##with open('security_levels.csv', newline='') as csvfile:
##    ##level, description
##     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
##     next(spamreader)
##     for p in spamreader:
##         format_str1 = """INSERT INTO levels (level_pk, abbrv, comment)
##         VALUES (NULL,"{abbrv}", "{comment}");"""
##         sql_command1 = format_str1.format(abbrv=p[1], comment=p[2])
##         cursor.execute(sql_command1)
####transit
##with open('transit.csv', newline='') as csvfile:
##    ##asset tag,src facility,dst facility,depart date,
##    ##arrive date,transport request #,Comments
##     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
##     next(spamreader)
##     for p in spamreader:
##         format_str1 = """INSERT INTO assets (assets_pk, product_fk, asset_tag, alt_description)
##         VALUES (NULL, NULL, "{asset_tag}", "{alt_description}");"""
##         sql_command1 = format_str1.format(asset_tag=p[0])
##         cursor.execute(sql_command1)
##        
####vendors
##
