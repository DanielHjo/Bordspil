from buzzer_music import music
from machine import Pin, PWM
import neopixel, time, random
from time import sleep

# ---------------------
# Reglur fyrir spilið.
# ---------------------

#Byrjun:
#Kastaðu upp á hver byrjar sem fær hæsta byrjar, fyrstur á FINISH reitinn vinnur.

#Sprengju Reitur:
#Þegar lent er á sprengju þarf að kasta aftur ef þú færð þrjá eða lægra farðu aftur um fjóra reiti af þú færð hærra en þrjá farðu fram um tvo reiti.

#Þrauta reitur:
#Ef ekki er náð að klára þrautina sem þú lentir á slepptu næstu umferð þinni.

#Hreyfing:
#Ef þú ert hreyfður vegna áhrif einhvers annað en teninga kasts þá áttu EKKI að gera það sem nýji reyturinn segir.



reed1 = Pin(14, Pin.IN, Pin.PULL_UP)
reed2 = Pin(13, Pin.IN, Pin.PULL_UP)
reed3 = Pin(12, Pin.IN, Pin.PULL_UP)
reed4 = Pin(11, Pin.IN, Pin.PULL_UP)

hatalari = PWM(Pin(9), 20000)
nol = 24
NeoPin = Pin(18)
np = neopixel.NeoPixel(NeoPin, nol)
button = Pin(17, Pin.IN, Pin.PULL_UP)






# Noturnar fyrir lagið

song = '0 D5 4 14;4 A5 4 14;8 C6 4 14;12 B5 4 14;16 G5 2 14;18 F5 2 14;20 E5 2 14;22 F5 2 14;24 G5 8 14;4 E5 8 16;4 C5 8 16;4 F4 8 16;12 D5 8 16;12 B4 8 16;12 E4 8 16;20 C5 8 16;20 A4 8 16;20 D4 8 16;0 E4 4 16;0 B4 4 16;28 E4 4 16;28 B4 4 16'


mySong = music(song, looping=False, pins=[Pin(9)])



np.fill((0,0,0))
np.write()

# kóðinn sem lætur lagið spilast
while True:    
    if not mySong.tick():   
        break
    sleep(0.04)


  
    
while True:
    if not reed1.value():   # ef reitur er tómur þá er gildið 1 lesið.
        hatalari.duty(512) 
        hatalari.freq(880) 
        print("1")
        
    elif not reed2.value():   # ef reitur er tómur þá er gildið 1 lesið.
        hatalari.duty(512) 
        hatalari.freq(440) 
        print("2")
        
        
    elif not reed3.value():   # ef reitur er tómur þá er gildið 1 lesið.
        hatalari.duty(512) 
        hatalari.freq(440) 
        print("4")
        
        
    elif not reed4.value():   # ef reitur er tómur þá er gildið 1 lesið.
        hatalari.duty(512) 
        hatalari.freq(440) 
        print("4")
    else:
        hatalari.duty(0)   
        print("0")        
        

    if not button.value():          
        np.fill((0,0,0)) # resettar LEDs
        led = random.randint(0, nol -1)
        np[led] = (0, 100, 0) # kveikir á grænum lit
        np.write()
        time.sleep(0.3) # debounce
    time.sleep(0.01)
    
