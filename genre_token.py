from block import Block

class Genre:
    
    def create_genre(self):
        name = 'History'
        publishers = ['Test'] 

        return {'Name': name, 'Publisher':publishers}


genre = Genre()

created_genre = genre.create_genre()

print('Genre {} successfully made'.format(created_genre['Name']))
transactions = [created_genre]
genre_block = Block(transactions, created_genre)

