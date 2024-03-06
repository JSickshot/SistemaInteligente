from deep_translator import GoogleTranslator
import gtts
import os

def translate_and_save(language_code):
    traducir_en = input('Escribe una frase: ')
    traducido = GoogleTranslator(source='auto', target=language_code).translate(traducir_en)
    print(traducido)
    tts = gtts.gTTS(traducido, lang=language_code)
    tts.save(f'{language_code}.mp3')
    os.system(f'{language_code}.mp3')

opcion = '0'
while opcion != '10':
    print(' 1. Español')
    print(' 2. Inglés')
    print(' 3. Francés')
    print(' 4. Portugués')
    print(' 5. Chino')
    print(' 6. Alemán')
    print(' 7. Italiano')
    print(' 8. Ruso')
    print(' 9. Japonés')
    print('10. Árabe')
    print(' 0. Salir')
    
    opcion = input('Elige el idioma al que deseas traducirlo y convertirlo a MP3: ')
    
    if opcion == '1':
        translate_and_save('es')
    elif opcion == '2':
        translate_and_save('en')
    elif opcion == '3':
        translate_and_save('fr')
    elif opcion == '4':
        translate_and_save('pt')
    elif opcion == '5':
        translate_and_save('zh')
    elif opcion == '6':
        translate_and_save('de')
    elif opcion == '7':
        translate_and_save('it')
    elif opcion == '8':
        translate_and_save('ru')
    elif opcion == '9':
        translate_and_save('ja')
    elif opcion == '10':
        translate_and_save('ar')
    elif opcion == '0':
        print('**** SALIENDO DEL MENÚ ')
    else:
        print('**** Opción no válida')
