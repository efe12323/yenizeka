import nltk

# Chatbot'un temel yanıtlarını içeren bir sözlük oluşturalım
responses = {
    "merhaba": "Merhaba! Nasıl yardımcı olabilirim?",
    "günaydın": "Günaydın! İyi günler dilerim.",
    "iyi akşamlar": "İyi akşamlar! İyi akşamlar dilerim.",
    "ne haber": "İyiyim, teşekkür ederim. Sen nasılsın?",
    "hoşçakal": "Hoşçakal! Görüşürüz.",
    "selam": "selam nasılsın?",
    "naber": "naber nasılsın?",
    "iyiyim": "çok mutlu oldum",
    "Nasılsın": "iyiyim sen.",
}


# Kullanıcı girişini alalım
user_input = input(">>> ")

# Kullanıcı girişini sözlükte arayalım
if user_input in responses:
    # Sözlükte varsa, temel yanıtı döndürelim
    print(responses[user_input])
else:
    # Sözlükte yoksa, rastgele bir yanıt döndürelim
    print(nltk.random.choice(responses.values()))
