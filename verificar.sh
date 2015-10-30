#!/bin/bash
# Verifica se há pacotes inexistentes listados no arquivo packagelist
zypper se -t package > todos_os_pacotes
inexistentes=""
for p in `cat packagelist`; do
    if [[ -z "$(cat todos_os_pacotes | grep $p)" ]]; then
        echo $p
    fi
done
rm todos_os_pacotes
