\echo 'username,password,role,active'
SELECT users.username, users.password, roles.role_name, users.active
 FROM users LEFT JOIN roles ON role_fk=role_pk;