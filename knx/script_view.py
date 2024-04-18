import time
import requests
import datetime
from Scraper_Project.utils import send_message,send_message_error
from knx.utils import start_new_thread, COUNTRIES
from django.shortcuts import redirect
from knx.models import CompaniesData, UrlCount
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow 
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from selenium.webdriver.common.by import By
from knx.utils import configure_webdriver
from django.utils import timezone
import os

def uploadRaw(companies):
    start_time = datetime.datetime.now()
    all_data = [
                [
                    record[0],
                   record[1],
                    record[2],
                    record[3],
            record[4],
            record[5],
                    record[6],
record[7],
                record[8],
            record[9],
            record[10],
                    record[11],
                    record[12],
                   record[13],
                    record[14],
                    record[15],
                    record[16],
                    record[17],
                    record[18],
                    record[19],
                    record[20],
                    record[21],
                    record[22],
                    record[23],
                    record[24],
                    record[25],
                    record[26],
                    record[27],
                    record[28],
                   record[29],
                    record[30],
                    record[31],
                    record[32],
                   record[33],
                    record[34],
                    record[35],
                   record[36],
                    record[37],
                   COUNTRIES.get(record[29], "N/A"),
                   start_time.strftime("%Y-%m-%d")]
                 for record in companies
            ]
     
    append_values(
                    "1VUQzWZz4c3b8wmBF6TncIafBKnJ-TjmEZvyczlEa7hY",
                    "Sheet1",
                    "USER_ENTERED",
                    all_data,
                )
    

def append_values(spreadsheet_id, range_name, value_input_option, values):
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
    credentials = None
    if os.path.exists("knx/token.json"):
        credentials = Credentials.from_authorized_user_file("knx/token.json", SCOPES)

    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("knx/credentials.json", SCOPES)
            credentials = flow.run_local_server(port=0)
            with open("knx/token.json", "w") as token:
                token.write(credentials.to_json())
    # pylint: disable=maybe-no-member
    try:
        service = build("sheets", "v4", credentials=credentials)

        body = {"values": values}
        result = (
            service.spreadsheets()
            .values()
            .append(
                spreadsheetId=spreadsheet_id,
                range=range_name,
                valueInputOption=value_input_option,
                body=body,
            )
            .execute()
        )
        print(f"{result.get('updates').get('updatedCells')} cells appended.")
        return result
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error

def start_script():
    try:
        cookies = {
            'Cookie-Navigator--enabled': 'accepted',
            'Cookie-Navigator--Google-Analytics--disable': 'false',
            'Cookie-Navigator--Facebook-Pixel--disable': 'false',
            'Cookie-Navigator--Hotjar--disable': 'false',
            'Cookie-Navigator--YouTube--Wall': 'false',
            'Cookie-Navigator--Google-Maps--Wall': 'false',
            '_gcl_au': '1.1.534571940.1708362628',
            '_fbp': 'fb.1.1708362629210.1560213889',
            '_hjSessionUser_346379': 'eyJpZCI6ImY4ZjNkNTQzLTNjZTAtNTE4OS05MWU0LTA5Mjg5N2I2MTQ5OCIsImNyZWF0ZWQiOjE3MDgzNjI2MjkxNDksImV4aXN0aW5nIjp0cnVlfQ==',
            '_gid': 'GA1.2.2052715013.1709735112',
            'WSESSIONID': 'mout38393q9rfbromjql0v0o9a',
            '_hjSession_346379': 'eyJpZCI6Ijg1N2E2YTIxLTQwMjYtNDk4Zi1hN2I3LTQ4MjgxNjg4ODI3YSIsImMiOjE3MDk3NTM3MzcwNDYsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=',
            '_gat_UA-5200821-3': '1',
            '_gat_UA-5200821-1': '1',
            '_ga_MP426EDT14': 'GS1.1.1709753737.3.1.1709753782.15.0.0',
            '_ga_G92MED9JS9': 'GS1.1.1709753737.3.1.1709753782.15.0.0',
            '_ga_NKNYYNG0S3': 'GS1.1.1709753737.3.1.1709753783.0.0.0',
            '_ga': 'GA1.2.1557507222.1708362629',
        }

        headers = {
            'authority': 'www.knx.org',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-US,en;q=0.9',
            # 'cookie': 'Cookie-Navigator--enabled=accepted; Cookie-Navigator--Google-Analytics--disable=false; Cookie-Navigator--Facebook-Pixel--disable=false; Cookie-Navigator--Hotjar--disable=false; Cookie-Navigator--YouTube--Wall=false; Cookie-Navigator--Google-Maps--Wall=false; _gcl_au=1.1.534571940.1708362628; _fbp=fb.1.1708362629210.1560213889; _hjSessionUser_346379=eyJpZCI6ImY4ZjNkNTQzLTNjZTAtNTE4OS05MWU0LTA5Mjg5N2I2MTQ5OCIsImNyZWF0ZWQiOjE3MDgzNjI2MjkxNDksImV4aXN0aW5nIjp0cnVlfQ==; _gid=GA1.2.2052715013.1709735112; WSESSIONID=mout38393q9rfbromjql0v0o9a; _hjSession_346379=eyJpZCI6Ijg1N2E2YTIxLTQwMjYtNDk4Zi1hN2I3LTQ4MjgxNjg4ODI3YSIsImMiOjE3MDk3NTM3MzcwNDYsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; _gat_UA-5200821-3=1; _gat_UA-5200821-1=1; _ga_MP426EDT14=GS1.1.1709753737.3.1.1709753782.15.0.0; _ga_G92MED9JS9=GS1.1.1709753737.3.1.1709753782.15.0.0; _ga_NKNYYNG0S3=GS1.1.1709753737.3.1.1709753783.0.0.0; _ga=GA1.2.1557507222.1708362629',
            'referer': 'https://www.knx.org/knx-en/for-professionals/community/partners/index.php?country=',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        params = {
            "type": "json",
            "country": "",
            "per_page": "20",
            "qualification": "total",
        }
        response = requests.get(
            'https://www.knx.org/knx-en/for-professionals/community/partners/index.php',
            params=params,
            cookies=cookies,
            headers=headers,
            )
        json_response = response.json() 
        total_count = int(json_response['total']) 
        total_comp_count = UrlCount.objects.all().first().count
        if total_count <= total_comp_count*20:
            a =  UrlCount.objects.all().first()
            a.count = 0
            a.save()
            total_comp_count = 0
            
        total_loop = int(total_count/20)
        total_loop += 2
        increment_count = total_comp_count
        real_records = []
        for x in range(total_loop):
            # c = UrlCount.objects.all().first()
            start_time = timezone.now()
            increment_count += 20
            print(increment_count)
            a =  UrlCount.objects.all().first()
            a.count = increment_count
            a.save()
            params["per_page"] = increment_count
            response = requests.get(
            'https://www.knx.org/knx-en/for-professionals/community/partners/index.php',
            params=params,
            cookies=cookies,
            headers=headers,
            )
            json_response = response.json() 
            for record in json_response["rows"]:  
                real_records.append(list(record.values()))
                
            uploadRaw(real_records)    
            user_profiles = [
                CompaniesData(
                    uid=record[0],
                    id=record[1],
                    salutation_id=record[2],
                    stars=record[3],
                    stars_feedback=record[4],
                    stars_projects=record[5],
                    stars_engagement=record[6],
                    stars_tools=record[7],
                    stars_knowledge=record[8],
                    score_feedback=record[9],
                    score_projects=record[10],
                    score_engagement=record[11],
                    score_tools=record[12],
                    score_knowledge=record[13],
                    score=record[14],
                    visible=record[15],
                    visible_list=record[16],
                    visible_map=record[17],
                    national_group_visible=record[18],
                    username=record[19],
                    firstname=record[20],
                    lastname=record[21],
                    company=record[22],
                    phone=record[23],
                    mobile=record[24],
                    street=record[25],
                    housenumber=record[26],
                    zipcode=record[27],
                    city=record[28],
                    country_id=record[29],
                    vat=record[30],
                    email=record[31],
                    website=record[32],
                    language=record[33],
                    longitude=record[34],
                    latitude=record[35],
                    communication_journal=record[36],
                    communication_journal_language_id=record[37],
                    country_name=COUNTRIES.get(record[29], "N/A")
                ) for record in real_records
            ]
            CompaniesData.objects.bulk_create(user_profiles, ignore_conflicts=True, batch_size=500)
            time.sleep(5)
            end_time = timezone.now()
            real_records = []
            newly_objects = CompaniesData.objects.filter(created_at__range=(start_time, end_time))
            if len(newly_objects) > 0:
                start_time = datetime.datetime.now()
                new_entries = [
                    [
                        x.uid,
                        x.id,
                        x.salutation_id,
                        x.stars,
                        x.stars_feedback,
                        x.stars_projects,
                        x.stars_engagement,
                        x.stars_tools,
                        x.stars_knowledge,
                        x.score_feedback,
                        x.score_projects,
                        x.score_engagement,
                        x.score_tools,
                        x.score_knowledge,
                        x.score,
                        x.visible,
                        x.visible_list,
                        x.visible_map,
                        x.national_group_visible,
                        x.username,
                        x.firstname,
                        x.lastname,
                        x.company,
                        "'" + x.phone if x.phone != "N/A" else x.phone,
                        "'" + x.mobile if x.mobile != "N/A" else x.mobile,
                        x.street,
                        x.housenumber,
                        x.zipcode,
                        x.city,
                        x.country_name,
                        x.vat,
                        x.email,
                        x.website,
                        x.language,
                        x.longitude,
                        x.latitude,
                        x.communication_journal,
                        x.communication_journal_language_id,
                        x.country_id,
                        start_time.strftime("%Y-%m-%d"),
                    ] for x in newly_objects
                ]
                print("sending message on slack")
                send_message(new_entries,"#knx-partners-updates")
                
                append_values(
                    "1OOSyu6IPaUJt9Y8SQZgLIVXIfnZChGoN8S1P24dTk8Q",
                    "Sheet1",
                    "USER_ENTERED",
                    new_entries,
                )
            send_message_error(f'On Page number: {increment_count}')
    except Exception as e:
        send_message_error(f'Error Occured: {e}')
        print(e)

def accept_cookie(driver):
    try:
        btns = driver.find_element(By.CLASS_NAME, "cookieButtons")
        btns.find_elements(By.TAG_NAME, "button")[1].click()
        time.sleep(2)
    except:
        pass

def check_count():
    try:
        driver = configure_webdriver()
        scraper = UrlCount.objects.filter()
        if not scraper.exists():
            scraper.create(count=0)
        link = "https://www.knx.org/knx-en/for-professionals/community/partners/index.php"
        driver.get(link)
        time.sleep(1)
        accept_cookie(driver)
        time.sleep(1)
        list_count = driver.find_element(By.CLASS_NAME, "total-selected").find_element(By.TAG_NAME, "b").text
        if UrlCount.objects.filter(count=list_count, url=link).exists():
            return False
        UrlCount.objects.all().update(count=list_count, url=link)
        return True
    except Exception as e:
        print(e)
        return False

@start_new_thread        
def run_fun_in_loop():
    try:
        print("yes called successfully")
        a = UrlCount.objects.all()
        if a :
            a =  UrlCount.objects.all().first()
            Sum = a.count
            if Sum >= 20:
                a.count = Sum - 20
                a.save()
        else:
            UrlCount.objects.create(count=0)
        while(1):
            # if check_count():
                start_script()
                send_message_error(f'Cycle completed successfully the system will be resumed soon')
                time.sleep(20)
    except Exception as e:
        print(e)
        
def scrape(request):
    run_fun_in_loop()
    print("Function called in a seperate thread")
    return redirect('index')


run_fun_in_loop()
