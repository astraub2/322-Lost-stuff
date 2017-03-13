import csv

#easy
def import_facilities():
        with open("facilities.csv") as f:
                facilities = csv.reader(f, skipinitialspace=True)
                next(facilities)
                for s in facilities:
                        print("INSERT INTO facilities (fcode, common_name) VALUES ('{}', '{}');".format(s[0], s[1]))

def import_users():
        with open("users.csv") as f:
                users = csv.reader(f, skipinitialspace=True)
                next(users)
                print("INSERT INTO roles (role_name) VALUES ('Logistics Officer');")
                print("INSERT INTO roles (role_name) VALUES ('Facilities Officer');")
                for s in users:
                        print("INSERT INTO users (username, password, role_fk, active) VALUES ('{}', '{}',(SELECT role_pk FROM roles WHERE role_name='{}'), '{}');".format(s[0], s[1],s[2], s[3]))
                
def import_assets():
        with open("assets.csv") as f:
                assets = csv.reader(f, skipinitialspace=True)
                next(assets)
                for s in assets:
                        if s[4]=='NULL':
                                print("INSERT INTO assets (asset_tag, alt_description)\
                              VALUES ('{}', '{}');".format(s[0], s[1]))
                                print("INSERT INTO asset_at (asset_fk, facility_fk, arrive_dt) VALUES\
                              ((SELECT assets_pk FROM assets WHERE asset_tag='{}'), (SELECT\
                              facilities_pk FROM facilities WHERE fcode='{}'), '{}');".format(s[0], s[2], s[3]))
                        else:
                                print("INSERT INTO assets (asset_tag, alt_description, disposed_dt)\
                                      VALUES ('{}', '{}', '{}');".format(s[0], s[1], s[4]))
                                print("INSERT INTO asset_at (asset_fk, facility_fk, arrive_dt) VALUES\
                                      ((SELECT assets_pk FROM assets WHERE asset_tag='{}'), (SELECT\
                                      facilities_pk FROM facilities WHERE fcode='{}'), '{}');".format(s[0], s[2], s[3]))
def import_transfers():
	with open("transfers.csv") as f:
		transfers = csv.reader(f, skipinitialspace=True)
		next(transfers)
		for s in transfers:
			print("""INSERT INTO transfer (requestor_fk, request_dt, approver_fk, approval_dt, source_fk, destination_fk, asset_fk) VALUES 
				((SELECT user_pk FROM users WHERE username='{}'), '{}', (SELECT user_pk FROM users WHERE username='{}'), 
				'{}', (SELECT facilities_pk FROM facilities WHERE fcode='{}'), 
				(SELECT facilities_pk FROM facilities WHERE fcode='{}'), (SELECT assets_pk FROM assets WHERE asset_tag='{}'));
				""".format(s[1], s[2], s[3], s[4], s[5], s[6], s[0]))
			print("""INSERT INTO transit (transfer_fk, asset_fk, load_dt, unload_dt) VALUES ((SELECT transfer_pk FROM transfer WHERE asset_fk=(SELECT assets_pk FROM assets WHERE asset_tag='{}') 
				AND request_dt=(SELECT max(request_dt) FROM transfer WHERE asset_fk=(SELECT asset_pk FROM assets WHERE asset_tag='{}'))), 
				(SELECT assets_pk FROM assets WHERE asset_tag='{}'), '{}', '{}');""".format(s[0], s[0], s[0], s[7], s[8]))
			print("UPDATE asset_at SET depart_dt='{}' WHERE asset_fk=(SELECT assets_pk FROM assets WHERE asset_tag='{}') AND depart_dt IS NULL;".format(s[7], s[0]))
			print("""INSERT INTO asset_at (asset_fk, facility_fk, arrive_dt) VALUES ((SELECT asset_pk FROM assets WHERE asset_tag='{}'), 
				(SELECT facility_pk FROM facilities WHERE facility_fcode='{}'), '{}');""".format(s[0], s[6], s[8]))

                        
if __name__ == "__main__":
        import_facilities()
        import_assets()
        import_users()
        import_transfers()
