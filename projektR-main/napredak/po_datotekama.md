# Promjene po datotekama

### DataHandler
Promjenile u konstruktorima obje klase da mode bude hardkodiran kao 'baseline'.
U create_train_val_test_ids promjenile dio s random.shuffle da ne vraća NoneType.
U create_train_val_test_ids popravile indekse za val_ids i test_ids liste da ne budu prazne.
Kod TrainCollector klase u get_loaders u else grani promjenile batch_Size u batch_size jer se tako zapravo zove atribut.

### ExtractFiles
Nismo ništa promjenile od ranijeg commita, ali je zanimljivo što se nekome stvori Pipeline direktorij unutar Pipeline direktorija, a nekome ne.

### Hyperparams
Smanjile max_epochs, batch_size, roi_size kako bismo mogle lakše pokrenuti dio s treniranjem. Smanjile smo max_epochs na 1 pa je prolazio korak treniranja, a onda smo povećali na 5 i dobili error u Logging datoteci.

### Inference
Promjenile da get_loaders() funkciju pozivamo nad instancom klase TestCollector, a ne InferenceLogger. Zakomentirale dio s transfer_strategy if-om i pomaknule ovo iz else da se izvrši uvijek. Promjenile path do modela da bude apsolutni.

### Logging
U log_tcs() funkciji zamijenili results_dict u results. U klasi ResultsLogger u funkciji save_info() privremeno stavili da printa varijablu results. Također smo do toga promjenili malo stvaranje DataFrame objekta po uputama iz linka u datoteci napredak.md. Promjenile da training_time : None bude training_time : [None], odnosno da bude lista kako bi se ona mogla proširiti s NaN elementima što je nužno da dio s DataFrame radi. Prekopirale save_info() i create...() iz ResultsLogger klase u InferenceLogger. U Logging u klasi InferenceLogger u njenom konstruktoru zamjenile redoslijed definiranja varijabli. Stavile self.random_seed u konstruktor. Definirale u rječniku fje populate_hyperparams() da postoji key-value par s random_seed.

### Plotting
Dodale mogućnost Plottinga iz results.csv datoteke.

### torchCUDA
Stvorile ovu malu skriptu za potrebe oslobađanja memorije na GPU i garbage collectiona.

### Train
Zakomentirale logger.log_results() unutar validacijskog koraka jer je javljalo da ne postoji ta fja. Nakon toga smo na mjestu te funkcije stavili funkciju logger.log_tcs() koja postoji.

### Training
Nismo ništa konkretno mijenjale, ali vidim da se jedino tu importa ResultPlotter iz Plotting datoteke, a nigdje se ne koristi :(
