OFFSETER 4 MA2 developed by Szymon Płotkowski
szymonplotkowski@gmail.com

OPIS:
Program porównuje dwa pliki presetów pozycji z gma2 i na podstawie różnic w wartościach oblicza offsety dla poszczególnych Fix. ID. 
Następnie Tworzy Macro, które uruchomione w stole, automatycznie przypisuje wartości offsetów do lamp.
W większości wypadków, użycie tego programu zrzuca z Ciebie mozolny obowiązek poprawiania wszystkich pozycji. 
Wystarczy poprawić jedną pozycję, a pozostałe staną się z automatu użyteczne, lub w najgorszym wypadku staną się dobrą bazą pod upiększanie. 
Dlaczego napisałem to, zamiast korzystać ze stage calibration? SC jest dużo bardziej skomplikowanym mechanizmem. Nierzadko wykrzaczającym deskę. By zadziałało należy stworzyć 4 pozycje i znać koordynaty punktów, w krórych umiejscawiamy pozycje.
Mój program w odróżnieniu do SC działa jedynie w 2 wymiarach i nie uwzględnia rotacji w osiach, ale w zamian za to jest szybszy (jedna poprawiana pozycja zamiast 4) i stabilniejszy (jeśli coś się nie uda, to nie zawiesi Ci deski bo działa na kompie). 
Testy na żywym organiźmie polegające na przeniesieniu w rzeczywistość pozycji stworzonych w WYSIWYGu, przebiegły pomyślnie, tak więc częstujcie się wszyscy!
Im mniej czasu poświęconego na programowanie, tym więcej czasu na socjalizację ;)
 

INSTRUKCJA OBSŁUGI:
-Wyzeruj dotychczasowe offsety
-Zapimportuj do MA2 macro EXPORT 4 OFFSETER.xml dołączone z programem
-Wybierz preset pozycji, który posłuży za referencję (najlepsze są pozycje typu "center"/"wszystkie lampy w punkt". 
-Skopiuj wybrany wcześniej preset i popraw pozycje lamp, by wyglądały jak trzeba
-Podłącz PENDRIVE do stołu
-Uruchom macro EXPORT 4 OFFSETER
-Na PENDRIVE w folderze gma2\importexport pojawią się dwa pliki *.xml (wyg.xml oraz corrected.xml). W tym samym folderze umieść plik .exe załaczony w archiwum
-Uruchom plik .exe. W wyniku tego w folderze gma2/macros powstanie nowy plik Offsets.xml
-Zaimportuj plik Offsets.xml jako nowe macro
-Uruchom zaimportowane Macro. 


INFO O WERSJI:

V 2.3
- Przepisany moduł tworzenia macro z użyciem SPlib (przygotowanie do przenosin programu na MA3)

V 2.2
- Przepisany na nowo silnik parsowania presetów. 
- Usprawniona walidacja presetów. Stary silnik wykrzaczał się przy podaniu presetu zawierającego coś więcej niż wartości PAN i TILT dla urządzeń. Nowy moduł ignoruje dane o efekcie, delay i fade, jakie mogą być wpisane do presetu.
- Dodana ikona programu 
- Obniżona sygnatura wynikowych plików macro tak by można je było uruchamiać na konsolach z softem od 3.4.0 w górę

V 2.1
- Przepisany silnik porównania presetów źródłowych. Od teraz program sprawdza nie tylko ilość lamp w presecie, ale również ich ID i kolejność. Nie ma możliwości stworzenia macro, jeśli presety źródłowe stworzono dla innej selekcji fix.ID
- W razie niepowodzenia program powinien poinformować, dlaczego doszło do błędu
- Dodano informacje o autorze

V 2.0
- Automatyczne umiejscawianie wynikowego pliku macro w folderze gma2\macros

V 1.0
- Concept proof



Jeśli nie jesteś na mojej liście mailingowej, a chciałbyś otrzymywać informacje o update'ach pisanych przeze mnie programów,
wyslij mi mail na splotkowski@gbd.com.