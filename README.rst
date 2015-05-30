You'll need a postgres database installed.


I'm cheating but here's a tutorial that includes how to install postges:
	https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-django-with-postgres-nginx-and-gunicorn





postgres=# create database games;



postgres=# create user games with password 'games';


postgres=# grant all privileges on database "games" to games;
