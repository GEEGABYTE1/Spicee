from blockchain import Blockchain
import time
from datetime import datetime
from termcolor import colored

Spicee = Blockchain()


class Article:
    
    def running(self):
        while True:
            user_prompt = str(input(':'))
            user_prompt = user_prompt.strip(' ')
        

    def write_article(self):
        current_date = datetime.now()
        now_date = current_date.strftime("%m/%d/%Y, %H:%M:%S")
        initial_intro = colored('Date Created: ', 'cyan')
        print(colored('-'*24))
        print('{}: {}'.format(initial_intro, now_date))
        print('\n')
        string = str(input('''-> '''))
        print(string)
        time.sleep(0.5)

        
        

    def add_article_to_chain(self):
        pass 


    def print_chain(self):
        local_chain = Spicee.chain
        
        for block in local_chain:
            block.print_contents()
        

test = Article()
print(test.write_article())

