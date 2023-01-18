import os
from justrpa.browser import TaskBrowser

class BestSellerBrowser(TaskBrowser):
    def zoom_in(self, ratio=1):
        js = f"document.body.style.zoom = '{ratio}'"
        self.driver.execute_script(js)

    def screenshot_bestseller_page(self, params:dict):
        url = self.get_url(params["site"], params["Category"])
        self.go_to(url)
        self.sleep_medium()
        self.zoom_in(0.5)
        self.sleep_short()
        filename = self.build_screenshot_filename(**params)
        self.screenshot_to_dest(filename, full_page=True)
        self.zoom_in(1)
        return filename

    def build_screenshot_filename(self, **kwargs):
        template = "{account_trim}/亚马逊/{site_short}/16.亚马逊Best Seller截图/每日截图/{today}/{Category}_{today}.jpg"
        filename = self.build_filename(template, **kwargs)
        return os.path.join(os.getcwd(), self.target_dir, filename)

    @TaskBrowser.error_handler
    def before_run_reports(self, report_params:dict):
        return self.generate_all_params()
    
    @TaskBrowser.error_handler
    def go_to_site(self, site):
        self.logger.info("go to site: do nothing.")
    
    def get_url(self, site, category):
        url_map = {
            "United States":{
                "Generators & Portable Power":"https://www.amazon.com/Best-Sellers-Garden-Outdoor-Generators-Portable-Power/zgbs/lawn-garden/552808/ref=zg_bs_unv_lg_2_348967011_1",
                "Generators & Portable Power—Generators":"https://www.amazon.com/Best-Sellers-Patio-Lawn-Garden-Generators/zgbs/lawn-garden/348967011/ref=zg_bs_nav_lawn-garden_2_552808",
                "Generators & Portable Power—Solar & Wind Power":"https://www.amazon.com/Best-Sellers-Patio-Lawn-Garden-Solar-Wind-Power/zgbs/lawn-garden/3236381/ref=zg_bs_nav_lawn-garden_2_348967011"
            },
            "Canada":{
                "Generators & Portable Power":"https://www.amazon.ca/Best-Sellers-Patio-Lawn-Garden-Outdoor-Generators-Portable-Power/zgbs/lawn-garden/6257186011/ref=zg_bs_unv_lg_2_6257187011_1",
                "Generators & Portable Power—Generators":"https://www.amazon.ca/gp/bestsellers/lawn-garden/6257187011/ref=pd_zg_hrsr_lawn-garden",
                "Generators & Portable Power—Solar & Wind Power":"https://www.amazon.ca/Best-Sellers-Patio-Lawn-Garden-Solar-Wind-Power/zgbs/lawn-garden/6257194011/ref=zg_bs_nav_lg_3_6257186011"
            },
            "United Kingdom":{
                "Outdoors":"https://www.amazon.co.uk/gp/bestsellers/outdoors/4370158031/ref=pd_zg_hrsr_outdoors"
            },
            "Germany":{
                "Garden":"https://www.amazon.de/gp/bestsellers/garden/120613031/ref=pd_zg_hrsr_garden"
            }
        }
        return url_map[site][category]
    
    def generate_all_params(self):
        params = {
            "United States":[
                {"Category":"Generators & Portable Power"},
                {"Category":"Generators & Portable Power—Generators"},
                {"Category":"Generators & Portable Power—Solar & Wind Power"}
            ],
            "Canada":[
                {"Category":"Generators & Portable Power"},
                {"Category":"Generators & Portable Power—Generators"},
                {"Category":"Generators & Portable Power—Solar & Wind Power"}
            ],
            "United Kingdom":[{"Category":"Outdoors"}],
            "Germany":[{"Category":"Garden"}]
        }
        return params

def test_bestseller_screenshot():
    from core.utils.config import load_merge_conf
    env = load_merge_conf("env.json")
    browser = BestSellerBrowser()
    browser.init(env)
    browser.home_url = "https://www.amazon.com/"
    browser.prepare_browser(browser.home_url)
    params = {
        "site":"United States",
        "Category":"Generators & Portable Power"
    }
    # browser.screenshot_bestseller_page(params)
    browser.run_bestseller_screenshots(params)
    browser.cleanup()

if __name__ == "__main__":
    test_bestseller_screenshot()


