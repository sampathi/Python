from urllib.request import urlopen
from urllib.error import HTTPError
import requests
import lxml
from bs4 import BeautifulSoup
import smtplib
import pandas as pd



#********************************************************************************************************************************
#********************************************************************************************************************************
#*Steps to follow:																											   *
#*"""1) Install the imported modules first using pip install <module name>	"""										   		   *
#*"""2) Use only amazon to get the product url. Copy url and paste it when prompted """										   *
#*"""3) Go to this Url <https://www.whatismybrowser.com/detect/what-is-my-user-agent> and find your browser user agent, 		   *
#*	copy it and use while prompted """																						   *
#*"""4) A file will be created in the same directory in which the preice will be updated. So check if price is added or not"""  *
#*																															   *
#*****************PLEASE CHANGE THE CODE IF REQUIRED AND ADD YOUR FUNCTIONALITIES************************************************
#********************************************************************************************************************************




#Web Scraper Function

def getPrice(url, user_agent):
    try:
        page_url = url
        browser_agent = {"Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"}
        browser_agent["User-Agent"] = user_agent
        response = requests.get(link, headers=browser_agent)
    except HTTPError as e:
        return None
    try:
        soup = BeautifulSoup(response.content, "lxml")
        price = soup.find(id="priceblock_ourprice").get_text()[1:-3]
        price = int(price.replace(',', ''))
    except AttributeError as e:
        return None
    return price


 # File output Function

def priceFile():
    try:
        file_path = r'sample_text.txt'
        with open(file_path,'a') as sample:
            sample.write(str(getPrice(link, user_agent)) + ',')
    except:
        return str('Error occured')


# Visualization Function

def pricePlots():
    
	try:
	    data = pd.read_csv(r'C:\Users\sampathi\Python_Jupyter_Practice\Python_Projects\sample_text.txt',header=None)
	    data = data.T
	    data.columns = ['Product Prices']
	    plt.figure(figsize=(10,6))
	    plt.plot(data)
	except :
		return str('Error occured')

# Mail Alert Function

def priceAlert():
    req_price = 40000 # required price

    sender_mail = input('Enter sender Mail Id: ')
    pwd = input('Enter Password: ')
    receiver_mail = input('Enter receiver Mail Id: ')
    
    try:
        if final_price >= req_price:
            message = f"is now available at {final_price}"

            with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
                connection.starttls()
                result = connection.login(sender_mail, pwd)
                connection.sendmail(
                from_addr= sender_mail,
                to_addrs= receiver_mail,
                msg=f"Subject:Amazon Price Alert!\n\n{message}"
                )
        print('Mail sent successfully')
    except:
        return str('Error occured')



# https://www.amazon.com/gp/product/B08723GJ2T?pf_rd_r=04QW71TQXP55RS4XX9A5&pf_rd_p=6fc81c8c-2a38-41c6-a68a-f78c79e7253f

# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36



# main function

if __name__ == "__main__":

	link = input('Enter URL: ')
	user_agent = input('Enter your brower user agent: ')

	final_price = getPrice(link,user_agent)

	if final_price == None:
	    print('Price could not be Found')
	else:
	    priceFile() # Updating the file with price value


	priceAlert()

	pricePlots()  # plot the prices 




