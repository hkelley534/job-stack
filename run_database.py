from database_manager import JobsDatabase
from json_writer import dict_list_to_json
from scrape_jobs import *


def main():

    # create the chromedriver path
    chromedriver_path = create_chromedriver_path()

    # create the url
    url = create_scraping_url("Software", "Charlotte")

    # scrape the jobs
    jobs = scrape_jobs(chromedriver_path, url)

    # write the jobs to a file
    dict_list_to_json(jobs, "jobs.json")

    # create the database
    jobs_database = JobsDatabase()

    # create the table
    jobs_database.create_table()

    # delete all the jobs
    jobs_database.delete_all_jobs()

    # insert the jobs
    for job in jobs:
        jobs_database.insert_job(job)

    # get all the jobs
    db_jobs = jobs_database.get_all_jobs()

    # print the jobs
    for job in db_jobs:
        print(job)

    # close the database
    jobs_database.close()


if __name__ == "__main__":
    main()
