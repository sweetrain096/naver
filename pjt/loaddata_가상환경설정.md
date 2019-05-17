# README

### csv2json-fixture

> csv를 json 파일로 변경하여 DB에 저장하는 법

1. git clone = "https://github.com/maur1th/csv2json-fixture.git"

2. cd fixture
3. `python csv2json.py movie.csv movies.Movie`
4. "[]" => [] 
5. `python manage.py loaddata movie.json`



### local pyenv 가상환경 설정

1. pyenv install 3.7.2
2. pyenv global 3.7.2
3. pyenv rehash
4. python -V

== 파이썬 버전 확인하고 가상환경 원하는 폴더에서 ==

5. python -m venv django-venv
6. cd django-venv
7. source Scripts/activate

== 그러면 ==

(django-venv)

student@DESKTOP MINGW64 ~/Desktop/django/django-venv

