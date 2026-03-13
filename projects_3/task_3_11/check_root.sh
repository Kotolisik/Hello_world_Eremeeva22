#!/bin/bash

check_root() {
        if [ $UID -ne 0 ]
        echo "ошибка!"
	exit 1
	fi
}
check_root
echo "Скрипт запущен"
