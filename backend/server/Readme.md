$ mkdir myproject
$ cd myproject
$ python3 -m venv venv

$ . venv/bin/activate

export FLASK_APP=server



create table user ( 
    -> userID int not null auto_increment primary key,
    -> username varchar(256),
    -> password varchar(256),
    -> email varchar(256))
    -> ;
