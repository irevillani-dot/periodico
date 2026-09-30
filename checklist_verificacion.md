# Verificación pendiente antes de publicar

El verificador no pudo abrir ninguna fuente original (bloqueo de red) y trabajó con fragmentos de buscador y espejos, así que todo sigue pendiente: abre cada fuente, busca lo indicado y marca la casilla; «Si se confirma» significa que la fuente respalda la frase tal como está en el original (`articulo.md`), y si no, pega la alternativa, que solo toca esa frase.

## A. Bloqueantes

### 1. OFAC, 18-sep: aviso sobre la emergencia (fuente del verificador)
Sin URL en el informe. Busca el aviso de la OFAC titulado "Expiration of Emergency With Respect to the Situation in Ethiopia".

- [ ] **Bloqueante.** «“La emergencia nacional ha llegado a su fin”, proclamó el Departamento del Tesoro.»
  - **Buscar:** texto no localizado: no existe esa cita literal. Lo que halló el verificador es el aviso "Expiration of Emergency With Respect to the Situation in Ethiopia", según el cual la emergencia "was not continued in effect beyond September 17, 2026".
  - **Si se confirma** (aparece la cita literal): nada.
  - **Si no se confirma:** sustituir la frase por:
    > El Departamento del Tesoro dio por expirada la emergencia nacional.

### 2. Addis Standard, 10-sep: Debretsion en Weyin Media (fuente del verificador)
Sin URL en el informe. Busca la pieza de Addis Standard del 10-sep que recoge la entrevista de Debretsion Gebremichael con Weyin Media.

- [ ] **Bloqueante.** «El líder del TPLF, Debretsion Gebremichael, lo admitía en el diario etíope Addis Standard: “Nuestros intereses no son los mismos, pero al menos hay algo común que nos une”.»
  - **Buscar:** "Our interests are not the same, we have our own respective interests, but at least we have one central thing that connects us." Comprueba también el contexto, que nadie ha visto: a quién se refería. La entrevista es diez días anterior a la alianza.
  - **Si se confirma:** nada.
  - **Si no se confirma:** si el texto es ese y habla de sus futuros aliados, sustituir la frase por:
    > Días antes, el líder del TPLF, Debretsion Gebremichael, lo admitía en una entrevista con Weyin Media recogida por el diario etíope Addis Standard: «Nuestros intereses no son los mismos […], pero al menos hay algo central que nos une».
  - **Si habla de otro actor o la cita no aparece:** suprimir la frase.

### 3. Addis Standard: el jefe del Ejército
<https://addisstandard.com/ethiopia-army-chief-accuses-foreign-powers-of-pushing-supporting-and-supplying-new-armed-alliance/>

- [ ] **Bloqueante.** «Según sus declaraciones, Eritrea actúa como intermediaria: “ni ella ni el TPLF pueden lograr nada a menos que Sudán, Egipto y otras potencias los impulsen, apoyen y suministren recursos”, relata Addis Standard.»
  - **Buscar:** "Neither Shaebia nor the TPLF can achieve anything alone – even if combined – unless pushed, supported, and supplied by Sudan, Egypt, and powers beyond." Para «intermediaria»: "He alleged that Eritrea… acts as an intermediary between external powers and armed groups". Cargo: "Field Marshal Birhanu Jula, Chief of General Staff of the ENDF".
  - **Si se confirma:** nada.
  - **Si no se confirma:** si el texto es el del verificador, sustituir la frase por la cita restituida (*Shaebia* es el nombre, peyorativo, que se da al régimen eritreo):
    > Según sus declaraciones, Eritrea actúa como intermediaria: «Ni [el régimen eritreo] ni el TPLF pueden lograr nada solos —ni siquiera juntos— a menos que Sudán, Egipto y potencias de más allá los impulsen, los apoyen y les suministren recursos», relata Addis Standard.
  - **Si la cita no aparece:** «Según sus declaraciones, recogidas por Addis Standard, Eritrea actúa como intermediaria entre potencias extranjeras y los grupos armados.»

### 4. The Economist
<https://www.economist.com/middle-east-and-africa/2026/09/23/a-disastrous-new-war-threatens-in-africa?giftId=YWM4OGUxMDgtYjgyYy00YTg0LTliYTQtYjJmZTJmZTI0ZmFk&utm_campaign=gifted_article>
Ojo: el verificador leyó la traducción de Infobae y fragmentos de buscador, así que el inglés de abajo puede no ser literal.

- [ ] **Bloqueante.** «“Fue una coincidencia curiosa”, ironiza The Economist, que advierte…»
  - **Buscar:** texto no localizado (el informe la da por no verificable).
  - **Si se confirma:** nada, aunque «apunta» es mejor que «ironiza», que le atribuye una intención.
  - **Si no se confirma:** cambiar «“Fue una coincidencia curiosa”, ironiza The Economist, que advierte» por «The Economist advierte».
- [ ] **Bloqueante.** «…que advierte de que esta vez será “radicalmente distinta” de la anterior.»
  - **Buscar:** "if fighting continues, the next round would be radically different"
  - **Si se confirma** (la fuente no pone condición): nada.
  - **Si no se confirma:** insertar el condicional: «…advierte de que, si los combates continúan, esta vez será “radicalmente distinta” de la anterior». Si no aparece la expresión, suprimir desde «, que advierte», y la frase entera si también cae «coincidencia curiosa».
- [ ] **Bloqueante.** «Su presidente, Isaias Afwerki, se sintió traicionado por la paz de Pretoria, de la que Eritrea quedó excluida pese a haber puesto tropas en la guerra, explica The Economist.»
  - **Buscar:** texto no localizado (no aparece en los fragmentos consultados).
  - **Si se confirma:** nada.
  - **Si no se confirma:** sustituir la frase por la de abajo y, en la siguiente, cambiar «A la traición se suma el miedo» por «A ello se suma el miedo».
    > Su presidente, Isaias Afwerki, quedó fuera de la paz de Pretoria pese a haber puesto tropas en la guerra.
- [ ] «Detrás de la alianza rebelde asoma Eritrea…»
  - **Buscar:** texto no localizado (el verificador no lo revisó). Comprueba si lo sostiene The Economist o solo el Gobierno etíope (sección 3).
  - **Si se confirma:** nada.
  - **Si no se confirma:** cambiar «Detrás de la alianza rebelde asoma Eritrea» por «Detrás de la alianza rebelde, Addis Abeba ve la mano de Eritrea».
- [ ] «El 18 de septiembre, Estados Unidos levantó el embargo de armas que pesaba sobre Etiopía desde 2021…»
  - **Buscar:** "on September 18 the US lifted the arms embargo on Ethiopia". Según el verificador, Etiopía estaba en la lista ITAR §126.1 desde noviembre de 2021; el fin de la política de denegación se decidió en febrero, se anunció en mayo y el 18-sep se publicó la norma final.
  - **Si se confirma:** nada.
  - **Si no se confirma:** cambiar «levantó el embargo» por «formalizó el fin del embargo».
- [ ] «el TPLF y las milicias Fano “parecen intentar cercar Weldiya” […]: “Si Weldiya cayera, podría ser el preludio de una ofensiva rebelde sobre la capital”»
  - **Buscar:** "The TPLF and Fano appear to be attempting to encircle Weldiya… If Weldiya were to fall, it could be the prelude to a rebel offensive against the Ethiopian capital."
  - **Si se confirma:** nada.
  - **Si no se confirma:** sustituir la frase por:
    > Según The Economist, el TPLF y las milicias Fano parecen intentar cercar Weldiya, una localidad del norte de Amhara situada en la carretera principal que une Tigray con Addis Abeba, cuya caída podría ser el preludio de una ofensiva rebelde sobre la capital.
- [ ] «Los rebeldes también amenazan interrumpir la carretera al puerto de Yibuti, del que Etiopía depende para casi todo su comercio exterior, combustible incluido.»
  - **Buscar:** "on which Ethiopia depends for almost all its international trade, including fuel imports". La amenaza a la carretera: texto no localizado (el verificador solo anota incursiones desde Afar).
  - **Si se confirma:** nada.
  - **Si no se confirma:** sustituir la frase por:
    > Los rebeldes también combaten en Afar, por donde pasa la principal carretera al puerto de Yibuti, del que Etiopía depende para casi todo su comercio exterior, combustible incluido.

### 5. AFP (vía France24 y Arab News), 27-sep: Tigrai TV (fuente del verificador)
Sin URL en el informe. Busca el despacho de AFP del 27-sep sobre Tigrai TV fuera de antena tras un ataque con dron.

- [ ] **Bloqueante.** «Incluso, un dron alcanzó en Mekelle la sede de Tigrai TV, la televisión pública regional y altavoz de las autoridades tigrinas, y la dejó fuera de antena.»
  - **Buscar:** "We heard a loud bang from a drone strike elsewhere and we fled the building" (periodista anónimo; otro periodista cuenta que la cadena quedó fuera de antena). Según esa cita, el dron no alcanzó la sede. Ojo también: el Gobierno federal había suspendido Tigrai TV "indefinitely" el 21-sep; si la AFP lo cuenta, aclara cómo seguía emitiendo.
  - **Si se confirma** (la AFP dice que el dron alcanzó la sede): nada, pero revisa entonces la cita del periodista («en otro lugar»).
  - **Si no se confirma:** sustituir la frase por:
    > Incluso Tigrai TV, la televisión pública regional con sede en Mekelle y altavoz de las autoridades tigrinas, quedó fuera de antena tras un ataque con dron.
  - **Si la cita del periodista no aparece en la AFP:** suprimir también la frase de la cita.
- [ ] La misma frase no da fecha, pero el párrafo anterior arranca con «El 23 de septiembre».
  - **Buscar:** texto no localizado: qué día sitúa la AFP el ataque (el verificador entiende que el domingo 27; Wikipedia dice el 23).
  - **Si se confirma el 27:** nada. Si quieres fecharlo: «Incluso, el domingo 27, …».
  - **Si no se confirma:** nada; no añadir fecha.

### 6. Reuters, 25-sep: el corte de internet (fuente del verificador)
Sin URL ni titular en el informe (el verificador usó el espejo de US News). Busca la información de Reuters del 25-sep sobre el corte de internet y telefonía en Tigray.

- [ ] **Bloqueante.** «Sobre el terreno, Tigray ha quedado aislada. Internet y las líneas móviles están cortadas…» (da a entender que el corte vino de fuera).
  - **Buscar:** texto no localizado; el verificador solo lo resume: según Reuters, el propio TPLF ordenó el corte a Safaricom y a Ethio Telecom, y hay compras de pánico.
  - **Si Reuters lo confirma:** precisarlo en la misma frase: «Internet y las líneas móviles están cortadas —por orden del propio TPLF, según Reuters— y las carreteras…».
  - **Si no lo confirma:** nada; no decir quién ordenó el corte.

### 7. Sin fuente identificada en el informe

- [ ] **Bloqueante.** «A la traición se suma el miedo, Addis Abeba ha amenazado con anexionar parte de la costa eritrea, y Asmara teme las amenazas.»
  - **Buscar:** «anexionar»: texto no localizado en ninguna fuente. Lo que halló el verificador, sin decir dónde, es que Abiy reclama Assab (y Massawa) "peacefully or by force"; un mando militar habló de "our survival interest worth paying any price for". Localiza el medio y la fecha.
  - **Si se confirma** (alguna fuente habla de anexión): nada.
  - **Si no se confirma:** si localizas lo de Abiy, sustituir la frase por:
    > A la traición se suma el miedo: Abiy ha reclamado el puerto eritreo de Assab sin descartar el uso de la fuerza, y Asmara teme las amenazas.
  - **Si tampoco localizas eso:** «A la traición se suma el miedo: Addis Abeba reclama una salida al mar por la costa eritrea, y Asmara lo vive como una amenaza.» En los dos casos, empieza por «A ello» si ya cambiaste la frase de Isaias.
- [ ] **Bloqueante.** «El conflicto causó unos 600.000 muertos, entre combates, hambruna y el colapso de la sanidad, según la estimación de la Unión Africana.»
  - **Buscar:** texto no localizado. Según el verificador, la cifra es del mediador de la UA, Olusegun Obasanjo, y no una estimación oficial de la UA (la Universidad de Gante calcula entre 162.000 y 378.000). Localiza la declaración de Obasanjo y qué muertes cuenta.
  - **Si se confirma:** nada.
  - **Si no se confirma:** si localizas lo de Obasanjo, cambiar «unos 600.000 muertos» por «hasta 600.000 muertos» y «según la estimación de la Unión Africana» por «según el mediador de la Unión Africana, Olusegun Obasanjo». Si no: «El conflicto causó cientos de miles de muertos, entre combates, hambruna y el colapso de la sanidad.»
- [ ] **Bloqueante.** «…el Frente Popular de Liberación de Tigray (TPLF), el partido que gobierna la región más septentrional…»
  - **Buscar:** texto no localizado; ninguna fuente del informe lo trata. En 2025 la junta electoral etíope retiró al TPLF el registro como partido, y además cambió la administración interina de Tigray. Compruébalo en la BBC o en las piezas de Al Jazeera.
  - **Si se confirma** (sigue siendo partido y gobierna la región): nada.
  - **Si no se confirma:** cambiar «el partido que gobierna la región» por «el movimiento que controla la región», o por «el antiguo partido gobernante de Tigray, la región».
- [ ] **Bloqueante.** «En el vecino Sudán, Etiopía y Eritrea respaldan a bandos opuestos de la guerra civil…»
  - **Buscar:** texto no localizado; ninguna fuente del informe lo dice. La cita de Boswell solo habla de la cercanía de Eritrea con el ejército sudanés y del deterioro de las relaciones de Etiopía con ese ejército.
  - **Si se confirma:** nada (anota la fuente).
  - **Si no se confirma:** apoyarse solo en Boswell: cambiar «respaldan a bandos opuestos de la guerra civil» por «tienen relaciones divergentes con el ejército, en plena guerra civil».
- [ ] **Bloqueante.** «…y eso podría convertir el choque en un conflicto mucho más amplio, a las puertas de un mar Rojo ya tensado por lo que ocurre en el estrecho de Bab el-Mandeb.»
  - **Buscar:** texto no localizado. Es voz de la autora, no de Boswell ni de ninguna fuente, y va pegada a su cita; el verificador apunta a la guerra de EE UU e Israel con Irán.
  - **Si se confirma** (tienes una fuente que dice qué ocurre en el estrecho): nombrarlo y atribuirlo.
  - **Si no se confirma:** cambiar «a las puertas de un mar Rojo ya tensado por lo que ocurre en el estrecho de Bab el-Mandeb» por «a las puertas del mar Rojo y del estrecho de Bab el-Mandeb».
  - **En ambos casos:** poner punto tras «International Crisis Group» («… Crisis Group. Eso podría convertir…») para que no parezca de Boswell.

### 8. The Reporter
<https://www.thereporterethiopia.com/53061/>
El verificador asocia esta pieza al discurso de Taye en la 81.ª Asamblea General de la ONU. Comprueba si también cuenta el aislamiento de Tigray; si eso viene de otra pieza, aporta el enlace.

- [ ] **Bloqueante.** «Internet y las líneas móviles están cortadas y las carreteras que unen la región con el resto del país se han cerrado al tráfico, informa The Reporter, que describe una escasez aguda de productos básicos.»
  - **Buscar:** texto no localizado (nadie ha leído la pieza).
  - **Si se confirma:** nada.
  - **Si no se confirma:** si confirmas lo de Reuters (sección 6), sustituir por «Internet y las líneas móviles están cortadas, informa Reuters, que describe compras de pánico». Si tampoco, suprimir la frase.
- [ ] «…y que persigue “todas las vías diplomáticas posibles” para lograrlo, recoge The Reporter.»
  - **Buscar:** "is pursuing all possible diplomatic avenues to secure access to and from the sea" (el verificador no pudo ver si va entre comillas).
  - **Si se confirma** (entre comillas y como palabras de Taye): nada.
  - **Si no se confirma:** quitar las comillas: «…y que persigue todas las vías diplomáticas posibles para lograrlo, recoge The Reporter.»

### 9. Al Jazeera, 23-sep: la alianza de siete grupos (fuente del verificador)
Sin URL en el informe. Titular: "Can Ethiopia's seven-group rebel alliance challenge Abiy Ahmed?"

- [ ] **Bloqueante.** «…para derrocar al primer ministro de Etiopía Abiy Ahmed…»
  - **Buscar:** texto no localizado: nadie ha visto el objetivo declarado de la alianza.
  - **Si se confirma:** nada.
  - **Si no se confirma:** cambiar «para derrocar al primer ministro de Etiopía Abiy Ahmed» por «contra el Gobierno del primer ministro de Etiopía, Abiy Ahmed».
- [ ] «…anunció una alianza con otros seis grupos armados…»
  - **Buscar:** "Ethiopian People's Forces Alliance for Survival" y "armed and political groups". Son siete miembros: TPLF, AFNM-Fano, OLA, ONLF, ARDUF, BPLM y Gumuz People's Democratic Movement.
  - **Si se confirma:** nada.
  - **Si no se confirma** (dice "armed and political groups", como anotó el verificador): cambiar «grupos armados» por «grupos armados y políticos».

### 10. The East African Daily (fuente del verificador)
El informe solo da el dominio, theeastafricandaily.com, sin URL del artículo. Busca allí la noticia de la alianza del 20-sep.

- [ ] **Bloqueante.** «…según reporta The East African.»
  - **Buscar:** texto no localizado en The East African (Nation Media). El verificador solo encontró la noticia en The East African Daily, que es otro medio, y en Al Jazeera (sección 9).
  - **Si se confirma** (la leíste en The East African y aportas el enlace, que no está en tu lista): nada.
  - **Si no se confirma:** cambiar «según reporta The East African» por «según informa Al Jazeera», o por «según informa The East African Daily» si fue ahí.

## B. Confirmaciones rutinarias

### 11. Al Jazeera, 19-sep: sanciones a Eritrea
<https://www.aljazeera.com/news/2026/9/19/us-lifts-sanctions-on-eritrea-imposed-during-conflict-in-ethiopias-tigray>

- [ ] «…y no renovó las sanciones contra Eritrea.»
  - **Buscar:** "to advance US regional interests" (la justificación del Departamento de Estado que cita Al Jazeera). Según el verificador, la OFAC retiró además de su lista de sancionados a las Fuerzas de Defensa de Eritrea y al PFDJ.
  - **Si se confirma:** nada. Es más preciso «y dejó expirar las sanciones contra Eritrea».
  - **Si no se confirma** (otra fecha): cambiar «y no renovó las sanciones contra Eritrea» por «y, por las mismas fechas, dejó expirar las sanciones contra Eritrea».

### 12. Reuters, 23-sep: análisis sobre Assab (fuente del verificador)
Sin URL en el informe. Titular: "Why new war in Ethiopia's Tigray threatens to trigger wider conflict" (el verificador usó el espejo de US News).

- [ ] «Addis Abeba reclama, en efecto, acceso al puerto y en Eritrea temen que intente tomarlo por la fuerza, según un análisis de Reuters que publica The East African.»
  - **Buscar:** "Addis Ababa has repeatedly argued that restoring access to the sea – specifically the port of Assab – is vital… Asmara has said it fears Addis Ababa will try to take Assab by force."
  - **Si se confirma** (y lo leíste en The East African, con enlace): nada.
  - **Si no se confirma:** quitar «que publica The East African»: «…, según un análisis de Reuters.»

### 13. Al Jazeera, 23-sep: vuelos a Tigray
<https://www.aljazeera.com/news/2026/9/23/ethiopian-airlines-suspends-flights-to-three-northern-tigray-airports>

- [ ] «El 23 de septiembre las fuerzas de Tigray tomaron los aeropuertos de Mekelle, Axum y Shire…»
  - **Buscar:** "seized control of three airports" (el verificador lo vio en Reuters, no aquí). En esta pieza debería estar que Ethiopian Airlines suspendió los vuelos a esos tres aeropuertos; el verificador lo da por correcto sin copiar el inglés. Comprueba los nombres y si la toma se da como hecho o como afirmación del TPLF.
  - **Si se confirma:** nada. Puede añadirse la suspensión de vuelos, como propone el verificador.
  - **Si no se confirma:** si es una afirmación del TPLF, «las fuerzas de Tigray aseguraron haber tomado los aeropuertos…». Si no aparece la toma: «El 23 de septiembre, Ethiopian Airlines suspendió los vuelos a tres aeropuertos de Tigray, y los combates se extendieron…».

### 14. Al Jazeera, 29-sep: lo último
<https://www.aljazeera.com/news/2026/9/29/fighting-in-ethiopia-intensifies-whats-the-latest>

- [ ] «El TPLF sostiene estar librando una “guerra defensiva” que responde a un ataque con drones orquestado por Addis Abeba.»
  - **Buscar:** el informe no copia el inglés, pero lo da por correcto (declaración del 23-sep). Busca *defensive war* y el ataque con drones, aquí o en la pieza del 23-sep, y de paso confirma que los combates se extendieron a Afar y Amhara.
  - **Si se confirma:** nada.
  - **Si no se confirma:** sustituir por «El TPLF sostiene que responde a un ataque con drones que atribuye a Addis Abeba.»

### 15. Al Jazeera: Alan Boswell (el informe lo fecha el 23-sep sin decir en qué pieza)
Busca en la pieza de vuelos (sección 13) y en la de la alianza (sección 9); si no está, en la del 29-sep.

- [ ] «“Eritrea también mantiene una relación bastante estrecha [...] con el ejército sudanés, y las relaciones entre Etiopía y el ejército sudanés también se han ido deteriorando” explica en Al Jazeera Alan Boswell…»
  - **Buscar:** "Eritrea is also quite close, for instance, with the Sudanese army, and relations between Ethiopia and the Sudanese army have also been deteriorating." Su cargo (director para el Cuerno de África del International Crisis Group): texto no localizado.
  - **Si se confirma:** nada; el [...] solo omite "for instance".
  - **Si no se confirma:** pasar la cita a estilo indirecto sin salir de la frase: cambiar desde «“Eritrea también…» hasta «…Crisis Group,» por «según explica en Al Jazeera Alan Boswell, director para el Cuerno de África del International Crisis Group, Eritrea está bastante próxima al ejército sudanés y las relaciones de Etiopía con ese ejército se han ido deteriorando,».
- [ ] «Para Boswell, todo está convirtiéndose en un único gran embrollo regional que “puede ponerse muy, muy feo si no hay desescalada”.»
  - **Buscar:** "this is all becoming one big regional mess, and it could get very, very ugly if we don't see de-escalation."
  - **Si se confirma:** nada; «podría ponerse» es más fiel a "could".
  - **Si no se confirma:** quitar las comillas: «…un único gran embrollo regional que podría ponerse muy feo si no hay desescalada.»

### 16. BBC
<https://www.bbc.com/news/articles/c6d94wywx0ypo>

- [ ] «El TPLF nació en los años setenta como guerrilla contra la junta militar y dominó la política etíope durante casi tres décadas, hasta la llegada al poder de Abiy en 2018, repasa la BBC.»
  - **Buscar:** texto no localizado (la página de la BBC no se pudo leer). Los datos coinciden con otras fuentes: 27 años de dominio, hasta 2018.
  - **Si se confirma:** nada.
  - **Si no se confirma:** quitar «, repasa la BBC»; son datos de dominio público.

### 17. Dato sin fuente enlazada: la población

- [ ] «…de un país de casi 140 millones de habitantes…»
  - **Buscar:** texto no localizado. Mira la estimación actual de la ONU; el verificador da entre 130 y 135 millones.
  - **Si se confirma** (la ONU ronda los 140): nada.
  - **Si no se confirma:** cambiar «casi 140 millones» por «más de 130 millones».

## Si no puedes comprobarlo a tiempo

Aplica la alternativa de los 16 bloqueantes, eligiendo siempre la opción más prudente, y además:
- **Quita:** la cita del Tesoro (déjala en estilo indirecto), «Fue una coincidencia curiosa», la frase de Debretsion, «se sintió traicionado… explica The Economist», «, repasa la BBC» y «que publica The East African».
- **Pasa a estilo indirecto:** la cita de Birhanu Jula, las dos de Weldiya (el verificador las leyó en la traducción de Infobae) y las «vías diplomáticas» de Taye.
- **Cambia dentro de la frase:** «alcanzó… la sede» → «quedó fuera de antena tras un ataque con dron»; «anexionar» → «reclama una salida al mar por la costa eritrea»; «para derrocar» → «contra el Gobierno»; The East African → Al Jazeera; «unos 600.000… Unión Africana» → «cientos de miles de muertos»; The Reporter → Reuters, sin carreteras ni escasez; «el partido que gobierna» → «el movimiento que controla»; «bandos opuestos» → la versión de Boswell; Bab el-Mandeb → «a las puertas del mar Rojo y del estrecho de Bab el-Mandeb», con punto tras «Crisis Group»; «casi 140» → «más de 130 millones».
- **No añadas** quién ordenó el corte de internet ni la fecha del ataque a Tigrai TV. Las citas de Boswell (con «podría») y del periodista de la AFP pueden quedarse: el verificador vio el inglés literal.
