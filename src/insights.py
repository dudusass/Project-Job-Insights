from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    jobs_type = set()

    for job in jobs:
        jobs_type.add(job["job_type"])
    return list(jobs_type)


def filter_by_job_type(jobs, job_type):
    filter_jobs = []

    for job in jobs:
        if job["job_type"] == job_type:
            filter_jobs.append(job)
    return filter_jobs


def get_unique_industries(path):
    industries = read(path)
    industries_types = set()

    for i in industries:
        if i["industry"] != "":
            industries_types.add(i["industry"])
    return list(industries_types)


def filter_by_industry(jobs, industry):
    filter_industry = []

    for job in jobs:
        if job["industry"] == industry:
            filter_industry.append(job)
    return filter_industry


def get_max_salary(path):
    salary = read(path)
    max_salary = 0

    for s in salary:
        if s["max_salary"] != "" and s["max_salary"] != "invalid":
            if int(s["max_salary"]) > max_salary:
                max_salary = int(s["max_salary"])
    return max_salary


def get_min_salary(path):
    salary = read(path)
    min_salary = 19857

    for s in salary:
        if s["min_salary"] != "" and s["min_salary"] != "invalid":
            if int(s["min_salary"]) < min_salary:
                min_salary = int(s["min_salary"])
    return min_salary


def matches_salary_range(job, salary):
    if "max_salary" not in job or "min_salary" not in job:
        raise ValueError()
    elif (
        not str(job["min_salary"]).isnumeric()
        or not str(job["max_salary"]).isnumeric()
    ):
        raise ValueError()
    elif type(salary) != int:
        raise ValueError()
    elif int(job["min_salary"]) > int(job["max_salary"]):
        raise ValueError()
    return int(job["min_salary"]) <= salary <= int(job["max_salary"])


def filter_by_salary_range(jobs, salary):
    salaries = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                salaries.append(job)
        except ValueError:
            print(ValueError)
    return salaries
