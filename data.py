import mysql.connector

bdd = None
cursor = None

def connexion():
    global bdd
    global cursor
    bdd = mysql.connector.connect(user='root', 
                                  password='example', 
                                  host= '127.0.0.1', 
                                  port = 3307, 
                                  database='ddb_don')
    cursor = bdd.cursor(buffered=True)

def deconnexion():
    global bdd
    global cursor
    cursor.close()
    bdd.close()

def enregistrer_promesse(nom, prenom, adresse, email, somme_promise):
    global cursor
    connexion()
    query = "INSERT INTO promesses_don (nom, prenom, adresse, email, somme_promise) VALUES (%s, %s, %s, %s, %s)"
    values = (nom, prenom, adresse, email, somme_promise)
    cursor.execute(query, values)
    bdd.commit()
    deconnexion()

def lire_promesses():
    global cursor
    connexion()
    query = "SELECT * FROM promesses_don"
    cursor.execute(query)
    promesses = []
    for enregistrement in cursor:
        promesse = {}
        promesse['id'] = enregistrement[0]
        promesse['nom'] = enregistrement[1]
        promesse['prenom'] = enregistrement[2]
        promesse['adresse'] = enregistrement[3]
        promesse['email'] = enregistrement[4]
        promesse['somme_promise'] = enregistrement[5]
        promesses.append(promesse)
    deconnexion()
    return promesses

def lire_promesse_par_id(id):
    global cursor
    connexion()
    query = "SELECT * FROM promesses_don WHERE id = %s"
    values = (id,)
    cursor.execute(query, values)
    promesse = cursor.fetchone()
    if promesse:
        promesse_info = {
            'id': promesse[0],
            'nom': promesse[1],
            'prenom': promesse[2],
            'adresse': promesse[3],
            'email': promesse[4],
            'somme_promise': promesse[5]
        }
    else:
        promesse_info = None
    deconnexion()
    return promesse_info
