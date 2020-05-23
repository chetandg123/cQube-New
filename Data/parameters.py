import base64
import os


class Data():

    def get_driver_path(self):
        os.chdir('../')
        executable_path = os.path.join(os.getcwd(), 'Driver/chromedriver')
        return executable_path

    def get_system_path(self):
        os.chdir('../')
        pwd = os.getcwd()
        return pwd

    def get_report_path(self):
        os.chdir('../')
        os.getcwd()
        report_path = os.path.join(os.getcwd(), 'cQube/Reports/report.html')
        return report_path


    url = base64.b64decode("aHR0cHM6Ly9jcXViZS50aWJpbHByb2plY3RzLmNvbQ==").decode("utf-8")
    username = base64.b64decode("dGliaWxzb2x1dGlvbnNAY3F1YmUuY29t").decode("utf-8")
    password = base64.b64decode("dGliaWwxMjM=").decode("utf-8")

    email = "//input[@id='exampleInputEmail']"
    pwd = "//input[@id='exampleInputPassword']"
    loginbtn = "//button[@type='submit']"

    Blocks = "//button[@class='btn btn-secondary']/b[contains(text(),'Blocks')]"
    Clusters = "//button[@class='btn btn-secondary']/b[contains(text(),'Clusters')]"
    Schools = "//button[@class='btn btn-secondary']/b[contains(text(),'Schools')]"

    dots = "leaflet-interactive"

    hyper_link = "//p/span"
    directory = "//p[contains(text(),' Semester report for:')]/span"
    Download = "//img[@title='Download Report']"

    # Dash board
    Dashboard = "//span[@class='" \
                "mat-button-wrapper']/mat-icon"
    login_in = "//span[@class='span']"
    SAR = "//div[@class='mat-list-item-content']/td[contains(text(),'Student')]"
    Log_out = "//button/span[contains(text(),'Log Out')]"
    Home_icon = "//img[@id='home']"

    select_district = 'myDistrict'
    select_blocks = 'myBlock'
    select_clusters = 'myCluster'
    select_month = 'month'
    select_year = 'year'

    No_schools = '/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-map-view/div/div[4]/div[2]'