uliana = 0
alice = 0
slavya = 0
lena = 0
miku = 0
uvao = 0
open_endes = str(input("Открыты ли концовки(Мику и или ЮВАО)"))

if open_endes == "main":
	def printscore():
		print("Ульяна:", uliana)
		print("Алиса:", alice)
		print("Славя:", slavya)
		print("Лена:", lena)
		print("Мику:", miku)

elif open_endes == "no":
	def printscore():
		print("Ульяна:", uliana)
		print("Алиса:", alice)
		print("Славя:", slavya)
		print("Лена:", lena)
else:
	def printscore():
		print("Ульяна:", uliana)
		print("Алиса:", alice)
		print("Славя:", slavya)
		print("Лена:", lena)
		print("Мику:", miku)


poity_za_golosom = str(input("Пойти за голосом?"))
if poity_za_golosom == "yes":
	uvao = uvao+1
else:
	miku = miku+1
printscore()
otvetit_slave = str(input("Ответить Славе?"))
if otvetit_slave == "yes":
	slavya = slavya+1
printscore()
pobejat_ot_alice = str(input("Побежать от Алисы?"))
if pobejat_ot_alice == "no":
	alice = alice+1
printscore()

otniyat_kotletu = str(input("Отнять котлету?"))
if otniyat_kotletu == "yes":
	uliana = uliana+1
printscore()
vzat_kluchi = str(input("Взять ключи?"))
if vzat_kluchi == "yes":
	miku = miku+1
else:
	uvao = uvao+1
printscore()
pohvalit_knigu = str(input("Похвалить книгу?"))
if pohvalit_knigu == "yes":
	lena = lena+1
printscore()
karta = str(input("Карта.Вы выбрали столовую первый или второй раз?"))
if karta == "yes":
	uliana = uliana+1
printscore()
idti_za_kartami = str(input("Пойти за картами одному?"))
if idti_za_kartami == "yes":
	if vzat_kluchi == "yes":
		miku = miku+1
	
else:
	slavya = slavya+1
printscore()

posporit_s_alice = str(input("Поспорить с Алисой?"))
if posporit_s_alice == "yes":
	alice = alice+2
	lena = lena-1
else:
	alice = alice-1
	lena = lena+2
printscore()


tournament = str(input("Турнир.(lost l, lust u, win, lost)"))
if tournament == "lost l":
	lena = lena+1
elif tournament == "lost u":
	uliana = uliana+1
elif tournament == "win":
	alice=alice+2
printscore()

kudaidti = str(input("Куда идти?(pole, scene)"))
if kudaidti == "pole" and posporit_s_alice == "no" and tournament == "lost l":
	lena = lena+1
elif kudaidti == "scene" and tournament == "lost u":
	uliana = uliana+1
elif tournament != "win" and idti_za_kartami == "no" and kudaidti == "autobus":
	slavya = slavya+1
printscore()


s_kem_obedat = str(input("С кем обедать?"))
if s_kem_obedat == "lena":
	lena = lena+1
printscore()
pomoch_lene = str(input("Помогать Лене?"))
if pomoch_lene == "yes":
	lena = lena+1
printscore()
poiti_posmotret = str(input("Пойти посмотреть?"))
if poiti_posmotret == "yes":
	soglasitsya = str(input("Солгласиться на предложение Алисы?"))
	if soglasitsya == "yes":
		alice = alice+1
else:
	komu_pomoch = str(input("Кому помочь?"))
	if komu_pomoch == "Slave":
		slavya = slavya+1
	elif komu_pomoch == "sport":
		uliana = uliana+1

printscore()		
pomoch_uliane = str(input("Помочь Убраться Ульяне?"))
if pomoch_uliane == "yes":
	uliana = uliana+1
else:
	slavya = slavya+1	
printscore()
disco = str(input("Пойти на дискотеку?"))
if disco == "yes" and pomoch_lene == "yes":
	if soglasitsya == "yes":
		alice = alice-5
elif disco == "yes" and pomoch_lene == "no":
	uvao = uvao+1
elif disco == "no" and soglasitsya == "yes":
	if pomoch_lene == "yes":
		lena == lena-5
	govorit_chto_bil_s_alice = str(input("Говорить что был с Алисой:"))
	if govorit_chto_bil_s_alice == "no":
		alice = alice+1

karta2 = str(input("Карта, куда пойти:(ostanovka)"))
printscore()
if karta2 == "ostanovka":
	soglasitsya_pomoch = str("Согласиться помочь")
	if soglasitsya_pomoch == "yes":
		miku = miku+1
printscore()
lena1 = str(input("На тебе это бы смотрелось прекрасно"))
if lena1 == "yes":
	lena = lena+1
printscore()
uliana1 = str(input("В столовой отравилась:"))
if uliana1 == "yes":
	uliana = uliana+1
printscore()
slavya1 = str(input("Не спрашивать:"))
if slavya1 == "yes":
	slavya = slavya+1
printscore()
alice1 = str(input("Дать угля:"))
if alice1 == "yes":
	alice = alice+1
printscore()
apple = str(input("Съесть яблоко:"))
if apple == "yes":
	uvao = uvao+1
s_kem_idti = str(input("С кем идти(alone, lena)"))
if s_kem_idti == "alone":
	svrnutnalevo = str(input("Свернуть два раза на лево?"))
	if svrnutnalevo == "yes":
		if open_endes == "main":
			print("Мику-рут")
		elif open_endes == "miku":
			idtilivgorod = str(input("Идти ли в город"))
			if idtilivgorod == "yes":
				print("Гарем")
			else:
				print("ЮВАО-рут")

elif s_kem_idti == "lena":
	upomenat_pro_lenu = str(input("Упоменать про Лену"))
	if upomenat_pro_lenu == "no":
		lena = lena+1
printscore()
karta3 = str(input("Карта, куда же пойти?(kruzki)"))
if karta3 == "kruzki":
	otkazaztsa = str(input("Отказаться?"))
	if otkazaztsa == "yes":
		uliana = uliana+1

printscore()
s_kem_klubnika = str(input("С кем соберать клубнику?"))

if s_kem_klubnika == "lena":
	lena = lena+2
else:
	slavya = slavya+1
printscore()	
chiya_zasluga = str(input("Чья заслуга"))

if chiya_zasluga != "my":
	slavya = slavya+1
kniga_alice = str(input("Выхватить Книгу?"))
printscore()
if kniga_alice == "no":
	alice = alice+1
pohod = str(input("Поход(lenaaalice, sit)"))
printscore()
if alice >6 or lena>6 and pohod == "lenaalice":
	if alice > lena:
		if alice > 6 and alice <9:
			print("Alice Bad")
		else:
			print("Alice good")
	else:
		lena = lena-1
		if lena < 9:
			print("Lena Bad")
		else:
			print("Lena good")		
elif pohod == "sit":
	pohod2 = str(input("Кого искать или просто сидеть(uliana, slavya)"))
	if uliana > 6 and pohod2 == "uliana":
		popitatsaostanovit = str(input("Поптытаться остановить словами"))
		if popitatsaostanovit == "yes":
			uliana = uliana+1
		vzat_vinu = str(input("Взять вину на себя?"))
		if vzat_vinu == "yes":
			uliana = uliana+2
			if uliana >9:
				print("uliana good")
			else:
				print("uliana bad")
		else:
			uliana = uliana-2
			if uliana >9:
				print("uliana good")
			else:
				print("uliana bad")
	if slavya > 6 and pohod2 == "slavya":
		vzat_edu = str(input("Взять еду для Слави"))
		if vzat_edu == "yes":
			slavya = slavya+1
		mne_ne_v_chem_opravdivatsa = str(input("Мне не в чем оправдываться"))
		if mne_ne_v_chem_opravdivatsa == "yes":
			slavya = slavya+1
			if slavya >9:
				print("slavya good")
			else:
				print("slavya bad")
		else:
			slavya = slavya-2
			if slavya >9:
				print("slavya good")
			else:
				print("slavya bad")
	if pohod2 == "sit":
		poiti_za_golosom1 = str(input("Пойти за голосом?"))
		if poiti_za_golosom1 == "yes":
			print("Main Bad")
		else:
			print("Main Good")