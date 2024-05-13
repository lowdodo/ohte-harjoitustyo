#instal poetry
1.
poetry install 


#build the database:
2. 
poetry run invoke build

#start the game
3. 
poetry run invoke start

##pylint:

you can run pylint with:

poetry run invoke lint