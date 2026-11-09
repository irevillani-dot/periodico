# Informe del redactor jefe: «Arrancan las quinielas para el próximo presidente de EE. UU., con Ossoff como favorito»

**Veredicto: APROBADO CON CAMBIOS.** La pieza cumple lo pedido por Mario y por la autora y, con los cambios aceptados, respeta las comprobaciones de la casa. No debe publicarse sin resolver tres cosas: la cita de Costa y el dato de Kalshi tras las elecciones (no verificados) y el desajuste «favorito» / «lidera las apuestas» del titular y el subtítulo.

Entregable: `ossoff_2028_corregido.docx` (34 cambios marcados, 68 comentarios). Al rechazar todos los cambios sale exactamente el original; al aceptarlos, la versión corregida. Supera `validate.py`.

## 0. Estilo de la primera entrega

- Frases de más de 30 palabras: **0 en el original y 0 en la corregida**. La más larga de la corregida (Wasserman con la atribución a El País) tiene 29 palabras tras un ajuste mínimo («no crecerán» por «no ampliarán su dominio»).
- Dos puntos fuera de una enumeración: **ninguno** en el cuerpo. Los de la cita de Costa son del autor citado.
- Comas antes de «y» entre oraciones: **ninguna**. Se ha corregido la de «un trumpista, y Ossoff despegó». Queda una coma antes de «y recuperaron» en el párrafo 3: cierra el inciso «que dejó el vicepresidente J. D. Vance» y une dos predicados del mismo sujeto, no dos oraciones.
- «Por eso»: de cuatro quedan dos, ambos con causa real. Párrafo 2: la propia frase de El País enlaza documentalista y conciencia de la imagen. Párrafo 8: el titular del Journal dice que la derrota complica el cálculo de Vance. Se han cambiado el del párrafo 4 («Ahora») y el del 7 («Además»), que no expresaban causa.

## 1. Raccord

Arreglado con cambio marcado:
- *The Wall Street Journal* completo en la primera mención (párrafo 3); después, «el *Journal*».
- Obama, «el expresidente», en la primera mención; se quita la repetición final.
- Ossoff, «senador», en el párrafo 1.
- Donald Trump, «el presidente», en el párrafo 4.
- Ocasio-Cortez, «la congresista».
- Elaine Luria, «la demócrata».
- Kemp, «gobernador saliente»: el párrafo 3 dice que los demócratas recuperaron Georgia, así que no podía seguir sin matiz.
- «Estos distritos» en la cita de Luria pasa a «estos distritos disputados», como en el Times.
- Elecciones: «legislativas».

DeSantis, Rubio, Cruz y Kemp ya salían presentados con cargo. «El diario» no aparece. No quedan siglas sin desarrollar. Pendiente, solo comentario: Trump sin nombre en el subtítulo (aceptable) y Cruz sin «por Texas».

## 2. Palabras y porcentaje de citas (`herramientas/porcentaje_citas.py`)

| | Cuerpo | Entre comillas | % | Frases >30 |
|---|---|---|---|---|
| Original | 896 | 164 | 18,3% | 0 |
| Corregida (todo aceptado) | 895 | 166 | 18,5% | 0 |

Las incorporaciones de raccord y de aclaración suman unas 30 palabras. Se compensan con cinco recortes marcados y rechazables, cada uno con su comentario «Recorte propuesto»:
- «ante 10.000 personas» (−3), porque la autora pidió pocas cifras.
- Segunda atribución a El País en el párrafo 4 (−3).
- «recuperar la confianza en el Gobierno» y la enumeración de tres promesas (−6).
- «Pero su ventaja se estrecha» (−5, redundante con la frase siguiente).
- Y la última frase del balance, «será una carrera generacional… *millennials*» (−13, sin atribuir y sin preparar).

Si la autora rechaza recortes, el cuerpo sube: con todos los cambios y sin el recorte de las 10.000 personas queda en 899; sin el de los *millennials*, en 907 (por encima del límite). Las citas se mantienen entre 18,3% y 18,5%.

## 3. Estructura frente a lo pedido

- **Mario:** Ossoff primero, después los demás aspirantes demócratas y, por último, Vance y los republicanos. Se cumple. El titular tiene el tono «quinielas» pedido.
- **Autora:** abre con Obama y Ossoff con las mangas enrolladas (sí), Ossoff documentalista (sí, párrafo 2), coste de la vida y «populistas pragmáticos» explicados (sí, con cambios en el párrafo 6: «Hablaron del coste de la vida» y «cercanos a la gente y con medidas posibles»), pocas cifras (sí; se propone quitar la de 10.000 personas) y «Dos partidos, dos resacas» como cierre (se mantiene el ladillo; el párrafo es un balance y termina con Costa).
- **Debilidades, solo comentario y con coste en palabras:**
  1. Las quinielas no aparecen hasta el párrafo 4. Un puente al final del párrafo 2 costaría ~+15 palabras (citas ~18,2%). Con la apertura que pidió la autora, lo razonable es que el titular haga de gancho.
  2. «Esa imagen funcionó en una noche histórica» insinúa una causa y no tiene atribución. Alternativa de +7 palabras con la causa del triunfo (moderados y coste de la vida).
  3. La cita de Obama queda sin oración principal. El País la completa: «Solo hay una opción sensata en esta batalla electoral, y ese es Jon Ossoff…». Cuesta +14 (+19 con «tan apuesto en los vídeos») y subiría las citas a ~20%, al límite.
  4. El cierre con Costa no vuelve al gancho. Una frase final con Ossoff costaría +12; no se aplica por indicación de la autora.

## 4. Verificación: qué se ha corregido y qué no

**Corregido con base en la fuente:**
- Cita de Obama: «solamente» y punto y coma, como en El País.
- Cita de El País: «es *perfectamente* consciente».
- «Seis años de mandato» es de El País, no del Journal.
- La enumeración «guerra de Irán, aranceles, coste de la vida» no es de El País: se corta la frase para que el «según» cubra solo la cita.
- Wasserman es de El País, no del Times: se añade la atribución.
- DeSantis: «antes visto como halcón» y «pide límites estrictos a los centros de datos» (The Washington Post).
- «Estos distritos disputados» (Times).
- Régimen de «escaños en el Senado», coma de «el de Ohio, que dejó», ambigüedad de «y con republicanos», complemento de «culpa… de la derrota», *caucus* en cursiva.

**NO VERIFICADO (solo comentario, no se borra):**
- La reflexión del péndulo de Francesco Costa y su cargo (director de *Il Post*). Es traducción del italiano.
- Kalshi para Rubio y DeSantis «tras las elecciones»: los datos de Kalshi que se localizan son del 4 de noviembre, anteriores a los comicios.

**Matices sin cambio, para la autora:**
- Kemp, Cruz, DeSantis y Vander Plaats salen del Post, con fuentes anónimas, y el texto no lo cita. Atribuirlo costaría +4.
- Cruz: el Post dice «si entra en la carrera».
- Vance «asegura»: lo dijo a su entorno, no en público.
- Donantes: lo cuenta un recaudador, de segunda mano.
- Buttigieg: «decenas» (el Journal habla de 102 candidatos).
- La primaria «será» abierta: el Journal dice «se espera».
- «Lastró al rival»: El País dice que lastró su campaña de primarias.

## 5. Titular, subtítulo y ladillos (no se tocan)

- **Titular y subtítulo:** «favorito» y «lidera las apuestas» sobrepasan el cuerpo. El País sí dice que las casas de apuestas «empiezan a colocarle como favorito», pero el texto solo recoge que Kalshi lo pone por delante de Ocasio-Cortez, que Harris lidera los sondeos y que Vance lidera las apuestas republicanas. Alternativas: «…con Ossoff entre los favoritos» y «Jon Ossoff gana terreno en las apuestas» (o «encabeza las apuestas demócratas», solo si lo confirma Kalshi).
- **Subtítulo:** «ganaron con candidatos moderados» → «sobre todo con moderados» (el Times dice «sobre todo»).
- **Ladillos:** correctos y sin punto final.

## 6. Decisiones que quedan para la autora

1. Titular y subtítulo: elegir una de las alternativas de la sección 5.
2. Enlace o original italiano de Costa. Sin él, la cita sigue sin verificar.
3. Enlace de Kalshi con datos posteriores a las elecciones (Rubio y DeSantis). Sin él, valorar quitar «tras las elecciones».
4. Si añade «según *The Washington Post*» a DeSantis, Kemp y Cruz (+4 palabras; hay que recortar otras).
5. Si acepta los recortes (especialmente las 10.000 personas y los *millennials*) o prefiere otros.
6. Si completa la cita de Obama (+14/+19 palabras).
7. Enlace original del Journal con las declaraciones de Vance «a su entorno» y de Beshear (entrevista), si quiere precisar «asegura».
