banner(){
clear
python /data/data/com.termux/files/home/wiki-termux/banhome
red="\e[1;31m"
gr="\e[1;32m"
nd="\e[0m"

echo -e "\e[1;36m"
read -p "Elige una opción: " opc

case $opc in
	1)bash comandos
	    ;;
	2)bash librerias
	    ;;
	3)cd /data/data/com.termux/files/home/wiki-termux
	bash herramientas
	    ;;
	99)echo -e "\e[1;33mHASTA LUEGO :)"
	sleep 0.5
	 exit
	  ;;
	*) echo "Opción invalida"
	 sleep 0.5
	 banner
	    ;;
esac
}
banner



