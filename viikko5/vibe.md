### Raportti Copilotin tuottamasta websovelluksesta

Pyysin Copilotia tekemään ohtuvaraston lähdetiedostoista varastosovelluksen, jossa käyttäjä pystyi luomaan ja muokkaamaan useita varastoja, lisäämään niihin tuotteita sekä hallitsemaan varastojen kapasiteettia.
Ensimmäisen version tekeminen kesti Copilotilla 53 minuuttia. Sovellus toimi suhteellisen hyvin ja käyttöliittymä oli selkeä. Huomasin kuitenkin joitakin käytettävyyteen ja ohjelmalogiikkaan liittyviä puutteita.

Tämän jälkeen pyysin Copilotia tekemään joitakin muutoksia parilla erillisellä kierroksella. Copilot toteutti muutokset yleensä noin 10 minuutissa.

* Varastoilla piti olla uniikit nimet.
* Varaston kapasiteettia ei saanut pienentää alle nykyisen saldon.
* Varaston sisältöä ja kapasiteettia pystyisi hallinnoimaan samalla sivulla. Lisäksi halusin, että käyttäjän lisäämät tiedot tallennetaan paikalliseen sql-tietokantaan ja tyylit viedään erilliseen css-tiedostoon.
* Etusivun nappien ulkoasuun ja sijaintiin tuli tehdä muutoksia, joita ei ollut aiemmissa Copilotin tuottamissa versioissa.
* Käyttäjä pystyy luomaan hedelmävaraston lisäksi oman (custom) varaston ja lisätä sinne haluamiaan tuotteita.

Copilotin tuottama koodi oli pääosin selkeää ja ymmärrettävää. Yksittäisiä havaintoja tein, miten esimerkiksi url_for-metodia voisi käyttää websovelluksessa.
Html:ään liittyvä kooodia oli paljon ja tyyliin liittyen oli paljon uusia yksityiskohtia. Toisaalta Copilot tuotti koodia runsaasti, minkä vuoksi kokonaisuuden hahmottaminen ei ollut kovin helppoa tai nopeaa.

Koodin mergeämisen jälkeen huomasin vielä Pylint-testien läpimenemisessä puutteita, joita pyysin Copilotia vielä korjaamaan lopuksi.
Lisäksi pyysin Copilotia vielä tekemään yksikkötestejä uusille tiedostoille, jotta testikattavuus olisi 100 %.

Yhteenvetona voi todeta, että Copilot onnistui tuottamaan suht lyhyessä ajassa toimivantuntuisen websovelluksen käyttöliittymän. Toisaalta sovelluksen generointi Copilotin avulla opetti myös, miten tärkeää on muotoilla muokkaustarpeet mahdollisimman kattavasti. Oli myös hyödyllistä huomata, että Copilot saattaa muokata jo toimivalta näyttäviä asioita, joita täytyy pyytää korjaamaan.
