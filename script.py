
from lib2to3.pgen2 import token
from tkinter import E
from blockchain import Blockchain
import time
from datetime import datetime
from termcolor import colored
import webbrowser
from tokenizing import token_block      # Publishing Token Integration
from genre_token import genre_block

Spicee = Blockchain()

def add_token():
    genesis_block = Spicee.chain[0]
    rest_of_chain = Spicee.chain[1:]
    token_block.generate_hash()
    Spicee.chain.append(token_block)
    print(token_block.generate_hash())
    print(Spicee.chain)


genres = []

def add_genre():
    genesis_block = Spicee.chain[0]
    rest_of_chain = Spicee.chain[1:]
    genre_block.generate_hash() 
    Spicee.chain.append(genre_block)
    print(genre_block.generate_hash())
    print(Spicee.chain)
    
        


    

class Article:

    article_done = {}

    
    def running(self):
        while True:
            user_prompt = str(input(':'))
            user_prompt = user_prompt.strip(' ')
            if user_prompt == '/write_article':
                self.write_article()
            elif user_prompt == '/fetch_article':
                self.fetch_article()
            elif user_prompt == '/view_chain':
                self.print_chain()
            elif user_prompt == '/add_web':
                self.add_web_article()
            elif user_prompt == '/view_publishers':
                self.view_publishers()
            elif user_prompt == '/view_articles':
                self.view_articles()
            
    def view_articles(self):
        for block in Spicee.chain:
            if len(block.transactions) == 0:
                continue
            else:
                if block.hash == genre_block.generate_hash():
                    genres = block.transactions
                    for genre in genres:
                        genre_name = genre[0]
                        genre_publisher = genre[-1]

                




    def write_article(self):
        current_date = datetime.now()
        now_date = current_date.strftime("%m/%d/%Y, %H:%M:%S")
        initial_intro = colored('Date Created: ', 'cyan')
        print(colored('-'*24))
        print('{}: {}'.format(initial_intro, now_date))
        print('\n')
        string = str(input('''-> '''))
        time.sleep(0.5)
        print('\n')
        saved = colored("Saved... ", 'blue')
        date = current_date.strftime("%m/%d/%Y, %H:%M:%S")
        print('\n')
        time.sleep(0.5)
        
        name_of_file = colored('name of file: ', 'cyan')
        name = str(input(name_of_file))
        print('-'*24)
        self.article_done[name] = string

        result = self.add_article_to_chain()
        if result == True:
            print('{} has been added to the chain'.format(name))
            Spicee.print_blocks()
        else:
            print(colored("There was an error adding the article to the chain", 'red'))

    def add_web_article(self):
        name_of_file = colored('name of file: ', 'cyan')
        name = str(input(name_of_file))
        website = colored(input('website of article: '))
        
        publisher_input = str(input('Would you like to submit your article to a publishing company?: '))
        if publisher_input == 'y':
            desired_publisher_token = self.fetch_token()
            desired_publisher_token_hash = desired_publisher_token.hash
            transaction = {'name': name, 'publisher': desired_publisher_token_hash, 'website': website, 'amount': '0.000000001' }
            Spicee.add_block(transaction)
        else:
            transaction = {'name': name, 'website': website, 'amount': '0.000000001'}
            Spicee.add_block(transaction)
        print(colored('{} has been added to the chain'.format(name), 'green'))
        Spicee.print_blocks()

    def add_article_to_chain(self):
        name = None 
        article = None 
        for key, value in self.article_done.items():
            name = key 
            article = value 
        
        publisher_input = str(input('Would you like to submit your article to a publishing company?: '))
        if publisher_input == 'y':
            desired_publisher_token = self.fetch_token()
            desired_publisher_token_hash = desired_publisher_token.hash
            transaction = {'name': name, 'article': [article], 'publisher': desired_publisher_token_hash, 'amount':'0.000000001'}
            Spicee.add_block(transaction)
        else:
            transaction = {'name': name, 'article': [article], 'amount':'0.000000001'}
            try:
                Spicee.add_block(transaction)
                return True
            except:
                return False


    def print_chain(self):
        local_chain = Spicee.chain
        
        if len(local_chain) == 1:
            print(colored("There are no articles on the chain"), 'red')
        else:
            for block in local_chain:
                block.print_contents()
                print('\n')

    def fetch_token(self):
        token_hash = str(input('Please type in the publisher hash: '))
        if len(token_hash) != 64:
            print("The hash is smaller than 64 characters")
        else:
            self.view_pulishers()
            user_publisher = str(input("Desired publisher Name: "))
            user_publisher = user_publisher.strip(' ')
            if user_publisher == 'n/a':
                return 
            else:
                for block in Spicee.chain:
                    if len(block.transactions) == 0:
                        pass 
                    else:
                        if block.hash == token_block.generate_hash():
                            transactions = block.transactions
                            for publisher in transactions:
                                if publisher['Name'] == user_publisher:
                                    return block
    
    def view_publishers(seflf):
        for block in Spicee.chain:
                if len(block.transactions) == 0:
                    pass 
                else:
                    if block.hash == token_block.generate_hash():
                        transactions = block.transactions
                        print('\n')
                        print("Here are the current publishers: ")
                        for publisher in transactions:
                            print('-'*24)
                            publisher_name = publisher['Name']
                            publisher_genre = publisher['Genre']
                            publisher_owner = publisher['Owners/Creators']
                            print(publisher_name)
                            print(publisher_genre)
                            print(publisher_owner)
                        print('\n')

                                
    def fetch_article(self):
        user_hash = str(input('Search by block Hash: '))
        result = False
        if len(user_hash) != 64:
            print("The Hash inputted does not seem to match the 64-bit format.")
        else:
            for block in Spicee.chain:
                if len(block.transactions) == 0:
                    pass
                else:
                    data = block.transactions
                    block_hash = block.hash
                    if block_hash == user_hash:
                        print(data)
                        name = data['name']
                        try:
                            article = data['article']
                            publisher = data.get('publisher', None)
                            if publisher == None:
                                pass 
                            else:
                                print('Publisher: {}'.format(publisher))
                            print('Name: {}'.format(name))
                            print('\n')
                            print(article)
                            result = True
                        except KeyError:
                            website = data['website']
                            webbrowser.open(website, new=1, autoraise=True)

                    else:
                        continue
                
            if result == False:
                print("Article not found")
        
        
test = Article()
add_token()
add_genre()
print(test.view_articles())

