from datetime import datetime
import csv
from bs4 import BeautifulSoup
import os

class PropertyData():
    html_content_str = ''
    html_soup = None
    parcel_id=''
    property_appraiser_url=''
    owner_mailing_address=''
    owner_mailing_address_g_map=''
    site_address=''
    site_address_g_map=''
    owner_home=''
    owner_count=''
    owner_1=''
    owner_2=''
    owner_3=''
    gis_map=''
    tax_collector_url=''
    homestead=''
    just_market_value=''
    county_assessed_value=''
    building_value=''
    land_value=''
    land_agricultural_value=''
    agricultural_market_value=''
    improve_value=''
    property_use=''
    parcel_id=''
    no_of_building=''
    zoning=''
    acreage=''
    improve_type=''
    building_type=''
    no_of_stories=''
    heated_area=''
    year_built=''
    bed=''
    bath=''
    air_cond=''
    exterior_wall=''
    subdivision=''
    historic_district=''
    last_sale_date=''
    sale_price=''
    deed=''

    def __init__(self, html_content:str) -> 'PropertyData':
        self.html_content_str = html_content
        self.html_soup = BeautifulSoup(html_content, 'html.parser')

        self.parse_interim_parcel_details_card()
        self.parse_btn_bar()


    def parse_btn_bar(self):
        bar = self.html_soup.find(class_='form-row actions-row')
        self.tax_collector_url = bar.find(id='btnPrintTaxBill')['href']
        self.gis_map = bar.find(id='btnPublicGIS')['href']
    
    def parse_interim_parcel_details_card(self):

        card = self.html_soup.find(class_='card-body p-2')
        col_values = card.find_all(class_='col-8')

        self.parcel_id = col_values[0].text

        owners = card.find_all(class_='parcel_owner')
        owners = [owner.string for owner in owners]
        while len(owners) < 3:
            owners.append('')

        self.owner_1 = owners[0]
        self.owner_2 = owners[1]
        self.owner_3 = owners[2]

        self.site_address = card.find(class_='parcel-911-address').text.replace('\n',' ')
        self.owner_mailing_address = col_values[5].text.replace('\n',' ')
        self.subdivision = col_values[6].text

    def log_csv(self):
        data_dict = self.to_dict()

        curr_t = datetime.now()
        curr_t = curr_t.strftime("%Y-%m-%d-%H-%M-%S")
        filename = f'property_page.csv'
        path = "tutorial/logged_csvs"
        fullpath = os.path.join(path, filename)

        with open(fullpath, 'w') as file:
            w = csv.DictWriter(file,data_dict.keys())
            w.writeheader()
            w.writerow(data_dict)

    def to_dict(self):

        all_data = vars(self)
        del all_data['html_content_str']
        del all_data['html_soup']

        return all_data