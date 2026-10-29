# Método de revisión de artículos (página de Internacional)

Cuando la autora pasa un texto para revisar:

1. Guardarlo tal cual como `nombre.md` en la raíz (titular con `# `, subtítulo en `**…**`, ladillos con `## `), hacer commit y subirlo a la rama.
2. Lanzar cinco agentes: cuatro revisores en paralelo y el redactor jefe cuando terminen.
   - **Ortografía y ortotipografía**: tildes, mayúsculas, comas, comillas, cursivas.
   - **Sintaxis y concordancia**: errores gramaticales, régimen, ambigüedades, calcos.
   - **Verificación de citas y fuentes**: cada cita entre comillas y cada dato atribuido, contra la fuente original (los enlaces que pase la autora, reenviados al agente en cuanto lleguen); veredicto por punto y texto original.
   - **Formato y estilo**: verbos de atribución, repeticiones, claridad, valoraciones sin atribuir. Máximo 15 puntos.
   - **Redactor jefe**: lee los cuatro informes, arbitra y da el veredicto (APROBADO / APROBADO CON CAMBIOS / NO APROBADO).
3. Entregar un **Word con control de cambios sobre el texto original** y comentarios al margen, más el informe breve del redactor jefe (`informe_redactor_jefe_<pieza>.md`). Comprobar que, rechazando todos los cambios, sale exactamente el original.

## Reglas innegociables

- **La estructura es una plantilla fija**: titular, subtítulo, ladillos y orden de los párrafos no se mueven, no se fusionan y no se reescriben. Como mucho, una coma o una cursiva. Nunca reestructurar.
- Consigna de la autora: «corrige ortografía, no cambies párrafos y, si hay algo de discordancia, arréglalo pero señálalo».
- **Cambio marcado** (mínimo, dentro de la frase) solo para: ortografía, puntuación y ortotipografía; errores gramaticales claros; discordancias con la fuente cuando el verificador da el dato correcto con base razonable.
- **Solo comentario**, sin tocar el texto: lo que no se haya podido verificar (no se borra: la autora puede tener la fuente), sugerencias de estilo y todo lo que afecte a titular, subtítulo o ladillos.

## Comprobaciones obligatorias del redactor jefe

0. **Estilo en la primera entrega**: el informe dice cuántas frases pasan de 30 palabras en el original y en la corregida (debe ser 0 en la corregida), y confirma que no quedan dos puntos fuera de una enumeración ni comas antes de «y» entre oraciones.
0b. **Estructura clara para el lector, desde la primera entrega**: el texto tiene que entenderse a la primera. El redactor jefe lo comprueba siempre, aunque la autora no lo pida:
   - un tema o un actor por bloque (por ejemplo, todo lo de la federación junto y todo lo de Rusia junto), sin ir y volver entre ellos;
   - la tesis en el primer o segundo párrafo, dicha en una frase;
   - cada dato una sola vez (si aparece en dos párrafos, se queda donde explica algo y se quita del otro);
   - la misma fórmula de enlace no se repite («A esa debilidad se suma…», «A la exclusión se suma…»);
   - cada escándalo, cifra o cita con su fuente y sin mezclar dos casos parecidos (dopaje de un Estado frente a corrupción de una federación).
   Si la estructura falla, se entrega ya la propuesta de reorganización completa, sin esperar a que la autora la pida.
1. **Raccord**: que nadie ni nada aparezca como ya presentado sin haberlo sido. Por ejemplo: persona citada solo por el apellido o por el cargo en su primera aparición; «el embajador», «la ministra», «el diario» sin presentar; siglas sin desarrollar (WSJ); pronombres y posesivos sin antecedente («lo», «su», «esos mismos»); cargos o grafías que cambian entre párrafos; datos que se contradicen entre el subtítulo y el cuerpo o entre párrafos.
2. **Porcentaje de citas**: las palabras entre comillas deben ser **entre el 15 % y el 20 %** del cuerpo del texto (sin titular, subtítulo ni ladillos). Se calcula con el script, no a ojo:

   ```
   python3 herramientas/porcentaje_citas.py nombre.md
   ```

   Va en el informe del redactor jefe, sobre el original y sobre la versión corregida. Si queda fuera del margen, se dice cuántas palabras faltan o sobran y se proponen en comentarios qué paráfrasis podrían ser citas literales (o al revés), sin cambiar la estructura.
3. **Extensión**: el cuerpo no puede pasar de **900 palabras** (el mismo script lo mide). Si se pasa, el redactor jefe propone recortes de frases o incisos como borrados marcados, cada uno con un comentario «Recorte propuesto (−N palabras)», sin eliminar párrafos ni ladillos. La versión con todos los cambios aceptados debe cumplir a la vez el límite de palabras y el 15–20 % de citas. Para subir el porcentaje, una paráfrasis solo se convierte en cita literal si el verificador aporta la frase original.

## Redacción (lo vigila el revisor de estilo y lo comprueba el redactor jefe)

**La primera versión corregida ya tiene que salir en el estilo de la página.** La autora no debe tener que pedir después, párrafo a párrafo, que se acorten frases o se quiten dos puntos. El revisor de estilo y el redactor jefe aplican estas pautas en la primera entrega.

- Frases cortas: sujeto, verbo y predicado. Nada de oraciones de cuatro o cinco líneas encadenando subordinadas. **Ninguna frase del cuerpo pasa de 30 palabras** en la versión corregida. Se comprueba con el script, sobre el original y sobre la corregida:

  ```
  python3 herramientas/frases_largas.py nombre.md
  ```

  Cada frase larga se parte, en principio, con un cambio marcado mínimo dentro del mismo párrafo: un punto en lugar de una coma o de una «y», y un conector si hace falta. Puede haber excepciones. Si un párrafo solo funciona reescribiéndolo o reordenando sus ideas, se hace como cambio marcado y con un comentario que explique por qué. Nunca se tocan el titular, el subtítulo, los ladillos ni el orden de los párrafos.
- No abusar de la «y» para unir oraciones, ni de la coma antes de «y»; mejor punto y seguido.
- Evitar las enumeraciones de tres elementos como recurso fijo.
- Que cada idea se enlace con la anterior con un conector claro (por eso, sin embargo, además…) y que el párrafo siga una lógica. Repertorio por función en `herramientas/conectores.md` (según el *Diccionario de conectores y operadores del español* de Catalina Fuentes); variar los conectores y evitar los coloquiales.
- Dos puntos **solo para introducir una enumeración**. No se usan para explicar, encadenar ideas ni introducir citas; la cita va con el verbo de atribución detrás o con «que».
- No trocear el texto en frases telegráficas: es un texto periodístico, no una lista de ladillos desarrollados. Las frases cortas se enlazan con conectores o con una subordinada breve.
- Ninguna valoración sin atribuir (p. ej. «algo que no parece probable»): solo hechos o juicios con fuente.
- Modelo de escritura: las piezas de *El País* resumidas en `herramientas/modelo_el_pais.md` (entrada con gancho y cierre que vuelve a ella, conectores intercalados, citas largas, verbos de atribución variados, contexto en incisos breves).
- Si la autora pasa un artículo de base para inspirarse, el ángulo se busca con el método de `herramientas/metodo_angulo.md`: el dato que cambia, por qué ahora, la escala europea, hechos de fuentes locales y voces del artículo de base, la reacción y el cierre con la cita más fuerte.
- Si la autora pide reestructurar un párrafo concreto, se hace aunque la plantilla sea fija, sin cambiar la extensión ni el porcentaje de citas.

## Criterios de la casa

Referencia general: **Libro de estilo de *El País***, que es el que sigue la redacción. Donde el periódico se aparta de él, mandan los criterios de abajo, sacados de lo que publica.

- Cursiva para periódicos, revistas y digitales; redonda para agencias, cadenas, instituciones y partidos.
- Los medios se citan siempre con su nombre completo (*The Wall Street Journal*, nunca WSJ); las cadenas con siglas se desarrollan en la primera mención (SRF, ZDF…).
- Comillas latinas « »; “ ” solo dentro de otra cita. Los incisos dentro de una cita van entre rayas: «Irlanda ha hecho el diagnóstico correcto –apunta–, pero…».
- Punto en los millares (5.000); porcentaje **sin espacio** (16%).
- «ex» unido a una sola palabra (exoficial, exdiputado) y separado ante expresiones de varias (ex primer ministro).
- Nombres de guerras con mayúscula (Segunda Guerra Mundial).
- Subtítulos y ladillos sin punto final.
- Primera mención de cada persona con nombre completo y cargo; cargos en minúscula.
- «el mismo periódico» o «el diario» solo si el antecedente inmediato es ese medio.
- Nombres rusos y ucranianos: transcripción al español según la Fundéu (Volodímir Zelenski, Serhí, Andrí Yermak, Kiev), no la transliteración inglesa.

## Trato con la autora

- No contestar «tienes razón» ni dar la razón de palabra: aplicar la corrección, anotar la lección aquí o en `herramientas/` y que no se repita.
