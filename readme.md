create virtualenv :
- virtualenv env

install all requirements from txt : pip3 install -r requirements.txt

rename .env_default to .env then fill credentials on .env

to run dev (reload on save) : 
- source env/bin/activate 
- uvicorn main:app --reload

