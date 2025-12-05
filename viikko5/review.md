## Review

Copilot teki katselmoinnin pull requestiin liittyen tennispelin luokan TennisGame koodin refaktorointiin.

Coplit antoi koodista kolme kommenttia, joista ensimmäinen liittyi yhden metodin sisällä määriteltävään muuttujaan (sanakirjaan)
tennispelin pisteistä (”Love”, ”Fifteen”, ”Thirty”, ”Forty”). Copilot ehdotti, että metodin sisällä olevaa sanakirjaa pisteiden
nimistä muodostettaisiin metodin ulkopuolella. Sinänsä hyvä ehdotus ei näyttäisi kuitenkaan suoraan toimivan, vaan sanakirja tulisi määritellä
esim. luokkamuuttujana. Toisaalta ehdotus sanakirjan nimestä `scores` to `score_names` oli ihan hyvä parannus, joka kuvaa muuttujan sisältöä paremmin.

Kommenteista kaksi liittyi luokat TennisGame metodien yksityistämiseen. Copilot perusteli, että se selkiyttää, kun toteutuksen yksityiskohdat
eivät ole tarkoitettu ulkoiseen käyttöön.

Copilotin tekemät ehdotukset olivat ihan hyviä ja yleisesti ottaen katselmointi hyödyllistä. Copilot voi huomata asioita,
joita ei itse ole huomannut. Mahdollisia korjausehdotuksia olisi voinut odottaa enemmänkin. Tämän perusteella on vaikea arvioida,
miten ”tyhjentävästi” Copilot antoi tässä muutosehdotuksia, miten paljon koodissa voisi olla vielä parannettavaa ja miten isoja muutoksia
Copilot kykenee ehdottamaan. Esimerkiksi Copilotin ehdotukset liittyivät lopulta suht pieniin yksityiskohtiin. Lisäksi suht lyhyenkin koodin katselmointiin
kului suhteellisen paljon aikaa. Tämän pohjalta voisi ajatella, että Copilotin tekemä katselmointi on ihan hyvä työkalu,
mutta pelkästään sen tekemän arvion varaan ei välttämättä uskaltaisi tuudittautua.
