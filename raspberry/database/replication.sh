#!/bin/bash

### BEGIN INIT INFO
# Provides:          piserver
# Required-Start:    $all
# Required-Stop:     $all
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: DomoticBox code
# Description:       Box domotique de Benjamin Touchard
### END INIT INFO

PASSWORD=rasp_user
HOST="raspi.com"
USER=rasp_user
DATABASE=mydb
#EXCLUDED_TABLES=(
#presence
#)

#IGNORED_TABLES_STRING=''
for TABLE in "${EXCLUDED_TABLES[@]}"
do :
   IGNORED_TABLES_STRING+=" --ignore-table=${DATABASE}.${TABLE}"
done

while :
do
	ping -c1 ${HOST} 2>/dev/null 1>/dev/null
	if [ "$?" = 0 ]
	then

	 	mysqldump -h ${HOST} --user=${USER} --password=${PASSWORD} -e -q --single-transaction --master-data --databases ${DATABASE} > /home/pi/Raspberry/database/test_dump.sql 2>&1

		sed -i "s/CHANGE MASTER TO MASTER_LOG_FILE/CHANGE MASTER TO MASTER_HOST='${HOST}',MASTER_PORT=3306, MASTER_USER='rasp_user', MASTER_PASSWORD='rasp_user',master_log_file/" /home/pi/Raspberry/database/test_dump.sql
		sed -i "21i STOP SLAVE;" /home/pi/Raspberry/database/test_dump.sql
		sed -i "25i START SLAVE;" /home/pi/Raspberry/database/test_dump.sql

		mysql --user=root --password=root ${DATABASE} < /home/pi/Raspberry/database/test_dump.sql

	 	break
	else
	 	sleep 10
	fi
done
