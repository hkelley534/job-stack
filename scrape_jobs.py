from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import os


def create_scraping_url(role, location):
    """
    Creates a URL for scraping jobs from www.talent.com
    - uses f strings to format the url
    """

    url = f"https://www.talent.com/jobs?k={role}&l={location}"
    return url


def create_chromedriver_path():
    """
    Creates the file path for the chromedriver
    - assume this exists in the chromedriver subdirectory
    - use os.path.join to create the path
    - use the `selenium_starter.py` file from last assignment as a guide
    """
    cwd = os.getcwd()
    chromedriver_path = os.path.join(cwd, 'chromedriver/chromedriver')
    return chromedriver_path

def scrape_jobs(chromedriver_path, url):
    """
    Scrapes the jobs from the given url
    - uses selenium to scrape the jobs
    - parses the jobs into a list of dictionaries
    - returns the list of dictionaries
    """

    # start the driver and grab the url
    driver = wd.Chrome(chromedriver_path)
    driver.get(url)

    # create a list to hold dictionaries of the jobs
    jobs = []

    # grab the all of the div tag contents where class = "link-job-wrap"
    job_elements = driver.find_elements(By.CLASS_NAME, "link-job-wrap")

    # loop through the job elements
    for job_element in job_elements:
        job = {}  # dictionary to hold the job data

        # title stored in "title" attribute
        job["title"] = job_element.get_attribute("title")

        # company stored in the class "card__job-empname-label"
        job["company"] = job_element.find_element(
            By.CLASS_NAME, "card__job-empname-label").text  # must use .text to get the text value

        # image stored in the class "card__job-logo" src attribute (if it exists)
        try:
            job["image_url"] = job_element.find_element(
                By.CLASS_NAME, "card__job-logo").get_attribute("src")
        except:
            job["image_url"] = None

        jobs.append(job)

    return jobs


def test_scraping():
    """
    Tests the scraping functions
    - creates a chromedriver path
    - creates a url
    - scrapes the jobs
    - writes the jobs to a file named jobs.txt
    """

    # create the chromedriver path
    chromedriver_path = create_chromedriver_path()

    # create the url
    url = create_scraping_url("Software", "Charlotte")

    # scrape the jobs
    jobs = scrape_jobs(chromedriver_path, url)

    # write the jobs to a file
    with open("jobs.txt", "w") as f:
        for job in jobs:
            f.write(f"Title: {job['title']}\n")
            f.write(f"Company: {job['company']}\n")
            f.write(f"Image: {job['image_url']}\n")


if __name__ == "__main__":
    test_scraping()
