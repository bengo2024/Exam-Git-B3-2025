def login(username, password):
    if username == "admin" and password == "bengo":
        print("Connexion réussi")
    else:
        print("Connexion échoué")

print("Hello World")
login("admin", "bengo")  # Test