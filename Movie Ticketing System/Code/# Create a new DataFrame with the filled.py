# Create a new DataFrame with the filled data
data_filled = {
    'title': [
        'IF', 'Deadpool and Wolverine', 'Inside Out 2', 'The Garfield Movie', 'Abigail', 
        'Furiosa: A Mad Max Saga', 'Moana 2', 'Immaculate', 'No Way Up', 'Alien: Romulus', 
        'The First Omen', 'Dune: Part Two', 'Atlas', 'Chief of Station', 'Arcadian', 
        'Damsel', 'The Crow', 'Wanted Man', 'Spellbound', 'It Ends with Us', 
        'Upgraded', 'A Family Affair', 'Joker: Folie a Deux', 'Sleeping Dogs'
    ],
    'duration': [
        '1h 44m', '2h 19m', '1h 55m', '1h 50m', '1h 46m', '2h 12m', '1h 47m', '1h 50m', 
        '1h 38m', '2h 5m', '1h 52m', '2h 35m', '1h 56m', '1h 45m', '1h 43m', '1h 52m', 
        '2h 10m', '1h 50m', '1h 48m', '1h 45m', '1h 54m', '1h 40m', '2h 30m', '1h 47m'
    ],
    'pg_rating': [
        'PG', 'R', 'PG', 'PG', 'PG-13', 'R', 'PG', 'PG-13', 'PG-13', 'R', 'R', 'PG-13', 
        'PG-13', 'R', 'PG', 'PG-13', 'R', 'R', 'PG', 'PG-13', 'R', 'PG-13', 'R', 'R'
    ],
    'movie_rating': [
        6.7, 8.5, 7.5, 6.3, 6.8, 8.1, 7.2, 6.9, 7.0, 7.4, 7.1, 8.3, 6.5, 6.8, 7.2, 6.9, 
        8.0, 6.7, 7.3, 6.6, 7.1, 6.4, 8.6, 6.9
    ],
    'genre': [
        ["Fantasy", "Drama"], ["Action", "Comedy"], ["Animation", "Family"], ["Animation", "Comedy"], ["Adventure", "Fantasy"], 
        ["Action", "Adventure"], ["Animation", "Family"], ["Horror", "Thriller"], ["Thriller", "Adventure"], ["Sci-Fi", "Horror"], 
        ["Horror"], ["Sci-Fi", "Adventure"], ["Action", "Sci-Fi"], ["Action", "Thriller"], ["Drama", "Mystery"], 
        ["Fantasy", "Adventure"], ["Action", "Fantasy"], ["Action", "Thriller"], ["Animation", "Fantasy"], ["Drama", "Romance"], 
        ["Sci-Fi", "Thriller"], ["Comedy", "Romance"], ["Drama", "Thriller"], ["Action", "Thriller"]
    ],
    'directors': [
        ["John Krasinski"], ["Shawn Levy"], ["Kelsey Mann"], ["Mark Dindal"], ["Aleksandr Boguslavskiy"], 
        ["George Miller"], ["John Musker", "Ron Clements"], ["Michael Chaves"], ["Scott Mann"], ["Fede Álvarez"], 
        ["Arkasha Stevenson"], ["Denis Villeneuve"], ["Brad Peyton"], ["Julius Avery"], ["Nathaniel Martello-White"], 
        ["Juan Carlos Fresnadillo"], ["Rupert Sanders"], ["David Leitch"], ["Vicky Jenson"], ["Justin Baldoni"], 
        ["Leigh Whannell"], ["Richard Curtis"], ["Todd Phillips"], ["Jonathan Mostow"]
    ],
    'actors': [
        ["Ryan Reynolds", "Phoebe Waller-Bridge"], ["Ryan Reynolds", "Hugh Jackman"], ["Amy Poehler", "Bill Hader"], 
        ["Chris Pratt", "Samuel L. Jackson"], ["Tinatin Dalakishvili", "Eddie Marsan"], ["Anya Taylor-Joy", "Chris Hemsworth"], 
        ["Auli'i Cravalho", "Dwayne Johnson"], ["Vera Farmiga", "Patrick Wilson"], ["Gemma Arterton", "Jack Huston"], 
        ["Katherine Waterston", "Michael Fassbender"], ["Bill Nighy", "Nell Tiger Free"], ["Timothée Chalamet", "Zendaya"], 
        ["Jennifer Lopez", "Sterling K. Brown"], ["Aaron Taylor-Johnson", "John Cena"], ["Naomi Watts", "Ruth Wilson"], 
        ["Millie Bobby Brown", "Angela Bassett"], ["Bill Skarsgård", "FKA Twigs"], ["Jake Gyllenhaal", "Jessica Chastain"], 
        ["Rachel Zegler", "Nicole Kidman"], ["Blake Lively", "Justin Baldoni"], ["Logan Marshall-Green", "Betty Gabriel"], 
        ["Emma Stone", "Andrew Garfield"], ["Joaquin Phoenix", "Lady Gaga"], ["Russell Crowe", "Karen Gillan"]
    ],
    'image': [
        "https://media.themoviedb.org/t/p/w600_and_h900_bestv2/if_image.jpg", "https://media.themoviedb.org/t/p/w600_and_h900_bestv2/deadpool_wolverine_image.jpg", 
        "https://media.themoviedb.org/t/p/w600_and_h900_bestv2/inside_out_2_image.jpg", "https://media.themoviedb.org/t/p/w600_and_h900_bestv2/garfield_image.jpg", 
        "https://media.themoviedb.org/t/p/w600_and_h900_bestv2/abigail_image.jpg", "https://media.themoviedb.org/t/p/w600_and_h900_bestv2/furiosa_image.jpg", 
        "https://media.themoviedb.org/t/p/w600_and_h900_bestv2/moana_2_image.jpg", "https://media.themoviedb.org/t/p/w600_and_h900_bestv2/immaculate_image.jpg", 
        "https://media.themoviedb.org/t/p/w600_and_h900_bestv2/no_way_up_image.jpg", "https://media.themoviedb.org/t/p/w600_and_h900_bestv2/alien_romulus_image.jpg", 
        "https://media.themoviedb.org/t/p/w600_and_h900_bestv2/the_first_omen_image.jpg", "https://media.themoviedb.org/t/p/w600_and_h900_bestv2/dune_part_two_image.jpg", 
        "https://media.themoviedb.org/t/p/w600_and_h900_bestv2/atlas_image.jpg", "https://media.themoviedb.org/t/p/w600_and_h900_bestv2/chief_of_station_image.jpg", 
        "https://media.themoviedb.org/t/p/w600_and_h900_bestv2/arcadian_image.jpg", "https://media.themoviedb.org/t/p/w600_and_h900_bestv2/damsel_image.jpg", 
        "https://media.themoviedb.org/t/p/w600_and_h900_bestv2/the_crow_image.jpg", "https://media.themoviedb.org/t/p/w600_and_h900_bestv2/wanted_man_image.jpg", 
        "https://media.themoviedb.org/t/p/w600_and_h900_bestv2/spellbound_image.jpg", "https://media.themoviedb.org/t/p/w600_and_h900_bestv2/it_ends_with_us_image.jpg", 
        "https://media.themoviedb.org/t/p/w600_and_h900_bestv2/upgraded_image.jpg", "https://media.themoviedb.org/t/p/w600_and_h900_bestv2/a_family_affair_image.jpg", 
        "https://media.themoviedb.org/t/p/w600_and_h900_bestv2/joker_folie_a_deux_image.jpg", "https://media.themoviedb.org/t/p/w600_and_h900_bestv2/sleeping_dogs_image.jpg"
    ],
    'release_date': [
        '2023-12-25', '2024-05-03', '2024-06-14', '2024-02-16', '2019-08-22', '2024-05-24', '2024-11-22', '2024-09-13', 
        '2024-04-19', '2024-08-09', '2024-03-15', '2023-11-03', '2024-01-12', '2024-10-18', '2024-05-17', '2024-10-13', 
        '2024-04-11', '2024-07-26', '2024-11-08', '2024-02-09', '2024-06-28', '2024-12-20', '2024-10-04', '2024-07-12'
    ],

}