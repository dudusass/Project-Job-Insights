from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    jobs = read_brazilian_file('tests/mocks/brazilians_jobs.csv')
    el = jobs[-1]
    assert el == {
        "title": "Auxiliar de manutenção",
        "salary": ' 1400',
        "type": ' full time',
    }
