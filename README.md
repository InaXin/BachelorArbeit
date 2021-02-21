# BachelorArbeit
1	Technische Anforderungen
1.1	IDE: PyCharm (Python 3.8)
1.2	ChromeDriver installieren
1.2.1	In diesem Programm ist die Version von ChromeDriver nun 88.0.4324.96
1.2.2	auf der Webseite https://chromedriver.chromium.org/downloads herunterladen
1.3	MySQL Workbench installieren
2	Bedienungsprozess
2.1	Web Scraping
2.1.1	Run Python Datei „SubAndProductCategoryHtmlCatch.py”, wird eine Excel-Datei mit alle Kategorien Links von Idealo erhaltet  „Daten_Html/IdealoProductCategoryHtml.xlsx“
2.1.2	Run Python Datei „ExcelHtmlClassify.py”, wird diese Excel-Datei in drei Excel-Datei klassifiziert  
Unterkategorien-Links: „Daten_Html/SubProductCategoryHtml.xlsx“
Produkt-Links: „Daten_Html/ProductCategoryHtml.xlsx“
Nutzlose Links: „Daten_Html/Plane&HotelHtml.xlsx“
2.1.3	Run Python Datei „ExcelToSubExcel.py”, um Unterkategorien Links in drei Excel-Dateien zu unterteilen 
„Daten_Html/SubProductCategoryHtml (1-30).xlsx”
“Daten_Html/SubProductCategoryHtml (31-60).xlsx”
„Daten_Html/SubProductCategoryHtml (61-70).xlsx“
2.1.4	Run Python Datei „SubProductCategoryToProductCategoryCatch.py”, um die Produkt Links aus Unterkategorien zu erhalten.
„Daten_Html/SubProductCategory (1-30) ToProductCategoryHtml.xlsx”
„Daten_Html/SubProductCategory (31-60) ToProductCategoryHtml.xlsx”
„Daten_Html/SubProductCategory (61-70) ToProductCategoryHtml.xlsx”
2.1.5	Run Python Datei „ExcelConcat.py”, um alle Produkt Links in einer Excel-Datei zusammenzufügen 
„Daten_Html/AllProductCategoryHtml.xlsx“
2.1.6	Run Python Datei „ExcelHtmlDropDuplicates.py“, um duplizierte Produkt Links zu löschen. (Jede Link enthält erste 36 Produkte)  
„Daten_Html/AllProductCategoryHtmlDropDuplicates.xlsx“
2.1.7	Optionale Schritt: Run Python Datei „PageTurning.py“, um die anderen Produkte zu bekommen.
2.1.8	Run Python Datei „ExcelToSubExcel.py”, um Produkt-Links in 21 Excel-Dateien zu unterteilen. 
„Daten_Html/AllProductCategoryHtmlDropDuplicates(1-100).xlsx“
…
„Daten_Html/AllProductCategoryHtmlDropDuplicates(2001-2011).xlsx“
2.1.9	Run Python Datei „ProductInfoCatch.py“ 
In diesem Schritt werden gewünschte Produktinformationen wie Produkt-ID, Produkt-Name und Kategorien erhalten und in JSON-Datei gespeichert. 
„Daten_Json/AllProductCategoryHtmlDropDuplicates(1-100)ToProductsInfo.json”
…
„Daten_Json/AllProductCategoryHtmlDropDuplicates(2001-2011)ToProductsInfo.json“
2.2	MySQL-Datenbank
2.2.1	Run Python Datei „DataCleaning.py“, um ungültige Daten zu bereinigen. 
„Daten_Json_Clean/ProductsInfo(1-100).json”
……
„Daten_Json_Clean/ProductsInfo(2001-2011).json”
2.2.2	Run Python Datei „JsonToExcel.py“, um JSON-Datei in Excel-Datei zu formatieren. 
„Daten/Json(ProductsInfo(1-100))ToExcel.xlsx”
……
„Daten/Json(ProductsInfo(2001-2011))ToExcel.xlsx“
2.2.3	Run Python Datei „DatabaseProcessor.py“, um Produktinformationen und Produktpreis in Datenbank einzufügen.


Run „main.py“, werden Preisänderung von gewünschter Kategorie in ausgewähltem Zeitraum, Trend, Analyse nach Saisonalitäten und Sondereffekten sowie Prognose in einer eingestellten Periode erhalten.
