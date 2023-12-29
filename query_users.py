from flaskblog import app, User

# Create an application context
with app.app_context():
    # Query all users
    all_users = User.query.all()
    
    # Print the users
    for user in all_users:
        print(f"Username: {user.username}, Email: {user.email}")

print("User query completed!")

