# cianatex
Il mio preambolo per LaTeX, richiede TexLive 2024 perchè è basato su alcuni pacchetti molto fichi e moderni come [quiver](https://q.uiver.app/) (quindi se usate Linux con una distro basata su Debian come me, il comando ```sudo apt-get install texlive-full``` non va bene, in quanto vi carica TexLive 2022)

## Contenuti

Questo comprende tre pacchetti:

* ```cianatex.sty``` comprende i comandi di base e carica i pacchetti necessari per un dignitoso utilizzo del LaTeX.
* ```cianacolors.sty``` definisce i colori che poi verranno usati da ```cianatheorems.sty``` con due opzioni alternative: ```zun``` e ```depression```, rispettivamente per avere un azzurro molto soft e un grigio print-friendly come colori (anche se per ora sono un poco buggate, non usatele)
* ```cianatheorems.sty``` definisce gli ambienti dei teoremi et cetera: attenzione, la sintassi corretta è quella sotto: i campi possono essere lasciati in bianco ma vanno almeno incluse le ```{}```. L'opzione ```cianabook``` cambia la numerazione dei teoremi da interna alle sezioni a interna ai capitoli, l'opzione ```cianaenglish``` imposta i nomi in inglese.

### Esempio di sintassi del teorema
```
\begin{theorem}{Titolo del teorema}{tag del teorema}{
   [Enunciato del teorema]
   \proof (se volete generare il cartellino della dimostrazione) 
   [Dimostrazione del teorema]
   \qed
}
```

## Compilazione assistita

Per compilare includo il mio super-casalingo script ```compile.sh``` che va semplicemente chiamato nel terminale come ```./compile.sh FILENAME BIB``` e compila il file ```FILENAME.tex``` (e se ```BIB == yesbib``` allora compila pure ```FILENAME.bib```) un paio di volte per sopprimere gli errori.
