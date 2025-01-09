# ENGLİSH

# AI HomePod

## Overview

AI HomePod is a voice-controlled assistant that offers a variety of functionalities such as setting alarms, adding events to a calendar, tracking the weather, running timers, and much more. The project integrates speech recognition and text-to-speech conversion, making it a comprehensive home assistant for everyday tasks.

## Features

- **Voice Commands**: Use natural language to interact with the HomePod for tasks such as adding events, checking the calendar, setting alarms, and checking the weather.
- **Text-to-Speech**: The assistant responds to commands and provides information using a high-quality speech synthesis engine.
- **Event Management**: Add, remove, and check events from a calendar.
- **Alarm System**: Set one-time or recurring alarms, and get reminders based on your preferences.
- **Weather Information**: Retrieve weather data based on the user’s location.
- **Timer and Stopwatch**: Start timers and stopwatches, with voice feedback.
- **Location Awareness**: Use IP-based geolocation to provide weather updates and location-based features.
- **Real-time Speech Recognition**: Continuous listening for commands, with support for voice commands and actions.

## Libraries Used

- `gTTS`: For converting text to speech.
- `pygame`: For playing audio files.
- `speech_recognition`: To capture and recognize speech commands.
- `requests`: For making HTTP requests to external APIs (e.g., weather, IP geolocation).
- `g4f.client`: For using AI-based responses.
- `cryptography`: For data encryption and decryption.
- `datetime`: To handle time-related functions.
- `json`: To manage event and alarm data.
- `threading`: To handle asynchronous tasks (e.g., alarms, timers).

## Installation

1. **Install dependencies**:
   To run this project, install the required Python libraries:

   ```bash
   pip install pyaudio speechrecognition gtts pygame requests cryptography numpy g4f
   ```

2. **Setup the API key**:
   You'll need to replace the placeholder for the OpenWeatherMap API key in the `hava_durumu()` function with your own API key.

   ```python
   api_key = "YOUR_OPENWEATHERMAP_API_KEY"
   ```

## Key Functions

### 1. `speak(text)`
Converts the given text to speech and plays it back to the user using the `gTTS` library.

### 2. `wake_up_sound()`
Listens for a specific volume threshold and activates listening for commands once detected.

### 3. `voice_listen()`
Captures audio and converts it into text using Google’s Speech-to-Text service.

### 4. `listen()`
Listens for a voice command and returns the text. It processes the speech input and sends it for command execution.

### 5. `add_event()`
Allows the user to add events to the calendar. The user can specify a date and description. The event is then saved to a `calendar` file.

### 6. `check_events()`
Checks the current day for events. If there's an event for today, it speaks the event description.

### 7. `set_alarm()`
Sets an alarm based on user input for the time and whether the alarm should repeat. The alarm information is saved to a file for later checks.

### 8. `get_greeting_message()`
Generates a greeting based on the time of day (morning, afternoon, or evening).

### 9. `alarm_thread()`
Runs in the background to check if any alarms are triggered and plays the alarm at the specified time.

### 10. `parse_duration(input_text)`
Converts natural language duration (e.g., "5 minutes", "30 seconds") into seconds.

### 11. `start_timer(duration)`
Starts a countdown timer based on the duration input by the user.

### 12. `start_stopwatch()`
Starts a stopwatch, providing real-time updates on elapsed time.

### 13. `stop_stopwatch()`
Stops the stopwatch and provides the final elapsed time.

### 14. `get_location_info()`
Retrieves the user's current location using IP geolocation.

### 15. `hava_durumu()`
Fetches the current weather information based on the user's location and provides details like temperature, humidity, and wind speed.

## File Structure

```
/AI_HomePod
  ├── main.py               # Main script to run the HomePod assistant
  ├── alarms.json           # Stores alarm data (time and repetition details)
  ├── calendar.json         # Stores calendar event data
  └── output.mp3            # Temporary file for audio output
```

## Usage

- **Activate the Assistant**: Once the HomePod is running, it will listen for specific voice commands such as:
  - "Set an alarm for 7:00 AM"
  - "What’s the weather like?"
  - "Add an event for tomorrow"
  - "Start a timer for 10 minutes"
- **Interacting with the Assistant**: Commands are recognized in Turkish, and responses are given in the same language.

## Future Improvements

- Integration with smart home devices (e.g., lights, thermostats).
- More accurate and robust voice recognition for various languages and accents.
- User authentication for personalized features.

---

This README provides a comprehensive overview of your AI HomePod, its functions, and how to use it. You can add more details based on specific features or updates you implement in the future!

# TÜRKÇE

# AI HomePod

## Genel Bakış

AI HomePod, alarm ayarlama, takvime etkinlik ekleme, hava durumunu takip etme, zamanlayıcıları çalıştırma ve çok daha fazlası gibi çeşitli işlevler sunan, ses kontrollü bir asistandır. Proje, konuşma tanıma ve metinden konuşmaya dönüştürmeyi entegre ederek onu günlük görevler için kapsamlı bir ev asistanı haline getiriyor.

## Özellikler

- **Sesli Komutlar**: Etkinlik ekleme, takvimi kontrol etme, alarm ayarlama ve hava durumunu kontrol etme gibi görevler için HomePod ile etkileşimde bulunmak üzere doğal dili kullanın.
- **Metin-Konuşma**: Asistan, yüksek kaliteli bir konuşma sentezi motorunu kullanarak komutlara yanıt verir ve bilgi sağlar.
- **Etkinlik Yönetimi**: Bir takvime etkinlik ekleyin, kaldırın ve kontrol edin.
- **Alarm Sistemi**: Tek seferlik veya yinelenen alarmlar ayarlayın ve tercihlerinize göre hatırlatıcılar alın.
- **Hava Durumu Bilgileri**: Kullanıcının konumuna göre hava durumu verilerini alın.
- **Zamanlayıcı ve Kronometre**: Sesli geri bildirimle zamanlayıcıları ve kronometreleri başlatın.
- **Konum Farkındalığı**: Hava durumu güncellemeleri ve konum tabanlı özellikler sağlamak için IP tabanlı coğrafi konumu kullanın.
- **Gerçek Zamanlı Konuşma Tanıma**: Sesli komutlar ve eylemler desteğiyle komutları sürekli dinleme.

## Kullanılan Kütüphaneler

- `gTTS`: Metni konuşmaya dönüştürmek için.
- `pygame`: Ses dosyalarını oynatmak için.
- `speech_recognition`: Konuşma komutlarını yakalamak ve tanımak için.
- `istekler`: Harici API'lere (ör. hava durumu, IP coğrafi konumu) HTTP istekleri yapmak için.
- `g4f.client`: Yapay zeka tabanlı yanıtların kullanılması için.
- `cryptograph`: Veri şifreleme ve şifre çözme için.
- `datetime`: Zamanla ilgili işlevleri yönetmek için.
- `json`: Olay ve alarm verilerini yönetmek için.
- 'threading': Eşzamansız görevleri (ör. alarmlar, zamanlayıcılar) yönetmek için.

## Kurulum

1. **Bağımlılıkları yükleyin**:
   Bu projeyi çalıştırmak için gerekli Python kitaplıklarını yükleyin:

   ``` bash
   pip install pyaudio speechrecognition gtts pygame requests cryptography numpy g4f
   ''''

2. **API anahtarını kurun**:
   'hava_durumu()' işlevindeki OpenWeatherMap API anahtarının yer tutucusunu kendi API anahtarınızla değiştirmeniz gerekecektir.

   ```piton
   api_key = "SİZİN_AÇIKWEATHERMAP_API_ANAHTARINIZ"
   ''''

## Tuş İşlevleri

### 1. `konuş(metin)`
Verilen metni konuşmaya dönüştürür ve 'gTTS' kütüphanesini kullanarak kullanıcıya oynatır.

### 2. `wake_up_sound()`
Belirli bir ses düzeyi eşiğini dinler ve algılandıktan sonra komutların dinlenmesini etkinleştirir.

### 3. `voice_listen()`
Sesi yakalar ve Google'ın Konuşmadan Metne Dönüştürme hizmetini kullanarak metne dönüştürür.

### 4. `dinle()`
Sesli komutu dinler ve metni döndürür. Konuşma girişini işler ve komutun yürütülmesi için gönderir.

### 5. `add_event()`
Kullanıcının takvime etkinlik eklemesine olanak tanır. Kullanıcı bir tarih ve açıklama belirleyebilir. Etkinlik daha sonra bir 'takvim' dosyasına kaydedilir.

### 6. `check_events()`
Etkinlikler için geçerli günü kontrol eder. Bugün için bir etkinlik varsa, etkinlik açıklamasını konuşur.

### 7. `alarm_ayar()`
Zaman için kullanıcı girişine ve alarmın tekrarlanıp tekrarlanmayacağına bağlı olarak bir alarm ayarlar. Alarm bilgileri daha sonraki kontroller için bir dosyaya kaydedilir.

### 8. `get_greeting_message()`
Günün saatine (sabah, öğleden sonra veya akşam) göre bir karşılama mesajı oluşturur.

### 9. `alarm_thread()`
Herhangi bir alarmın tetiklenip tetiklenmediğini kontrol etmek için arka planda çalışır ve belirlenen saatte alarmı çalar.

### 10. `ayrıştırma_süresi(giriş_metni)`
Doğal dil süresini (ör. "5 dakika", "30 saniye") saniyeye dönüştürür.

### 11. `başlangıç_zamanlayıcısı(süre)`
Kullanıcının girdiği süreye göre bir geri sayım sayacı başlatır.

### 12. `start_stopwatch()`
Geçen süreye ilişkin gerçek zamanlı güncellemeler sağlayan bir kronometreyi başlatır.

### 13. `stop_stopwatch()`
Kronometreyi durdurur ve geçen son süreyi gösterir.

### 14. `get_location_info()`
IP coğrafi konumunu kullanarak kullanıcının mevcut konumunu alır.

### 15. `hava_durumu()`
Kullanıcının konumuna göre mevcut hava durumu bilgilerinai getirir ve sıcaklık, nem ve rüzgar hızı gibi ayrıntıları sağlar.

## Dosya Yapısı

''''
/AI_HomePod
  ├── main.py # HomePod asistanını çalıştırmak için ana komut dosyası
  ├── alarms.json # Alarm verilerini saklar (zaman ve tekrar ayrıntıları)
  ├── takvim.json # Takvim etkinliği verilerini saklar
  └── çıktı.mp3 # Ses çıkışı için geçici dosya
''''

## Kullanım

- **Asistan'ı etkinleştirin**: HomePod çalıştığında aşağıdakiler gibi belirli sesli komutları dinleyecektir:
  - "Sabah 7:00'ye alarm kur"
  - "Hava nasıl?"
  - "Yarın için bir etkinlik ekle"
  - "10 dakikalık bir zamanlayıcı başlat"
- **Asistan ile Etkileşim**: Komutlar Türkçe olarak tanınır ve yanıtlar aynı dilde verilir.

## Gelecekteki İyileştirmeler

- Akıllı ev cihazlarıyla entegrasyon (örn. ışıklar, termostatlar).
- Çeşitli diller ve aksanlar için daha doğru ve sağlam ses tanıma.
- Kişiselleştirilmiş özellikler için kullanıcı kimlik doğrulaması.

---

Bu README, AI HomePod'unuza, işlevlerine ve nasıl kullanılacağına ilişkin kapsamlı bir genel bakış sağlar. Gelecekte uygulayacağınız belirli özelliklere veya güncellemelere göre daha fazla ayrıntı ekleyebilirsiniz!
