# coding=utf-8
from pymongo import MongoClient
import pprint
import pandas as pd
import numpy as np
import re
from random import randint
import random

test3Answers = [
  {"number":15,"question":"","answers":6,"correctAnswer":[2],"set":1},
  {"number":16,"question":"","answers":6,"correctAnswer":[1],"set":1},
  {"number":17,"question":"","answers":8,"correctAnswer":[8],"set":1},
  {"number":18,"question":"","answers":6,"correctAnswer":[3],"set":1},
  {"number":19,"question":"","answers":8,"correctAnswer":[7],"set":1},
  {"number":20,"question":"","answers":8,"correctAnswer":[1],"set":2},
  {"number":21,"question":"","answers":8,"correctAnswer":[4],"set":2},
  {"number":22,"question":"","answers":8,"correctAnswer":[6],"set":2},
  {"number":23,"question":"","answers":8,"correctAnswer":[5],"set":2},
  {"number":24,"question":"","answers":6,"correctAnswer":[5],"set":2},
  {"number":25,"question":"","answers":8,"correctAnswer":[1],"set":3},
  {"number":26,"question":"","answers":8,"correctAnswer":[8],"set":3},
  {"number":27,"question":"","answers":8,"correctAnswer":[4,2],"set":3},
  {"number":28,"question":"","answers":8,"correctAnswer":[8,2],"set":3},
  {"number":29,"question":"","answers":8,"correctAnswer":[3,2],"set":3},
  {"number":30,"question":"","answers":8,"correctAnswer":[4,2],"set":4},
  {"number":31,"question":"","answers":8,"correctAnswer":[2,2],"set":4},
  {"number":32,"question":"","answers":8,"correctAnswer":[7,2],"set":4},
  {"number":33,"question":"","answers":8,"correctAnswer":[7,2],"set":4},
  {"number":34,"question":"","answers":8,"correctAnswer":[7,2],"set":4},
  {"number":35,"question":"","answers":8,"correctAnswer":[3,2],"set":5},
  {"number":36,"question":"","answers":8,"correctAnswer":[5,2],"set":5},
  {"number":37,"question":"","answers":8,"correctAnswer":[3,2],"set":5},
  {"number":38,"question":"","answers":8,"correctAnswer":[4,2],"set":5},
  {"number":39,"question":"","answers":8,"correctAnswer":[1,2],"set":5},
  {"number":40,"question":"","answers":8,"correctAnswer":[8,6],"set":6},
  {"number":41,"question":"","answers":8,"correctAnswer":[1,2],"set":6},
  {"number":42,"question":"","answers":8,"correctAnswer":[8,5],"set":6},
  {"number":43,"question":"","answers":8,"correctAnswer":[2,4],"set":6},
  {"number":44,"question":"","answers":8,"correctAnswer":[1,2],"set":6},
  {"number":45,"question":"","answers":8,"correctAnswer":[2,3],"set":7},
  {"number":46,"question":"","answers":8,"correctAnswer":[2,3],"set":7},
  {"number":47,"question":"","answers":8,"correctAnswer":[1,2],"set":7},
  {"number":48,"question":"","answers":8,"correctAnswer":[7,3],"set":7},
  ]

test4Answers = [
  {"number":0,"correctAnswer":["Celoso","Asustado","Arrogante","Odio"]},
  {"number":1,"correctAnswer":["Entusiasmado","Reconfortante","Irritado","Aburrido"]},
  {"number":2,"correctAnswer":["Aterrado","Compungido","Arrogante","Enojado"]},
  {"number":3,"correctAnswer":["Bromista","Agitada","Deseo","Convencida"]},
  {"number":4,"correctAnswer":["Bromista","Insistente","Entretenido","Relajado"]},
  {"number":5,"correctAnswer":["Irritado","Sarcástico","Preocupado","Simpático"]},
  {"number":6,"correctAnswer":["Horrorizada","Fantasiosa","Impaciente","Alarmada"]},
  {"number":7,"correctAnswer":["Disculpante","Simpático","Intranquilo","Decaído"]},
  {"number":8,"correctAnswer":["Abatido","Relajado","Tímido","Excitado"]},
  {"number":9,"correctAnswer":["Enojada","Hostil","Aterrorizada","Acongojada"]},
  {"number":10,"correctAnswer":["Prudente","Insistente","Aburrido","Horrorizado"]},
  {"number":11,"correctAnswer":["Aterrado","Entretenido","Arrepentido","Seductor"]},
  {"number":12,"correctAnswer":["Indiferente","Abochornado","Escéptico","Decaído"]},
  {"number":13,"correctAnswer":["Contundente","Expectante","Amenazante","Severo"]},
  {"number":14,"correctAnswer":["Irritado","Decepcionado","Deprimido","Acusar"]},
  {"number":15,"correctAnswer":["Pensativa","Agitada","Ilusionada","Entretenida"]},
  {"number":16,"correctAnswer":["Irritado","Meditativo","Ilusionado","Compasivo"]},
  {"number":17,"correctAnswer":["Insegura","Afectuosa","Entusiasmada","Horrorizada"]},
  {"number":18,"correctAnswer":["Contundente","Entretenida","Horrorizada","Aburrida"]},
  {"number":19,"correctAnswer":["Arrogante","Agradecida","Sarcástica","Vacilante"]},
  {"number":20,"correctAnswer":["Imponente","Simpático","Culpable","Aterrorizado"]},
  {"number":21,"correctAnswer":["Abochornada","Fantasiosa","Confundida","Asustada"]},
  {"number":22,"correctAnswer":["Acongojada","Agradecida","Insistente","Suplicante"]},
  {"number":23,"correctAnswer":["Satisfecho","Disculpante","Desafiante","Curioso"]},
  {"number":24,"correctAnswer":["Caviloso","Irritado","Excitado","Hostil"]},
  {"number":25,"correctAnswer":["Asustada","Incrédula","Abatida","Interesada"]},
  {"number":26,"correctAnswer":["Alarmado","Tímido","Hostil","Ansioso"]},
  {"number":27,"correctAnswer":["Bromista","Prudente","Arrogante","Tranquilizadora"]},
  {"number":28,"correctAnswer":["Interesada","Bromista","Afectuosa","Satisfecha"]},
  {"number":29,"correctAnswer":["Impaciente","Horrorizada","Irritada","Reflexiva"]},
  {"number":30,"correctAnswer":["Agradecida","Seductora","Hostil","Decepcionada"]},
  {"number":31,"correctAnswer":["Avergonzada","Segura","Entusiasmada","Decaída"]},
  {"number":32,"correctAnswer":["Serio","Horrorizado","Aturdido","Alarmado"]},
  {"number":33,"correctAnswer":["Abochornado","Culpable","Fantasioso","Inquieto"]},
  {"number":34,"correctAnswer":["Horrorizada","Desconcertada","Recelosa","Aterrada"]},
  {"number":35,"correctAnswer":["Confusa","Nerviosa","Insistente","Pensativa"]},
  {"number":36,"correctAnswer":["Avergonzado","Nervioso","Desconfiado","Indeciso"]},
  ];

test2Answers = [
  {"number":6,"question":"Por donde entra la luz","answers":"__NT_NA","correctAnswer":["VENTANA","BENTANA"],"set":1},
  {"number":7,"question":"Enredo","answers":"_IO","correctAnswer":["LIO"],"set":1},
  {"number":8,"question":"Vive en una zona muy fría","answers":"__Q__M_L","correctAnswer":["ESQUIMAL","ESKIMAL"],"set":1},
  {"number":9,"question":"Un pariente","answers":"_RI__","correctAnswer":["PRIMO","PLIMO"],"set":1},
  {"number":10,"question":"Anotar","answers":"E_C_I___","correctAnswer":["ESCRIBIR","ESCRIVIR"],"set":1},
  {"number":11,"question":"Responder a un favor","answers":"__RA__CE_","correctAnswer":["AGRADECER"],"set":2},
  {"number":12,"question":"Relacionado con la investigación","answers":"_XP___M____","correctAnswer":["EXPERIMENTO","ESPERIMENTO"],"set":2},
  {"number":13,"question":"Afable, cariñoso o afectuoso","answers":"COR___L","correctAnswer":["CORDIAL"],"set":2},
  {"number":14,"question":"Excluir, no contar  con...","answers":"P_ES_I_D__","correctAnswer":["PRESCINDIR"],"set":2},
  {"number":15,"question":"Agradable, alegre","answers":"_I_P___CO","correctAnswer":["SIMPATICO"],"set":2},
  {"number":16,"question":"Dibujo con rasgos exagerados","answers":"_A_IC_T_R_","correctAnswer":["CARICATURA"],"set":3},
  {"number":17,"question":"Odio","answers":"_E_C_R","correctAnswer":["RENCOR"],"set":3},
  {"number":18,"question":"Un tipo de crimen","answers":"A_EN__D_","correctAnswer":["ATENTADO","ATENADO"],"set":3},
  {"number":19,"question":"Bastante","answers":"_U_I_I_N_E","correctAnswer":["SUFICIENTE"],"set":3},
  {"number":20,"question":"Capacidad o fuerza para actuar","answers":"_NE_G__","correctAnswer":["ENERGIA"],"set":3},
  {"number":21,"question":"Alto","answers":"_L_V___","correctAnswer":["ELEVADO","ELEVADOR"],"set":4},
  {"number":22,"question":"Desfavorecido de la suerte","answers":"__FO__U_A_O","correctAnswer":["INFORTUNADO","DESFORTUNADO"],"set":4},
  {"number":23,"question":"\"Pero, Doctor, realmente estoy enfermo; siempre me duele algo\"","answers":"_I_OCO__R_A_O","correctAnswer":["HIPOCONDRIACO"],"set":4},
  {"number":24,"question":"Obstaculizar","answers":"E__OR__R","correctAnswer":["ESTORBAR","ESTORVAR"],"set":4},
  {"number":25,"question":"Perseverante","answers":"C_N_T___E","correctAnswer":["CONSTANTE"],"set":4},
  {"number":26,"question":"Aceptar sin entusiasmo","answers":"_O_SE__I_","correctAnswer":["CONSENTIR"],"set":5},
  {"number":27,"question":"Charla","answers":"__N_E__A_I__","correctAnswer":["CONVERSACION"],"set":5},
  {"number":28,"question":"Necio o imprudente","answers":"__SE_S___","correctAnswer":["INSENSATO"],"set":5},
  {"number":29,"question":"Uno que destaca","answers":"__B_E_AL__N_E","correctAnswer":["SOBRESALIENTE"],"set":5},
  {"number":30,"question":"Corregir","answers":"_N_EN__R","correctAnswer":["ENMENDAR"],"set":6},
  {"number":31,"question":"Como algunas manchas o tintes","answers":"_ND__EB__","correctAnswer":["INDELEBLE"],"set":6},
  {"number":32,"question":"Con apariencia de verdadero","answers":"_E_O__M__","correctAnswer":["VEROSIMIL"],"set":6},
  {"number":33,"question":"Secreto y furtivo","answers":"C__ND_S___O","correctAnswer":["CLANDESTINO"],"set":6},
  {"number":34,"question":"Poderoso, arrogante","answers":"_R__O_E__E","correctAnswer":["PREPOTENTE"],"set":7},
  {"number":35,"question":"Establecer contacto","answers":"_O__C__R","correctAnswer":["CONECTAR","CONTACTAR","CONOCER"],"set":7},
  {"number":36,"question":"Algo oscuro o misterioso","answers":"_N_G__","correctAnswer":["ENIGMA"],"set":7},
  {"number":37,"question":"Apasionadamente aferrado a sus ideas","answers":"___A_I_O","correctAnswer":["FANATICO"],"set":7}
  ]

test1Answers = [
  {"number":31,"correctAnswer":["ANCLA","HANCLA"],"set":7},
  {"number":32,"correctAnswer":["ENCHUFE","NCHUFE"],"set":7},
  {"number":33,"correctAnswer":["CALCULADORA","CALCU"],"set":7},
  {"number":34,"correctAnswer":["ANZUELO","ANSUELO","HANZUELO"],"set":7},
  {"number":35,"correctAnswer":["SILLA MONTAR","SILLA"],"set":7},
  {"number":36,"correctAnswer":["ESCALERA MECANICA","ESCALERAS"],"set":8},
  {"number":37,"correctAnswer":["EMBUDO","ENBUDO"],"set":8},
  {"number":38,"correctAnswer":["COMPAS"],"set":8},
  {"number":39,"correctAnswer":["SALTAMONTES","GRILLO","INSECTO"],"set":8},
  {"number":40,"correctAnswer":["BALANZA","PESO","VALANZA"],"set":8},
  {"number":41,"correctAnswer":["MICROSCOPIO","MECROSCOPIO"],"set":9},
  {"number":42,"correctAnswer":["EXTINTOR","ESTINTOR"],"set":9},
  {"number":43,"correctAnswer":["HEXAGONO","EXAGONO"],"set":9},
  {"number":44,"correctAnswer":["YUNQUE","LLUNQUE"],"set":9},
  {"number":45,"correctAnswer":["SALVAVIDAS","SALVABIDAS"],"set":9},
  ]



def generateAnswer(testAnswers,testNo,frequencies):
	answers = []
	half = int(len(testAnswers) / 2.0)
	hh = int(half / 2.0)
	mu, sigma = half, hh # mean and standard deviation
	s = int(np.random.normal(mu, sigma, 1))
	if testNo == 4:
		texts = "Test de los ojos - item "
	else:
		texts = "Test " + str(testNo) + " - item "
	if s >= len(testAnswers) or testNo == 4 or testNo == 1:
		s = len(testAnswers) -1
	elif s <= 0:
		s = half
	#print("answer range: {}").format(s)
	#print("Testno: {}").format(testNo)
	for i in range(s-1):
		number = i
		if testNo == 4 or testNo == 2:
			itemstring = texts + str(i)
		else:
			itemstring = texts + str(i+1)
			number = i+1
		freq = frequencies[itemstring].value_counts()
		rg = 3
		if len(freq) > rg:
			elements = []
			for item in range(rg):
				if isinstance(freq.index[item],(basestring)):
					elements += [freq.index[item]]*freq[item]
				else:
					elements += freq.index[item]*freq[item]
			val = random.choice(elements)
			if isinstance(val,(basestring)) and "_" in val:
				val = val = freq.index[0]
		else:
			#just pick the most common value:
			val = freq.index[0]
		#if len(testAnswers[i]["correctAnswer"]) > 1:
		#	c = randint(0,len(testAnswers[i]["correctAnswer"])-1)
		#else:
		#	c = 0
		#val = testAnswers[i]["correctAnswer"][c]

		if isinstance(val,(basestring)):
			val = val.lower()
		n = testNo
		if testNo == 3:
			n = 1
		elif testNo == 1:
			n = 3

		answers.append({"testNo":n,"answerNo":number,"answerValue":val})
	return answers


client = MongoClient('172.17.0.9', 27017)
db = client.users
collection = db.users

data = pd.read_excel("file://localhost/home/slimbook/Documentos/sources/nodejs_mongo_server/Report(7).xlsx",sheetname = 'sheet1')

for i in range(50):
	test3 = generateAnswer(test1Answers,1,data)	
	test2 = generateAnswer(test2Answers,2,data)
	test4 = generateAnswer(test4Answers,4,data)
	test1 = generateAnswer(test3Answers,3,data)
	answers = test1 + test2 + test3 + test4
	#print("User : {}").format(i)
	#print(answers)
	user = {"idUser":i+636,"answers":answers}
	result = collection.insert_one(user)
	print(result)
