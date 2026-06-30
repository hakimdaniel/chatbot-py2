import random

dataset = {
    "nama":[
        "Nama saya HilmBot.",
        "Saya HilmBot.",
        "Boleh panggil saya HilmBot je."
    ],
    "developer":[
        "Daniel Hakim yang cipta saya.",
        "Saya dicipta oleh Daniel Hakim.",
        "Daniel Hakim adalah Developer saya."        
    ],
    "error":[
        "Jika ada sebarang masalah, hubungi developer di telegram https://t.me@d4n13lh4k1m",
        "Contact Daniel Hakim di teleram https://t.me@d4n13lh4k1m",
        "Dm developer di teleram https://t.me@d4n13lh4k1m untuk pertanyaan."
    ],
    "else":[
        "Maaf saya tak faham.",
        "Saya tak faham ayat ni, cuba ayat lain.",
        "Saya tak faham apa yang dikatakan, cuba ayat lain."
    ]
}

while True:
    soalan = input("Soalan: ")
    test = soalan.lower().split(" ")

    if "nama" in test and "kamu" in test:
        print(f"Bot: {dataset['nama'][random.randint(0,2)]}")
    elif ("siapa" in test and "developer" in test) or ("cipta" in test):
        print(f"Bot: {dataset['developer'][random.randint(0,2)]}")
    elif "error" in test or "masalah" in test:
        print(f"Bot: {dataset['error'][random.randint(0,2)]}")        
    else:
        print(f"Bot: {dataset['else'][random.randint(0,2)]}")
