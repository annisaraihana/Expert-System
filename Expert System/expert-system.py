from experta import *

diseases_list = []
diseases_symptoms = []
symptom_map = {}
d_desc_map = {}
d_treatment_map = {}

def preprocess():
    global diseases_list,diseases_symptoms,symptom_map,d_desc_map,d_treatment_map
    diseases = open("diseases.txt")
    diseases_t = diseases.read()
    diseases_list = diseases_t.split("\n")
    diseases.close()
    for disease in diseases_list:
        disease_s_file = open("Disease symptoms/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        s_list = disease_s_data.split("\n")
        diseases_symptoms.append(s_list)
        symptom_map[str(s_list)] = disease
        disease_s_file.close()
        disease_s_file = open("Disease descriptions/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        d_desc_map[disease] = disease_s_data
        disease_s_file.close()
        disease_s_file = open("Disease treatments/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        d_treatment_map[disease] = disease_s_data
        disease_s_file.close()
        
def identify_disease(*arguments):
    symptom_list = []
    for symptom in arguments:
        symptom_list.append(symptom)
    # Handle key error
    return symptom_map[str(symptom_list)]

def get_details(disease):
    return d_desc_map[disease]

def get_treatments(disease):
    return d_treatment_map[disease]

def if_not_matched(disease):
        print("")
        id_disease = disease
        disease_details = get_details(id_disease)
        treatments = get_treatments(id_disease)
        print("")
        print("Penyakit yang mungkin anda alami adalah %s\n" %(id_disease))
        print("Deskripsi singkatnya sebagai berikut :\n")
        print(disease_details+"\n")
        print("Cara pengobatan : \n")
        print(treatments+"\n")
    
class Greetings(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        print("")
        print("Hi! Saya asisten kesehatan kehamilan anda. Saya di sini untuk membantu mengecek kondisi anda.")
        print("Untuk itu anda perlu menjawab beberapa pertanyaan dengan yes atau no.")
        print("Apakah anda merasakan gejala:")
        print("")
        yield Fact(action="find_disease")
        
    @Rule(Fact(action='find_disease'), NOT(Fact(mual=W())),salience = 1)
    def symptom_0(self):
        self.declare(Fact(mual=input("mual: ")))

    @Rule(Fact(action='find_disease'), NOT(Fact(muntah=W())),salience = 1)
    def symptom_1(self):
        self.declare(Fact(muntah=input("muntah: ")))

    @Rule(Fact(action='find_disease'), NOT(Fact(mudah_lelah=W())),salience = 1)
    def symptom_2(self):
        self.declare(Fact(mudah_lelah=input("mudah lelah: ")))

    @Rule(Fact(action='find_disease'), NOT(Fact(pusing=W())),salience = 1)
    def symptom_3(self):
        self.declare(Fact(pusing=input("pusing: ")))

    @Rule(Fact(action='find_disease'), NOT(Fact(sesak_napas=W())),salience = 1)
    def symptom_4(self):
        self.declare(Fact(sesak_napas=input("sesak napas: ")))

    @Rule(Fact(action='find_disease'), NOT(Fact(tekanan_darah_naik=W())),salience = 1)
    def symptom_5(self):
        self.declare(Fact(tekanan_darah_naik=input("tekanan darah naik: ")))

    @Rule(Fact(action='find_disease'), NOT(Fact(wajah_pucat=W())),salience = 1)
    def symptom_6(self):
        self.declare(Fact(wajah_pucat=input("wajah pucat: ")))

    @Rule(Fact(action='find_disease'), NOT(Fact(bercak_darah=W())),salience = 1)
    def symptom_7(self):
        self.declare(Fact(bercak_darah=input("bercak darah: ")))

    @Rule(Fact(action='find_disease'), NOT(Fact(nyeri_bahu=W())),salience = 1)
    def symptom_8(self):
        self.declare(Fact(nyeri_bahu=input("nyeri bahu dan seluruh bagian perut: ")))

    @Rule(Fact(action='find_disease'), NOT(Fact(mata_berkunang=W())),salience = 1)
    def symptom_9(self):
        self.declare(Fact(mata_berkunang=input("mata berkunang-kunang: ")))

    @Rule(Fact(action='find_disease'), NOT(Fact(hilang_nafsu_makan=W())),salience = 1)
    def symptom_10(self):
        self.declare(Fact(hilang_nafsu_makan=input("hilang nafsu makan: ")))

    @Rule(Fact(action='find_disease'), NOT(Fact(demam=W())),salience = 1)
    def symptom_11(self):
        self.declare(Fact(demam=input("demam: ")))

    @Rule(Fact(action='find_disease'), NOT(Fact(leher_bengkak=W())),salience = 1)
    def symptom_12(self):
        self.declare(Fact(leher_bengkak=input("leher belakang bengkak: ")))

    @Rule(Fact(action='find_disease'), NOT(Fact(nyeri_otot=W())),salience = 1)
    def symptom_13(self):
        self.declare(Fact(headache=input("nyeri otot: ")))

    @Rule(Fact(action='find_disease'), NOT(Fact(ruam_wajah=W())),salience = 1)
    def symptom_14(self):
        self.declare(Fact(ruam_wajah=input("ruam di wajah: ")))

    @Rule(Fact(action='find_disease'), NOT(Fact(gatal=W())),salience = 1)
    def symptom_15(self):
        self.declare(Fact(gatal=input("gatal: ")))

    @Rule(Fact(action='find_disease'), NOT(Fact(kulit_mengelupas=W())),salience = 1)
    def symptom_16(self):
        self.declare(Fact(kulit_mengelupas=input("kulit mengelupas halus: ")))

    @Rule(Fact(action='find_disease'),Fact(mual="yes"),Fact(muntah="yes"),Fact(mudah_lelah="yes"),Fact(pusing="yes"),Fact(sesak_napas="yes"),Fact(tekanan_darah_naik="yes"),Fact(wajah_pucat="yes"),Fact(bercak_darah="yes"),Fact(nyeri_bahu="yes"),Fact(mata_berkunang="no"),Fact(hilang_nafsu_makan="no"),Fact(demam="no"),Fact(leher_bengkak="no"),Fact(nyeri_otot="no"),Fact(ruam_wajah="no"),Fact(gatal="no"),Fact(kulit_mengelupas="no"))
    def disease_0(self):
            self.declare(Fact(disease="Kehamilan Ektopik"))
    
    @Rule(Fact(action='find_disease'),Fact(mual="yes"),Fact(muntah="yes"),Fact(mudah_lelah="yes"),Fact(pusing="yes"),Fact(sesak_napas="yes"),Fact(tekanan_darah_naik="yes"),Fact(wajah_pucat="yes"),Fact(bercak_darah="yes"),Fact(nyeri_bahu="no"),Fact(mata_berkunang="yes"),Fact(hilang_nafsu_makan="yes"),Fact(demam="no"),Fact(leher_bengkak="no"),Fact(nyeri_otot="no"),Fact(ruam_wajah="no"),Fact(gatal="no"),Fact(kulit_mengelupas="no"))
    def disease_1(self):
            self.declare(Fact(disease="Anemia Kehamilan"))
    
    @Rule(Fact(action='find_disease'),Fact(mual="yes"),Fact(muntah="yes"),Fact(mudah_lelah="yes"),Fact(pusing="yes"),Fact(sesak_napas="no"),Fact(tekanan_darah_naik="no"),Fact(wajah_pucat="no"),Fact(bercak_darah="no"),Fact(nyeri_bahu="no"),Fact(mata_berkunang="no"),Fact(hilang_nafsu_makan="no"),Fact(demam="yes"),Fact(leher_bengkak="yes"),Fact(nyeri_otot="yes"),Fact(ruam_wajah="no"),Fact(gatal="no"),Fact(kulit_mengelupas="no"))
    def disease_2(self):
            self.declare(Fact(disease="Toxoplamosis"))
            
    @Rule(Fact(action='find_disease'),Fact(mual="yes"),Fact(muntah="yes"),Fact(mudah_lelah="yes"),Fact(pusing="yes"),Fact(sesak_napas="no"),Fact(tekanan_darah_naik="no"),Fact(wajah_pucat="no"),Fact(bercak_darah="no"),Fact(nyeri_bahu="no"),Fact(mata_berkunang="no"),Fact(hilang_nafsu_makan="no"),Fact(demam="yes"),Fact(leher_bengkak="yes"),Fact(nyeri_otot="no"),Fact(ruam_wajah="yes"),Fact(gatal="yes"),Fact(kulit_mengelupas="yes"))
    def disease_3(self):
            self.declare(Fact(disease="Rubella"))
    
    @Rule(Fact(action='find_disease'),Fact(disease=MATCH.disease),salience = -998)
    def disease(self, disease):
        print("")
        id_disease = disease
        disease_details = get_details(id_disease)
        treatments = get_treatments(id_disease)
        print("")
        print("Penyakit yang mungkin anda alami adalah %s\n" %(id_disease))
        print("Dengan deskripsi singkat sebagai berikut :\n")
        print(disease_details+"\n")
        print("Cara pengobatan : \n")
        print(treatments+"\n")
        
    @Rule(Fact(action='find_disease'),
          Fact(mual=MATCH.mual),
          Fact(muntah=MATCH.muntah),
          Fact(mudah_lelah=MATCH.mudah_lelah),
          Fact(pusing=MATCH.pusing),
          Fact(sesak_napas=MATCH.sesak_napas),
          Fact(tekanan_darah_naik=MATCH.tekanan_darah_naik),
          Fact(wajah_pucat=MATCH.wajah_pucat),
          Fact(bercak_darah=MATCH.bercak_darah),
          Fact(nyeri_bahu=MATCH.nyeri_bahu),
          Fact(mata_berkunang=MATCH.mata_berkunang),
          Fact(hilang_nafsu_makan=MATCH.hilang_nafsu_makan),
          Fact(demam=MATCH.demam),
          Fact(leher_bengkak=MATCH.leher_bengkak),
          Fact(nyeri_otot=MATCH.nyeri_otot),
          Fact(ruam_wajah=MATCH.ruam_wajah),
          Fact(gatal=MATCH.gatal),
          Fact(kulit_mengelupas=MATCH.kulit_mengelupas),NOT(Fact(disease=MATCH.disease)),salience = -999)
          
    def not_matched(self,mual, muntah, mudah_lelah, pusing, sesak_napas, tekanan_darah_naik, wajah_pucat, bercak_darah, nyeri_bahu, mata_berkunang, hilang_nafsu_makan, demam, leher_bengkak, nyeri_otot, ruam_wajah, gatal, kulit_mengelupas):
        print("\nTidak menemukan penyakit yang sesuai dengan gejala anda")
        lis = [mual, muntah, mudah_lelah, pusing, sesak_napas, tekanan_darah_naik, wajah_pucat, bercak_darah, nyeri_bahu, mata_berkunang, hilang_nafsu_makan, demam, leher_bengkak, nyeri_otot, ruam_wajah, gatal, kulit_mengelupas]
        max_count = 0
        max_disease = ""
        for key,val in symptom_map.items():
            count = 0
            temp_list = eval(key)
            for j in range(0,len(lis)):
                if(temp_list[j] == lis[j] and lis[j] == "yes"):
                    count = count + 1
            if count > max_count:
                max_count = count
                max_disease = val
        if_not_matched(max_disease)
        
if __name__ == "__main__":
    preprocess()
    engine = Greetings()
    while(1):
        engine.reset()  # Prepare the engine for the execution.
        engine.run()  # Run it!
        print("Apakah anda ingin mendiagnosis gejala lainnya?")
        if input() == "no":
            exit()
        
