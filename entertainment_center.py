import media, the_reel, random

#Create Movie objects
bottle_rocket = media.Movie("tt0115734",
                            "https://www.youtube.com/watch?v=hspUSez-rYY")
full_metal_jacket = media.Movie("tt0093058",
                                "https://www.youtube.com/watch?v=UuWmCVdwhKg")
death_proof = media.Movie("tt1028528",
                          "https://www.youtube.com/watch?v=7mICGcg5-pM")
tremors = media.Movie("tt0100814",
                      "https://www.youtube.com/watch?v=hiAIvcWJ_yM")
alien = media.Movie("tt0078748",
                    "https://www.youtube.com/watch?v=f9tlCjlhNtE")
children_of_men = media.Movie("tt0206634",
                              "https://www.youtube.com/watch?v=Esrf8X07eZk")
mud = media.Movie("tt1935179",
                  "https://www.youtube.com/watch?v=OSLYyPK2vsc")
big_fish = media.Movie("tt0319061",
                       "https://www.youtube.com/watch?v=rziFIdDjfHo")
bio_dome = media.Movie("tt0115683",
                       "https://www.youtube.com/watch?v=4EWikCCfHJw")
the_matrix = media.Movie("tt0133093",
                         "https://www.youtube.com/watch?v=a94b1yZOBes")
the_boondock_saints = media.Movie("tt0144117",
                                  "https://www.youtube.com/watch?v=vVdxMxr1UJQ")
jaws = media.Movie("tt0073195",
                   "https://www.youtube.com/watch?v=3hIvvho2T1k")

#Create a list of objects
movies = [
    bottle_rocket, full_metal_jacket, death_proof, tremors,
    alien, children_of_men, mud, big_fish,
    bio_dome, the_matrix, the_boondock_saints, jaws
    ]

#Send list of objects to the 
the_reel.open_movies_page(movies)
