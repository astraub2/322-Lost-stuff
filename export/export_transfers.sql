SELECT assets.asset (FROM transfers JOIN assets ON assets_pk=asset_fk), users.username(FROM transfers JOIN users ON requestor_fk=user_pk),\
 users.username(FROM transfers JOIN users ON approver_fk=user_pk), transfer.approve_dt, facilities.fcode(FROM transfers JOIN facilities\
 	ON facilities_pk=source_fk),facilities.fcode(FROM transfers JOIN facilities ON facilities_pk=destination_fk), transit.load_dt\
 (FROM transit Join transfer ON asset_fk), transit.unload_dt (FROM transit Join transfer ON asset_fk) FROM transfer);
