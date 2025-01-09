import random, re, pyaudio, threading, json, datetime, time, os, pygame
from cryptography.fernet import Fernet
import numpy as np
import speech_recognition as sr
from g4f.client import Client
from gtts import gTTS
import requests

# G4F API istemcisi ayarı
client = Client()

def speak(text):
    """Verilen metni seslendir."""
    # gTTS ile metni ses dosyasına çevir
    tts = gTTS(text=text, lang='tr')
    filename = "output.mp3"
    tts.save(filename)
    
    # pygame ile sesi çal
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    
    # Ses bitene kadar bekle
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(100)
    
    # Geçici dosyayı sil
    pygame.mixer.music.unload()
    os.remove(filename)
    
def wake_up_sound():
    try:
        aktif = False  # Başlangıçta aktif durum False
        while True:
            if not aktif:  # Sadece aktif değilse mikrofon dinlenir
                # Mikrofon verisini okuma
                data = np.frombuffer(stream.read(CHUNK, exception_on_overflow=False), dtype=np.int16)
                volume = np.linalg.norm(data)  # Ses seviyesi hesapla
                print(f"Ses seviyesi: {volume}")

                # Ses seviyesi eşikten büyükse dinlemeye başla
                if volume > THRESHOLD:
                    aktif = True  # Dinleme aktif hale gelir
                    print("Ses algılandı, dinlemeye başlıyorum...")
                    voice_listen()  # Dinlemeyi başlat
                    aktif = False  # Dinleme tamamlandıktan sonra tekrar pasif hale döner
            else:
                # `aktif` True iken hiçbir işlem yapılmaz
                pass
            
    except Exception as e:
        print(f"Hata: {str(e)}")

def voice_listen():
        try:
            bip()
            with sr.Microphone() as source:
                audio = recognizer.listen(source, timeout=7, phrase_time_limit=7)
                
                # Ses kaydını metne çevir
                text = recognizer.recognize_google(audio, language='tr-TR')
                text = text.lower()
                print(f"Bunu duydum: {text}")
                
                execute_command(text)
                    
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass
        except sr.WaitTimeoutError:
            pass
        except Exception:
            pass

def listen():
        try:
            bip()
            with sr.Microphone() as source:
                audio = recognizer.listen(source, timeout=7, phrase_time_limit=7)
                
                # Ses kaydını metne çevir
                text = recognizer.recognize_google(audio, language='tr-TR')
                text = text.lower()
                print(f"Bunu duydum: {text}")
                
                return text
                    
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass
        except sr.WaitTimeoutError:
            pass
        except Exception:
            pass
        
# Ay isimlerini Türkçe'den İngilizce'ye çeviren fonksiyon
def convert_month_to_english(date_input):
    turkish_to_english_months = {
        'Ocak': 'January', 'Şubat': 'February', 'Mart': 'March',
        'Nisan': 'April', 'Mayıs': 'May', 'Haziran': 'June',
        'Temmuz': 'July', 'Ağustos': 'August', 'Eylül': 'September',
        'Ekim': 'October', 'Kasım': 'November', 'Aralık': 'December'
    }
    
    for turkish, english in turkish_to_english_months.items():
        if turkish in date_input:
            return date_input.replace(turkish, english)
    return date_input        

# Etkinlik ekleme fonksiyonu
def add_event():
    speak("Tarih söyleyin (örneğin 15 Şubat):")
    date_input = listen().strip()

    speak("Açıklamayı söyleyin:")
    description = listen().strip()

    # Türkçe ay adını İngilizce'ye çevir
    date_input_converted = convert_month_to_english(date_input)

    speak("Açıklamayı söyleyin:")
    description = listen().strip()

    if date_input in calendar:
        speak("Bu tarihte başka bir etkinlik bulunmaktadır.")
        return
    
    try:
        # Tarihi doğrula
        datetime.datetime.strptime(date_input_converted, '%d %B')
        calendar[date_input] = description
        with open(calendar_file, 'w') as file:
            json.dump(calendar, file)
        speak(f"Etkinlik '{description}' {date_input} tarihinde kaydedildi.")
    except ValueError:
        speak("Geçersiz tarih formatı. Lütfen 'gün ay' formatında girin.")

# Günün etkinliklerini kontrol eden fonksiyon
def check_events():
    today = datetime.now().strftime('%d %B')
    if today in calendar:
        speak(f"Bugün {today}. {calendar[today]}")
    else:
        speak("Bugün için bir etkinlik yok.")
        
# Alarm fonksiyonu
def set_alarm():
    speak("Alarm saati girin (örneğin 14:30):")
    alarm_time_input = listen().strip()

    # Kullanıcı girdisindeki '.' yerine ':' koy
    alarm_time_input = alarm_time_input.replace('.', ':')

    try:
        alarm_time = datetime.datetime.strptime(alarm_time_input, '%H:%M')
        speak("Alarmın bir seferlik mi, her gün mü, hafta içi mi yoksa hafta sonu mu çalmasını istersiniz?")
        repeat_option = listen().strip().lower()

        alarm_info = {
            'alarm_time': alarm_time.strftime('%H:%M'),
            'repeat_option': repeat_option
        }

        # Alarmları dosyaya ekle
        try:
            with open('alarms.json', 'r') as file:
                alarms_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            alarms_data = {"alarmlar": []}

        alarms_data["alarmlar"].append(alarm_info)

        with open('alarms.json', 'w') as file:
            json.dump(alarms_data, file, indent=4)

        speak(f"Alarm saat {alarm_time_input} olarak ayarlandı. Tekrar edilme seçeneği: {repeat_option}")
    except ValueError:
        speak("Geçersiz saat formatı. Lütfen 'saat:dakika' formatında girin.")

# Alarm kontrol fonksiyonu
def get_greeting_message():
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        speak(f"Günaydın {data['ad']}.")
    elif 12 <= current_hour < 20:
        speak(f"İyi günler {data['ad']}.")
    else:
        speak(f"İyi geceler {data['ad']}.")

def alarm_thread():
    while True:
        current_time = datetime.datetime.now()
        try:
            # Alarm dosyasını oku
            with open('alarms.json', 'r') as file:
                alarm_list = json.load(file).get("alarmlar", [])

            for alarm in alarm_list[:]:  # Listeyi kopyalayarak iterasyon yap
                alarm_time = datetime.datetime.strptime(alarm['alarm_time'], '%H:%M')
                repeat_option = alarm.get('repeat_option', 'bir seferlik')

                # Alarmın belirtilen saatte mi olduğunu kontrol et
                if current_time.hour == alarm_time.hour and current_time.minute == alarm_time.minute:
                    get_greeting_message()
                    speak(f"Alarm çaldı: {alarm['alarm_time']} - {repeat_option}")

                    # Tekrar seçeneğine göre işlem yap
                    if repeat_option == 'bir seferlik':
                        alarm_list.remove(alarm)  # Alarmı kaldır
                    elif repeat_option == 'hafta içi' and current_time.weekday() >= 5:  # Cumartesi-Pazar
                        continue
                    elif repeat_option == 'hafta sonu' and current_time.weekday() < 5:  # Pazartesi-Cuma
                        continue

            # Güncellenmiş alarm listesini kaydet
            with open('alarms.json', 'w') as file:
                json.dump({"alarmlar": alarm_list}, file, indent=4)

        except FileNotFoundError:
            print("Alarm dosyası bulunamadı.")
        except json.JSONDecodeError:
            print("Alarm bilgileri hatalı.")
        except Exception as e:
            print(f"Hata: {e}")
        
        time.sleep(30)  # 30 saniyede bir kontrol et

def parse_duration(input_text):
    """Kullanıcıdan gelen süre bilgisini doğal dilde çözümleyip saniyeye çevirir."""
    duration_regex = r"(\d+)\s*(saniye|dakika)?"
    matches = re.findall(duration_regex, input_text)

    total_seconds = 0
    for value, unit in matches:
        value = int(value)
        if unit in ["dakika", "minute"]:
            total_seconds += value * 60
        elif unit in ["saniye", "second", ""]:  # Default unit is seconds
            total_seconds += value

    return total_seconds

def start_timer(duration):
    """Belirtilen süre için bir sayaç başlatır."""
    speak(f"Sayaç başladı: {duration} saniye")
    for remaining in range(duration, 0, -1):
        minutes, seconds = divmod(remaining, 60)
        # print(f"Kalan süre: {minutes} dakika {seconds} saniye", end="\r")
        time.sleep(1)
    speak("\nSüre doldu!")

def start_stopwatch():
    """Stopwatch işlevini başlatır."""
    global stop_flag
    stop_flag.clear()  # Durdurma bayrağını sıfırlar

    def stopwatch():
        speak("Süre ölçümü başladı.")
        start_time = time.time()

        while not stop_flag.is_set():  # Durdurulma bayrağı set edilene kadar çalışır
            elapsed_time = time.time() - start_time
            minutes, seconds = divmod(int(elapsed_time), 60)
            # print(f"Geçen süre: {minutes} dakika {seconds} saniye", end="\r")
            time.sleep(1)

        speak("\nSüre ölçümü durduruldu.")
        elapsed_time = time.time() - start_time
        minutes, seconds = divmod(int(elapsed_time), 60)
        speak(f"Toplam geçen süre: {minutes} dakika {seconds} saniye")

    stopwatch_thread = threading.Thread(target=stopwatch)
    stopwatch_thread.start()
    return stopwatch_thread

def stop_stopwatch():
    """Stopwatch işlevini durdurur."""
    global stop_flag
    stop_flag.set()  # Durdurma bayrağını set eder
    
def sayaç(command):
    try:
        duration = parse_duration(command)
        if duration > 0:
            timer_thread = threading.Thread(target=start_timer, args=(duration,))
            timer_thread.start()
        else:
            print("Geçerli bir süre belirtiniz.")   
    except Exception as e:
        print(f"Hata: {str(e)}") 

# Konum tabanlı işlemler
def get_location_info(retries=3, delay=5):
    import requests
    for i in range(retries):
        try:
            # Genel IP adresini al
            ip_response = requests.get('https://api.ipify.org?format=json')
            ip_response.raise_for_status()  # HTTP hatalarını kontrol et
            ip_data = ip_response.json()
            public_ip = ip_data['ip']

            # Genel IP adresi ile konum bilgilerini al
            location_response = requests.get(f"http://ipinfo.io/{public_ip}/json")
            location_response.raise_for_status()  # HTTP hatalarını kontrol et
            location_info = location_response.json()

            # Detaylı konum bilgilerini çıkar
            city = location_info.get('city', 'Bilinmeyen')
            region = location_info.get('region', 'Bilinmeyen')
            country = location_info.get('country', 'Bilinmeyen')
            postal = location_info.get('postal', 'Bilinmeyen')

            location_text = f"Bulunduğunuz yer: {city}, {region}, {country}, Posta Kodu: {postal}"
            print(location_text)
            return city, region, country, postal

        except requests.RequestException as e:
            if i < retries - 1:
                time.sleep(delay)  # Bekleme süresi
            else:
                speak("Üzgünüm bir sorun oluştu, internetinizi kontrol edin.")
        
def hava_durumu():
    try:
        speak("İlgileniyorum...")
        # API anahtarını buraya ekleyin
        api_key = "1a44ca0976662f6f21b9cab1af1db067"

        # Şehir ismini buraya ekleyin
        location = get_location_info()
        if location is None:
            return

        city = location[0]
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': city,
            'APPID': api_key,
            'units': 'metric'  # Birimleri Celsius olarak almak için
        }

        response = requests.get(base_url, params=params)
        response.raise_for_status()  # HTTP hatalarını kontrol et
        data = response.json()

        if data.get('cod') == 200:
            speak(f"Hissedilen Sıcaklık: {data['main']['feels_like']} °C")
            speak(f"Nem Oranı: {data['main']['humidity']} %")
            speak(f"Rüzgar Hızı: {data['wind']['speed']} m/s")
            
        else:
            speak(f'Hava Durumu Bilgileri Alınamadı.')
            
    except Exception:
        speak("Konum bazlı hava durumu tespit edilemedi.")
            
def ne_yapıyorsun():
    ne_yapıyorsun_listesi = [
            "Elektronların çarpışmasını izliyorum, ortam çok elektrikli görünüyor.",
            "Sizinle konuşuyorum.",
            "Sizi dinliyorum.",
            "Kendimi geliştirmeye çalışıyorum.",
            "Sözlük okuyorum, lütfen sonunu söyleyip süprizi bozma.",
            "Yeni espriler öğreniyorum, espri yap diyebilirsin."
    ]
    speak(random.choice(ne_yapıyorsun_listesi))

def git(text):
    try:
        yer = yer_ayıkla(text)
        
        # API anahtarını buraya ekleyin
        api_key = "1a44ca0976662f6f21b9cab1af1db067"

        # Şehir ismini argümandan alın
        city = yer
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': city,
            'APPID': api_key,
            'units': 'metric'  # Birimleri Celsius olarak almak için
        }

        response = requests.get(base_url, params=params)
        response.raise_for_status()  # HTTP hatalarını kontrol et
        data = response.json()

        if data.get('cod') == 200:
            speak(f"Bir saniye...")
            speak(f"{yer} konumu şuanda hava {data['main']['feels_like']} °C")
            rüzgar = data['wind']['speed']
            if rüzgar == 0:
                speak("ve rüzgar görünmüyor.")
            elif rüzgar < 5:
                speak("ve hafif rüzgar var.")
            elif 5 < rüzgar < 10:
                speak("Ve rüzgarlı görünüyor.")
            elif 10 < rüzgar:
                speak("Ve çok rüzgarlı görünüyor.")
            else:
                speak("Ancak rüzgarı ölçemedim.")
            
        else:
            speak(f'Hava Durumu Bilgileri Alınamadı.')
            
    except Exception as e:
        print(e)
        speak("Hava durumu tespit edilemedi.")
    
    
def yer_ayıkla(cumle):
    # Yer isimlerini yakalamak için kapsamlı bir regex deseni
    pattern = r"\b(\w+)(?:'?(?:ye|ya|ne|na|e|a|de|da|den|dan|da doğru|na doğru|ne doğru|e doğru|a doğru|ya doğru|ye doğru)\b|(?:ya gidiyorum|ye gitmek üzereyim|a gidiyorum|e gitmek üzereyim|gideceğim))"
    matches = re.findall(pattern, cumle, re.IGNORECASE)
    return matches[0] if matches else "Bilinmeyen Yer"

def asistan(user_input):
    if "" == user_input:
        return 
    
    """Kullanıcının mesajını G4F API'sine gönder ve yanıtı döndür."""
    text = f"{user_input} Kısa yanıt istiyorum."
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": text}]
    )
    blink()
    response = response.choices[0].message.content
    speak(response)

def blink():
    pygame.mixer.music.load('scale-e6-14577.mp3')
    pygame.mixer.music.play()

def bip():
    pygame.mixer.music.load('level-up-191997.mp3')
    pygame.mixer.music.play()
    time.sleep(1)

# Kullanıcı bilgileri yükleme
def read_encrypted_json(filename, key_filename):
    def decrypt_data(encrypted_data, key):
        cipher_suite = Fernet(key)
        decrypted_data = cipher_suite.decrypt(encrypted_data)
        return decrypted_data

    # Anahtarı okuyun
    with open(key_filename, 'rb') as key_file:
        key = key_file.read()

    # Şifreli veriyi okuyun
    with open(filename, 'rb') as file:
        encrypted_data = file.read()

    # Veriyi çözün
    decrypted_data = decrypt_data(encrypted_data, key)

    # JSON'u çözün ve Python nesnesine dönüştürün
    data = json.loads(decrypted_data.decode())
    return data

def read_data():
        # user.json dosyasını okumaya çalış
        try:    
                SECRET_KEY = 'aCrH_r_sdF7I0RmsZI1wU8dJADAB90G1lcG2chkP-hc='
                
                def decrypt_data(encrypted_data, key):
                    cipher_suite = Fernet(key)
                    decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
                    return decrypted_data

                def read_encrypted_json(filename):
                    # Anahtarı doğrudan koddan alın
                    key = SECRET_KEY.encode()  # Anahtarı bytes formatına çevirin

                    with open(filename, 'rb') as file:
                        encrypted_data = file.read()

                    decrypted_data = decrypt_data(encrypted_data, key)
                    return json.loads(decrypted_data)

                # Dosyayı oku ve veriyi döndür
                user = read_encrypted_json('user_asistan.json')
                return user
        except FileNotFoundError:
            speak("Kullanıcı bilgileri bulunamadı.")
            exit()
            
# Komutları yükle
def load_commands():
    global komutlar
    try:
        with open('vb.json', 'r', encoding='utf-8') as file:
            veri = json.load(file)
            komutlar = veri.get('komutlar', [])
            
    except FileNotFoundError:
        print("JSON dosyası bulunamadı.")
        komutlar = []
    except json.JSONDecodeError:
        print("JSON dosyası okunurken bir hata oluştu.")
        komutlar = []
    except Exception as e:
        print(f"Beklenmedik bir hata oluştu: {str(e)}")
        komutlar = []
            
# Komutu yürüt
def execute_command(text):
    for komut in komutlar:
        for ifade in komut['ifadeler']:
            if ifade in text:
                cevap = komut['cevap']
                if cevap:
                    cevap = cevap.format( 
                        datetime.datetime.now().strftime('%H:%M'), 
                        datetime.datetime.now().strftime('%d-%m-%Y')
                    )
                    speak(f"{cevap}")
                if komut.get('fonksiyon'):  # Fonksiyon varsa eval fonksiyonunu çalıştır
                    eval(f"{komut['fonksiyon']}")
                return
    asistan(text)
    
def kapat():
    speak(f"Görüşürüz {data['ad']}.")

if __name__ == "__main__":
    komutlar = []
    load_commands()
    
    data = read_data()
    print(data)
    
    # Süre sayımını kontrol etmek için bir bayrak
    stop_flag = threading.Event()
    
    pygame.mixer.init()
    
    calendar_file = 'calendar.json'
    # JSON dosyasını yükle veya yeni oluştur
    try:
        with open(calendar_file, 'r') as file:
            calendar = json.load(file)
    except FileNotFoundError:
        calendar = {}
        
    threading.Thread(target=alarm_thread).start()
    
    # Mikrofon Ayarları
    recognizer = sr.Recognizer()
    CHUNK = 1024  # Her bir ses bloğu
    FORMAT = pyaudio.paInt16  # Ses formatı
    CHANNELS = 1  # Mono
    RATE = 44100  # Örnekleme hızı (Hz)
    THRESHOLD = 50000  # Ses seviyesi eşiği (ayar yapılabilir)
    
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True, frames_per_buffer=CHUNK)
    
    wake_up_sound()
