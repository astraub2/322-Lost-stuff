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
                        print("INSERT INTO assets (asset_tag, alt_description, disposed_dt)\
                              VALUES ({}, '{}', {});".format(s[0], s[1], s[4]))
                        print("INSERT INTO asset_at (asset_fk, facility_fk, arrive_dt) VALUES\
                              ((SELECT assets_pk FROM assets WHERE asset_tag='{}'), (SELECT\
                              facilities_pk FROM facilities WHERE fcode='{}'), {});".format(s[0], s[2], s[3]))
if __name__ == "__main__":
        import_facilities()
        import_assets()
        import_users()
        #import_transfers()
