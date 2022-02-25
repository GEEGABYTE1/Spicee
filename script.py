from blockchain import Blockchain
import time

Spicee = Blockchain()


class Article:
    
    def running(self):
        while True:
            user_prompt = str(input(':'))
            user_prompt = user_prompt.strip(' ')
        

    def write_article(self):
        pass 

    def add_article_to_chain(self):
        pass 


    def print_chain(self):
        local_chain = Spicee.chain
        
        for block in local_chain:
            block.print_contents()
        


