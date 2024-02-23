### WORLD-DOMINATION

## Echipa:
* Diana Maria Stefan, Maria Cristina Costea, Stefan Valentin Ionescu, Marin Marius Daniel

## Aplicatie implementata:
* mini-joc in care concurezi cu un bot pentru a distruge navele adversarului primul

## Descriere aplicatie
* Mini-jocul porneste cu un meniu de start in care apare titlul jocului si in care se sugereaza ca jucatorul sa apese tasta `S` pentru a incepe. Se genereaza atat in harta ta (ce reprezinta o matrice de 10x10) cat si a botului 3 barci de dimensiuni diferite. Scopul jocului este de a fi primul care reuseste sa ghiceasca unde sunt pozitionate toate barcile adversarului. Astfel, este pus la dispozitie un "cursor" in forma de `X` ce poate fi miscat din sageti pentru alegerea pozitiei in care doresti sa lovesti, lovirea efectiva fiind actionata de butonul `X` de la tastatura. Dupa o miscare efectuata de tine botul genereaza o lovire pe harta. In functie de cine castiga (tu sau calculatorul), se afiseaza fereastra end_menu cu mesajul corespunzator. De asemenea, jocul contine si efecte sonore.

## Limbaje/ tehnologii folosite:
* libraria `pygame` pentru construirea efectiva a jocului
* libraria `random` pentru generarea mutarilor
* libraria `time` pentru sincronizarea actiunilor prin sleep uri

## Instructiuni rulare/folosire:
* pentru START, apasa tasta `S`
* pentru a misca CURSORUL, foloseste te de sageti
* pentru a lovi, apasa tasta `X`

## Contribuire membrii echipa:
* Diana Maria Stefan : construire initiala schema joc, reparare bug uri, curatare cod, alegere + editare imagini, creare fereastra start
* Maria Cristina Costea : descoperire bug uri, redimensionare barci, lovire barci, game-tester
* Stefan Valentin Ionescu : implementare bot, sincronizare + generare miscari
* Marin Marius Daniel : creare meniu start + final, alegere + editare sunete, pozitionare elemente in ferestre

## Dificultati:
* afisare animatii -> rezolvare prin suprapunere imagini redimensionate
* bug uri -> rezolvare naturala

## Demo:
https://github.com/Carusel02/Battleship-game/assets/40697296/1cad7984-bb64-4613-ac72-bdcdedb0d67b



