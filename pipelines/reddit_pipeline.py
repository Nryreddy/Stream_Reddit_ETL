from utils.constants import CLIENT_ID,SECRET



def reddit_pipeline(file_name:str , subreddit:str,time_filter='day',limit=None):

    #connection to reddit instance
    instance = connect_reddit(CLIENT_ID, SECRET,'Airscholar Agent')


    #extraction

    
    # transformarion

    #loading to csv