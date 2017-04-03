insert into admin (login, password) values ("root", "root");

insert into body (name) values ("ril15");
insert into body (name) values ("professeur");

insert into badger (firstname, lastname, qr_id, body_id) values ("Bob", "Lejuste", "555", "1");
insert into badger (firstname, lastname, qr_id, body_id) values ("Romain", "Durant", "556", "1");
insert into badger (firstname, lastname, qr_id, body_id) values ("Hector", "Hublot", "557", "2");
insert into badger (firstname, lastname, qr_id, body_id) values ("Seb", "Codec", "558", "1");
insert into badger (firstname, lastname, qr_id, body_id) values ("Patricia", "Carotte", "559", "1");

insert into room (name) values ("Saint Malo");
insert into room (name) values ("Bordeaux");
insert into room (name) values ("La Rochelle");
insert into room (name) values ("Nantes");
insert into room (name) values ("Metz");
insert into room (name) values ("Limoges");
insert into room (name) values ("Perpignan");
insert into room (name) values ("Lyon");
insert into room (name) values ("Avignon");
insert into room (name) values ("La Chapelle");

insert into presence (badger_id, room_id, morning_date, afternoon_date) values ("1", "6", "2017-03-03 09:30:00", "2017-03-03 14:30:00");
insert into presence (badger_id, room_id, morning_date, afternoon_date) values ("3", "6", "2017-04-04 08:30:00", "2017-04-04 13:30:00");

insert into planning (date, body_id, room_id) value ("2017-03-03", "1", "6")