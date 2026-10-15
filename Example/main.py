import os
from gtts import gTTS

# kullanıcıdan metin alma
text = input("Lütfen sese dönüştürmek istediğiniz metni girin: ")

# metin ve dil secenegi
voice = gTTS(text=text, lang="tr", slow=False)

#kaydedecegimiz dosya yolu
saved_location = r"~~~"

# sesi kaydet
voice.save(saved_location)

print(f"Başarılı! Ses dosyası klasöre kaydedildi.")
print(f"Dosya Konumu: {saved_location}")
