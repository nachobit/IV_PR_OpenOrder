from openGestion import db
from openGestion.users.models import User

db.create_all()

# insert data
#db.session.add(User("pepito", "pepe@email.com", "1234"))
#db.session.add(User("admin", "ad@admin.com", "admin"))
db.session.add(User("mike", "mike@herman.com", "tell"))

# commit the changes
db.session.commit()