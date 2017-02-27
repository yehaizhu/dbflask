# -*- coding: utf-8 -*-


from hello import Role, User, db

admin_role = Role(name='Admin')
mod_role = Role(name='Moderator')
user_role = Role(name='User')
user_john = User(username='john', role=admin_role)
user_susan = User(username='susan', role=mod_role)
user_david = User(username='david', role=user_role)

db.session.add(admin_role)
db.session.add(mod_role)
db.session.add(user_role)
db.session.add(user_john)
db.session.add(user_susan)
db.session.add(user_david)
db.session.commit()




print admin_role.id,admin_role.name
print "----------"

print user_role.id,user_role.name

print "----------"

print mod_role.id,mod_role.name

print "----------"

print user_john.id,user_john.username

print "----------"

print user_susan.id,user_susan.username

print "----------"

print user_david.id,user_david.username


print "----修改-----"
admin_role.name = 'sss'
db.session.add(admin_role)
db.session.commit()

print admin_role.name







