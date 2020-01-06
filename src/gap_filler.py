import random
import spacy
import en_core_web_sm
from bs4 import BeautifulSoup
from urllib3 import PoolManager
import certifi

nlp = en_core_web_sm.load()


def gapfinder(txt, removal_proportion=7):
    
    doc = nlp(txt)
    
    low = []
    
    for token in doc:
        if token.tag_ == "CC":
            if random.randrange(1,100) <= removal_proportion:
                txt = txt.replace(token.text, "__________", 1)
                low.append(token.text)
        elif token.tag_ == "DT":
            if random.randrange(1,100) <= removal_proportion:
                txt = txt.replace(token.text, "__________", 1)
                low.append(token.text)
        elif token.tag_ == "EX":
            if random.randrange(1,100) <= removal_proportion:
                txt = txt.replace(token.text, "__________", 1)
                low.append(token.text)
        elif token.tag_ == "IN":
            if random.randrange(1,100) <= removal_proportion:
                txt = txt.replace(token.text, "__________", 1)
                low.append(token.text)
        elif token.tag_ == "MD":
            if random.randrange(1,100) <= removal_proportion:
                txt = txt.replace(token.text, "__________", 1)
                low.append(token.text)
        elif token.tag_ == "PDT":
            if random.randrange(1,100) <= removal_proportion:
                txt = txt.replace(token.text, "__________", 1)
                low.append(token.text)
        elif token.tag_ == "RP":
            if random.randrange(1,100) <= removal_proportion:
                txt = txt.replace(token.text, "__________", 1)
                low.append(token.text)
        elif token.tag_ == "TO":
            if random.randrange(1,100) <= removal_proportion:
                txt = txt.replace(token.text, "__________", 1)
                low.append(token.text)
        elif token.tag_ == "WDT":
            if random.randrange(1,100) <= removal_proportion:
                txt = txt.replace(token.text, "__________", 1)
                low.append(token.text)
        elif token.tag_ == "WP":
            if random.randrange(1,100) <= removal_proportion:
                txt = txt.replace(token.text, "__________", 1)
                low.append(token.text)
        elif token.tag_ == "WP$":
            if random.randrange(1,100) <= removal_proportion:
                txt = txt.replace(token.text, "__________", 1)
                low.append(token.text)
        elif token.tag_ == "WRB":
            if random.randrange(1,100) <= removal_proportion:
                txt = txt.replace(token.text, "__________", 1)
                low.append(token.text)
                    
    print("\nRead the below text and complete each gap with a word that fits.\n")
    
    print(txt)
    
    low.sort(key=str.lower)
    
        
        
    






 
def get_body(url):
    """
    This function gets the main body of a news page
   
    Input: url - URL (string) of the web site from which you want to get the HTML file
    Output: soup - HTML file of the web site specified in the URL input
    """
   
    # To make requests to multiple hosts taking care of maintaining the pools
    http = PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
 
    # Get get the HTML page of the URL
    response = http.request("GET", url)
 
    # Query the URL and pulling data out of HTML
    soup = BeautifulSoup(response.data,"lxml")
   
    if 'bbc.co.uk' in url:
        pass
    elif 'theguardian.com' in url:
       
        #get content of article (as html tag)
        article_content = soup.find(class_="content__article-body from-content-api js-article__body")
 
        # find the paragraph tags in the content element
        content_list = article_content.find_all('p')
       
        # get the text content
        text_list = [item.get_text() for item in content_list]
       
        output = ''.join(text_list)
       
       
    else:
        raise ValueError
   
    #body = soup.find('body')
    #the_contents_of_body_without_body_tags = body.findChildren()
 
    return output
 
 
 
def main():
    TEST_URL = 'https://www.bbc.co.uk/news/uk-50929543'
    TEST_URL_GUARDIAN = 'https://www.theguardian.com/uk-news/2019/dec/28/government-exposes-addresses-of-new-year-honours-recipients'
     
    text_output = get_body(TEST_URL_GUARDIAN)
    
    gapfinder(text_output)
    
    print('\nThis news article can be found via the below link:\n\n' , TEST_URL_GUARDIAN)
    
    
    
if __name__ == "__main__":
    main()
