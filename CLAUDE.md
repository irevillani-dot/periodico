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

1. **Raccord**: que nadie ni nada aparezca como ya presentado sin haberlo sido. Por ejemplo: persona citada solo por el apellido o por el cargo en su primera aparición; «el embajador», «la ministra», «el diario» sin presentar; siglas sin desarrollar (WSJ); pronombres y posesivos sin antecedente («lo», «su», «esos mismos»); cargos o grafías que cambian entre párrafos; datos que se contradicen entre el subtítulo y el cuerpo o entre párrafos.
2. **Porcentaje de citas**: las palabras entre comillas deben ser **entre el 15 % y el 20 %** del cuerpo del texto (sin titular, subtítulo ni ladillos). Se calcula con el script, no a ojo:

   ```
   python3 herramientas/porcentaje_citas.py nombre.md
   ```

   Va en el informe del redactor jefe, sobre el original y sobre la versión corregida. Si queda fuera del margen, se dice cuántas palabras faltan o sobran y se proponen en comentarios qué paráfrasis podrían ser citas literales (o al revés), sin cambiar la estructura.

## Criterios de la casa

- Cursiva para periódicos, revistas y digitales; redonda para agencias, cadenas, instituciones y partidos.
- Comillas latinas « »; “ ” solo dentro de otra cita.
- Punto en los millares (5.000); espacio antes de % (16 %).
- Subtítulos y ladillos sin punto final.
- Primera mención de cada persona con su cargo; cargos en minúscula.
