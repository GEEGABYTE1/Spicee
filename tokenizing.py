from block import Block


class Publisher:


    def publisher_name(self):
        publishing_name = 'Spicee Publisher'
        return publishing_name

    def publisher_genre(self):
        genre = 'Test'
        return genre

    def owners(self):
        owners = {'Test': 'Me'}
        return owners

    def publishing_token(self):
        token = {'Name': self.publisher_name(), 'Genre': self.publisher_genre(), 'Owners/Creators': self.owners()}
        return token


test = Publisher()
token = test.publishing_token()
print('Token successfully Made: {}'.format(token))
transactions = [token]
token_block  = Block(transactions, token)



        

    
    





