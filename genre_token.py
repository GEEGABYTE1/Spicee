from block import Block

class Genre:
    
    def create_genre(self):
        name = ''
        publishers = [] 

        return name, publishers


genre = Genre()

created_genre = genre.create_genre()

print('Genre {} successfully made'.format(created_genre[0]))
transactions = [created_genre]
genre_block = Block(transactions, created_genre)

