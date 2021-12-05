def v():
    with open('dane/movies.csv', newline='', encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        next(spamreader)
        for i, row in enumerate(spamreader):
            movie = Movies(row[0], row[1], row[2])
            movies_list.append(movie.__dict__)