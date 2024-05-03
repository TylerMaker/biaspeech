# --------------------------
# Models folder
# Class definition
#
# Youtube : define the Youtube (Block) model
# --------------------------

""" imports: logging and config """
import logging
import logging.config
from utils.config import Config
import webbrowser

""" objects:  """
conf = Config()  # config
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=conf.LOGLEVEL)

""" MVC """
from models.blocks import block


class Youtube(block.Block):
    
    """ constructor """
    def __init__(self, prompt, ai): 
        block.Block.__init__(self, prompt, ai)
        
    """ get_output """        
    def get_output(self): 
        return(conf.OUTPUT_WEB)
 
    """ get_file """        
    def get_file(self):
        pass
       
    """ run """        
    def run(self, file):
        self.logger.info("run w Youtube")  # inform the user      
        
        search = self.prompt.mia.input.replace("youtube ", "")  # build the url
        url = conf.YOUTUBE  # build the url
        
        if search != "":  # build the url
            url = url + "results?search_query=" + search
        
        webbrowser.open(url)  # open-up the url
     
