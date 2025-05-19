# 21.12.2022.

## Prvi pokušaj s Richterinim kodom

Neonatal kod je na laptopu, a ne na external disku jer su nas zezali permissions;
Promjenili path da pokazuje na external drive directories;
Pokrenuli ExtractFiles.py;
Bio error sa dijeljenjem stringova pa smo popravili to u kodu;
AssertionError se javlja, promjenili za sad ručno da mode bude baseline (inače je false iz nekog razloga);
id_list_shuffle = random.shuffle(id_list) promjenjeno da ne vraća NoneType u DataHandler.py line 95;
batch_Size promjenjeno u batch_size u DataHandler.py line 164; To smo zakomentirali nakon mijenjanja; Onda smo otkomentirali;

# 22.12.2022.

## Skinule svježu kopiju Richterinog repozitorija, sve ispod se odnosi na mijenjanje tog koda

Kreiran gitlab repo s drugom kopijom githuba od richterleo;
Napravljene izmjene u ExtractFiles.py za ručni unos puta do eksternog direktorija s izvornim podacima;

# 23.12.2022.

AssertionError se javlja, promjenili za sad ručno da mode bude baseline (inače je false iz nekog razloga) u DataHandler u konstruktorima obje klase;
id_list_shuffle = random.shuffle(id_list) promjenjeno da ne vraća NoneType u DataHandler.py line 95;
batch_Size promjenjeno u batch_size u DataHandler.py line 164;
treba izbrisati Ids da bi create_train_val_test_ids se izvršila;
Line 100 DataHandler.py: promjenili indekse lista tako da val_eval lista ne bude prazna;
pip3 install nibabel; (ovo zato što je u monai biblioteci došlo do interne pogreške zbog nemogućnosti čitanja arhivskih datoteka);
CUDA empty cache napravili malu skriptu s garbage collectorom i empty_cache;
batch size smanjili s 2 na 1;
epoch smanjili s 10 na 2;
roi_size smanjili s 256,256,256 na 64,64,64;
Line 163 Train.py: RADI JEDNA EPOHA, ali ResultsLogger nema atribut log_results. Ovo se pojavljuje samo kod validacije pa smo za sad to zakomentirale jer validacija nije nužan korak. Obje epohe sad rade i modeli su se spremili u rezultate;
Moramo skužiti još taj logging da bismo imali tri zadnje datoteke iz pipelinea u results poddirektorijima;
Napravljen .gitignore za pycache;

# 29.12.2022.

Otkomenirale logger.log_results() unutar validacijskog koraka u Train datoteci i zamjenile smo log_results s funkcijom log_tcs() jer nam se čini da će to popraviti "ValueError: All arrays must be of the same length"; U Logging promjenili u log_tcs() results_dict u results_dir; Ovo prijašnje nam je javljalo PosixPath error pa smo results_dir promjenili u results; Nakon ovog je Training ZAVRŠIO BEZ ERRORA; Ipak ne radi ako imamo više od jedne epohe, opet javlja "All arrays must be of the same length". To je zato što se u results rječnik zajedno s rezultatima epoha sprema i najbolji rezultat od tih epoha, što naravno nema jednak broj elemenata kao i ostatak rezultata; Popravile taj error s ovim linkom: https://stackoverflow.com/questions/40442014/python-pandas-valueerror-arrays-must-be-all-same-length ; Sad nam javlja "TypeError: object of type 'NoneType' has no len()"

# 30.12.2022.

U Logging promjenili da training_time : None bude training_time : [None]; Sada radi Training korak; U Logging prekopirale save_info() i create...() iz ResultsLogger klase u InferenceLogger; U Logging u klasi InferenceLogger u njenom konstruktoru zamjenile redoslijed definiranja varijabli; Stavili self.random_seed u konstruktor; Definirale u rječniku fje populate_hyperparams() da postoji key-value par s random_seed; U Inference promjenile da get_loaders() funkciju pozivamo nad instancom klase TestCollector, a ne InferenceLogger; U Inference zakomentirale dio s transfer_strategy if-om i pomaknule ovo iz else da se izvrši uvijek; Promjenile path do modela da bude apsolutni; U Logging u infer funkciji promjenile sw_batch_size iz 1 u 2, također batch_size u Hyperparams iz 1 u 2; Vratile smo oboje na 1 za sad;

# 10.01.2023.

Isprobale postaviti okolišnu varijablu za PyTorch alokaciju memorije putem export 'PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:512', isprobale vrijednosti 400, 512 i 700, ali svaki put dobivamo 'CUDA out of memory' error. Ista error se javlja i kod pokretanja Inference.py i kod SaveSegmentations.py, a u oba slučaja zapne na inferenceLogger.infer() dijelu pipelinea, kod sliding_window_inference; Stavile 10 epoha i pustile model da se trenira, uspio se istrenirati, spremili ga pod prvi_od_10_epoha; Istražile Kaggle;

# 18.01.2023.

Ostavile da se izvrti 50 epoha; Dodale mogućnost izrade grafova unosom results.csv datoteke (za sad hardkodirano); Generirale grafove za par iteracija izvršenog programskog toka; Završile većinu dokumentacije;

# 19.01.2023.

Promjenom parametra pixdim ustanovile da su rezultati programskog toka bolji pri većoj dimenziji piksela te smo ostavile da se s takvim hiperparametrima izvrti 50 epoha; Generirale grafove iz epoha koje su se odvrtile u prethodnom koraku; Napravile završne preinake na dokumentaciji;

# Napomena

Prije nego što smo pokrenule kod smo morale instalirati CUDA driver za Nvidia GPU kako bi se kod mogao izvoditi na njoj.

