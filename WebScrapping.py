import requests
from bs4 import BeautifulSoup
import pandas
import argparse
import connect

parser = argparse.ArgumentParser()
parser.add_argument("--page_num_max", help="Enter the no of pages to parse : ", type=int)
parser.add_argument("--dbname",help="Enter name of db : ",type=str)
args = parser.parse_args()

oyo_url = "https://www.oyorooms.com/hotels-in-bangalore//?page="
page_num_MAX=3

for page_num in range(1,page_num_MAX):
    url=oyo_url+str(page_num)
    print("Get request for : "+url)
    req=requests.get(url)
    content=req.content

    print(content)

    soup = BeautifulSoup(content,"html.parser")
    all_hotels = soup.find_all("div", {"class": "hotelcardlisting"})
    scrapped_info_list=[]

    for hotel in all_hotels:
        hotel_dict = {}
        hotel_dict["name"] = hotel.find("h3", {"class": "listingHotelDescription__HotelName"}).text
        hotel_dict["Address"] = hotel.find("span", {"itemprop": "StreetAddress"}).text
        hotel_dict["Price"] = hotel.find("span", {"class": "ListingPrice__FinalPrice"}).text
        try:
            hotel_dict["rating"] = hotel.find("span", {"class": "hotelRating__ratingSummary"}).text
        except AttributeError:
            pass
        
        parent_amenities_element=hotel.find("div", {"class": "amenityWrapper"})
        
        amenities_list = []
        for amenity in parent_amenities_element.find_all("div", {"class": "amenityWrapper__amenity"}):
            amenities_list.append(amenity.find("span", {"class":"d-body-sm"}).text.strip())
                
        hotel_dict["amenities"] = ', '.join(amenities_list[:-1])
        
        scrapped_info_list.append(hotel_dict)
        
        #print(hotel_name, hotel_address, hotel_price, hotel_rating)

dataFrame = pandas.DataFrame(scrapped_info_list)
print("Creating csv file...")
dataFrame.to_csv("oyo.csv")
connect.get_hotel_info(args.dbname)