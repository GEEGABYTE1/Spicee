from platformdirs import user_runtime_dir
from blockchain import Blockchain
import time
from datetime import datetime
from termcolor import colored


Spicee = Blockchain()


### EDIT ARTICLES BY REFERENCING THE CHAIN #### 

class Article:

    article_done = {}

    
    def running(self):
        while True:
            user_prompt = str(input(':'))
            user_prompt = user_prompt.strip(' ')
            if user_prompt == '/write_article':
                self.write_article()
        

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
        


    def add_article_to_chain(self):
        name = None 
        article = None 
        for key, value in self.article_done.items():
            name = key 
            article = value 
        
        transaction = {'name': name, 'article_name': article}
        try:
            Spicee.add_block(transaction)
            return True
        except:
            return False


    def print_chain(self):
        local_chain = Spicee.chain
        
        for block in local_chain:
            block.print_contents()
        

test = Article()
print(test.running())

