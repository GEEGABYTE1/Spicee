

class Publisher:


    def publisher_name(self):
        publishing_name = 'Spicee Publisher'
        return publishing_name

    def publisher_genre(self):
        genre = ''
        return genre

    def owners(self):
        owners = {}
        return owners

    def publishing_token(self):
        token = {'Name': self.publisher_name(), 'Genre': self.publisher_genre(), 'Owners/Creators': self.owners()}
        return token

genres = []
publishers = []
while True:
    user_input = str(':')
    if user_input == '/stop':
        break 
    else:
        test = Publisher()
        token = test.publishing_token()

        token_genre = token['Genre']
        publishers = token['Owners/Creators']
        genres.append(token_genre)
        publishers.append(token_genre)

    
    





