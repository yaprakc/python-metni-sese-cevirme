import os
from gtts import gTTS

# kullanıcıdan metin
text = input("Lütfen sese dönüştürmek istediğiniz metni girin: ")

# metin ve dil seçeneği
voice = gTTS(text=text, lang="tr", slow=False)

#kaydedeceğimiz dosya yolu
saved_location = r"~~~"

# sesi kaydetme
voice.save(saved_location)

print(f"Başarılı! Ses dosyası klasöre kaydedildi.")
print(f"Dosya Konumu: {saved_location}")