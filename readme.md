create virtualenv :
- virtualenv env

rename .env_default to .env then fill credentials on .env

to run dev (reload on save) : 
- source env/bin/activate 
- uvicorn server:app --reload

