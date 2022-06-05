import os 
import time
from colorama import Fore, Style, init 

init(autoreset=True)

code={}
code["а"]="¢"
code["б"]="◤"
code["в"]="π"
code["г"]="&"
code["д"]="₴"
code["ё"]="œ"
code["е"]="£"
code["є"]="¥"
code["э"]="⚈"
code["ж"]="𖨆"
code["з"]="⊹"
code["ы"]="å"
code["и"]="✉"
code["і"]="•"
code["й"]="√"
code["ї"]="æ"
code["к"]="~"
code["л"]="õ"
code["м"]="™"
code["н"]="۵"
code["о"]="%"
code["п"]="℅"
code["р"]="✺"
code["с"]="✜"
code["т"]="≛"
code["у"]="©"
code["ф"]="ᦗ"
code["х"]="∆"
code["ц"]="¶"
code["ч"]="×"
code["ш"]="÷"
code["щ"]="^"
code["ь"]="߷"
code["ю"]="╚"
code["я"]="𖤂"
code[" "]="€"
code[","]="°"
code["?"]="ü"
code["."]="ē"
code["a"]="∭"
code["b"]="ñ"
code["c"]="û"
code["d"]="ą"
code["e"]="𖢺"
code["f"]="𖣵"
code["g"]="𖥑"
code["h"]="≠"
code["i"]="ෆ"
code["j"]="◇"
code["k"]="◈"
code["l"]="▧"
code["m"]="✠"
code["n"]="☯"
code["o"]="ツ"
code["p"]="∞"
code["q"]="☭"
code["r"]="𖠰"
code["s"]="𖣫"
code["t"]="ᕕ"
code["u"]="♔"
code["v"]="┏"
code["w"]="╔"
code["x"]="╩"
code["y"]="╬"
code["z"]="〢"
code[")"]="「"
code["("]="♙"


decode={}
decode["¢"]="а"
decode["◤"]="б"
decode["π"]="в"
decode["&"]="г"
decode["₴"]="д"
decode["£"]="е"
decode["¥"]="є"
decode["⚈"]="э"
decode["𖨆"]="ж"
decode["⊹"]="з"
decode["✉"]="и"
decode["å"]="ы"
decode["•"]="і"
decode["√"]="й"
decode["æ"]="ї"
decode["~"]="к"
decode["õ"]="л"
decode["™"]="м"
decode["۵"]="н"
decode["%"]="о"
decode["℅"]="п"
decode["✺"]="р"
decode["✜"]="с"
decode["≛"]="т"
decode["©"]="у"
decode["ᦗ"]="ф"
decode["∆"]="х"
decode["¶"]="ц"
decode["×"]="ч"
decode["÷"]="ш"
decode["^"]="щ"
decode["߷"]="ь"
decode["╚"]="ю"
decode["𖤂"]="я"
decode["€"]=" "
decode["°"]=","
decode["?"]="ü"
decode["ē"]="."
decode["∭"]="a"
decode["ñ"]="b"
decode["û"]="c"
decode["ą"]="d"
decode["𖢺"]="e"
decode["𖣵"]="f"
decode["𖥑"]="g"
decode["≠"]="h"
decode["ෆ"]="i"
decode["◇"]="j"
decode["◈"]="k"
decode["▧"]="l"
decode["✠"]="m"
decode["☯"]="n"
decode["ツ"]="o"
decode["∞"]="p"
decode["☭"]="q"
decode["𖠰"]="r"
decode["𖣫"]="s"
decode["ᕕ"]="t"
decode["♔"]="u"
decode["┏"]="v"
decode["╔"]="w"
decode["╩"]="x"
decode["╬"]="y"
decode["〢"]="z"
decode["「"]=")"
decode["♙"]="("

def banner():
	os.system("figlet Text coder")
	os.system("echo                             by: github.com/Wemis|lolcat")

def menu():
	print("-1- encode text")
	print("-2- decode text")
	print("-3- encode .txt file")
	print("-4- decode .txt file")

def error():
	print("")
	print(Fore.RED + "  [*] Invalid input")
	Style.RESET_ALL
	time.sleep(2)
	os.system("clear")

def exit():
	e=input(Fore.GREEN + "Press Enter to back#")
	Style.RESET_ALL
	os.system("clear")

while True:
	banner()
	menu()
	choice=int(input("> "))
	if choice == 1:
		text=input("input text for encoding: ")
		text2=''.join([code.get(i,i) for i in text])
		if text == text2:
			error()
			continue
		print(Fore.BLUE + "your result: ", text2)
		print("")
		e=input(Fore.GREEN + "Press Enter to back#")
		os.system("clear")
	if choice == 2:
		chiper = input("input chiper: ")
		normal_text=''.join([decode.get(i,i) for i in chiper])
		if chiper==normal_text:
			error()
			continue
		print(Fore.BLUE + "your result: ", normal_text)
		print("")
		e2=input(Fore.GREEN + " Press Enter to back#")
		os.system("clear")
	if choice == 3:
		filename=input("input path to the file: ")
		filepath=input("input path to the file for save: ")
		try:
			with open(filename, "r") as f:
				filetext = f.read()
				f.close()
		except:
			error()
			continue
		chiper=''.join([code.get(i,i) for i in filetext])
		if filetext == chiper:
			error()
			continue
		with open(filepath, "w") as save:
			save.write(chiper)
			save.close()
		print(Fore.GREEN + " [*] File saved!")
		exit()
	if choice == 4:
		filename1=input("input path to the file: ")
		filepath1=input("input path to the file for save: ")
		try:
			with open(filename1, "r") as t:
				filetext1=t.read()
				t.close()
		except:
			error()
			continue
		normaldata=''.join([decode.get(i,i) for i in filetext1])
		if filetext1 == normaldata:
			error()
			continue
		with open(filepath1, "w") as save1:
			save1.write(normaldata)
			save1.close()
		print(Fore.GREEN + " [*] File saved!")
		exit()


