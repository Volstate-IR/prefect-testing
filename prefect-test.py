from prefect import flow, task
from datetime import date

@flow
def test_flow():
    test_task()


@task
def test_task():
    
    today = date.today()
    
    print('Hello, RASI!')
    print(f'It is currently {today.year}')


if __name__ == "__main__":
    test_flow()