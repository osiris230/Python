class SalleCinema:
    def __init__(self, total_places=10, total_places_speciales=2):
        self.reservations = {}
        self.reservatons_speciale = {}
        self.total_places = total_places
        self.total_places_speciales = total_places_speciales

    def reserver_place(self, nom, place):
        if len(self.reservations) >= self.total_places:
            print("Désolé, toutes les places sont déjà réservées.")
            return

        if place < 1 or place > self.total_places:
            print("Cette place n'existe pas dans la salle.")
            return

        if place in self.reservations:
            print("Désolé, cette place est déjà prise.")
        else:
            self.reservations[place] = nom
            print(f"Place {place} réservée pour {nom}.")

    def afficher_places_reservees(self):
        if self.reservations:
            print("Liste des places réservées :")
            for place, nom in self.reservations.items():
                print(f"Place {place} réservée par {nom}.")
        else:
            print("Aucune place réservée pour le moment.")

    def nombre_places_disponibles(self):
        places_disponibles = self.total_places - len(self.reservations)
        print(f"Nombre de places disponibles : {places_disponibles}")

    def filtrer_reservations_par_personne(self, nom):
        trouve = False
        print(f"Recherche de réservations pour {nom}...")

        for place, res_nom in self.reservations.items():
            if res_nom == nom:
                if not trouve:
                    print(f"Réservations faites par {nom} :")
                    trouve = True  
                print(f"Place {place}")
        if not trouve:
            print(f"Aucune réservation trouvée pour {nom}.")

    def annuler_reservation(self, nom):
        places_a_annuler = list(self.reservations.keys())  
        annulation_effectuee = False
    
        for place in places_a_annuler:
            if self.reservations.get(place) == nom:
                del self.reservations[place] 
                annulation_effectuee = True
            
        if annulation_effectuee:
            print(f"Toutes les réservations pour {nom} ont été annulées.")
        else:
            print(f"Aucune réservation trouvée pour {nom}, donc rien à annuler.")


salle_cinema = SalleCinema(10)
salle_cinema.reserver_place("Ginette", 1)
salle_cinema.reserver_place("Bob", 2)
salle_cinema.reserver_place("Charle", 1)
salle_cinema.nombre_places_disponibles() 
salle_cinema.afficher_places_reservees()
salle_cinema.filtrer_reservations_par_personne("Ginette")
salle_cinema.annuler_reservation("Bob")
salle_cinema.afficher_places_reservees()