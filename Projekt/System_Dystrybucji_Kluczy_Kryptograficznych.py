import random

# Baza danych której zadaniem jest przechowywanie użytkowników, ich kluczy publicznych
# oraz z którymi użytkownikami może wykonać wymianę klucza

database = {
    "user1": {"public_key": None, "authorized_users": ["user2", "user3"]},
    "user2": {"public_key": None, "authorized_users": ["user1"]},
    "user3": {"public_key": None, "authorized_users": ["user1", "user2"]},
}

PRIME = 23
BASE = 5

def generate_key(prime, generator):
    private_key = random.randint(1, prime - 1)
    public_key = pow(generator, private_key, prime)
    return private_key, public_key

def authorize(database, user, other_user):
    return other_user in database.get(user, {}).get("authorized_users", [])

def shared_secret(prime, private_key, other_public_key):
    return pow(other_public_key, private_key, prime)

def register_user_public_key(database, user, public_key):
    if user in database:
        database[user]["public_key"] = public_key
    else:
        raise ValueError("User not found in database.")

def verify_user(database, user):
    return user in database and database[user]["public_key"] is not None

def central_authorization(server_db, user1, user2):
    return authorize(server_db, user1, user2) and authorize(server_db, user2, user1)

# Wykorzystuję funkcje do stworzenia klucza prywatnego oraz publicznego
private_key1, public_key1 = generate_key(PRIME, BASE)
private_key2, public_key2 = generate_key(PRIME, BASE)
private_key3, public_key3 = generate_key(PRIME, BASE)


# Jest tu używana funkcja do rejestracji kluczy publiczne użytkowników do bazy danych

register_user_public_key(database, "user1", public_key1)
register_user_public_key(database, "user2", public_key2)
register_user_public_key(database, "user3", public_key3)

def exchange_keys(user_a, user_b):
    if verify_user(database, user_a) and verify_user(database, user_b):
        if central_authorization(database, user_a, user_b):
            private_key_a = globals()[f"private_key{user_a[-1]}"]
            public_key_b = database[user_b]["public_key"]
            secret_key = shared_secret(PRIME, private_key_a, public_key_b)
            print(f"Shared secret of {user_a} and {user_b}: {secret_key}")
        else:
            print(f"Users {user_a} and {user_b} are not authorized to exchange keys.")
    else:
        print(f"One or both users {user_a} and {user_b} are not verified.")


# Tutaj jest wykonywana wymiana kluczy pomiędzy użytkownika

exchange_keys("user1", "user2")
exchange_keys("user1", "user3")
exchange_keys("user2", "user3")

