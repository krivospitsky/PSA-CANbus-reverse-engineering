# PSA AEE2004 reverse engineering

## What is going on here

Just some repository to document the WIP of the reverse engineering of PSA's (Peugeot, Citroen and DS cars) CANbus architecture

## Basics

### History

Basically, PSA co-created the VAN bus, which was a competitor of CAN, and their first multiplexed cars used an architecture that's going to define how PSA does car electronics: 1 CAN "inter-systemes" IS bus, which connects the motor ECU, and other sensitive controllers (ABS, power steering, etc) to a central controller, the BSI (which is mostly a bridge between the CAN buses and also does functions such as centralized lock, climate control compressor management and the like); 1 or 2 VAN buses "Carosserie" (body) for the airbags, sensors and the like; and 1 VAN bus "confort" for the head unit, screen, gauges and the like.
Then in 2004 they updated to a "Full CAN" architecture called AEE2004 (AEE stands for "Architecture Electrique et Electronique"), which is basically the same as the CAN+VAN architecture, but using only CAN buses (and only 1 bdody bus).
In 2010, this was also updated to AEE2010, which uses the same bases as AEE2004 but updated for the current generation of controllers.

### Architecture & Design

The BSI is the central hub for the whole car, it also contains one end of every CAN bus, the IS bus is a 250 or 500kbps bus without fault tolerance, the other ones (CAR and CONF) are 125kbps and can work using only one wire if something happens.
Basically, PSA designs the whole architecture, and then send the specs to their different OEMs who apparently are given the choice of techology used, as long as it's "API" (both on the can bus and on the connector) matches PSA's design. That's why there's sometime different controllers for the same role, and why these controllers often aren't designed using the same architecture at all.
The controllers also comply with OSEK and AUTOSAR standards.

### Diagnostics

The diagnostic (OBD-II) port is a bit different, as it uses a 500kbps "DiagOnCan" bus as well as the IS bus, which is switched to the OBD-II port on demand.
AEE2004 apparently uses UDS (over CAN-TP) as well as standard EOBD standards, they may (and probably do) use proprietary extensions of UDS.
Their official diagnostic kit is made by actia, there was 2 generations: a combinaison of "Lexia" (citroen) and "PP2000" (peugeot), using (at least for peugeot) the "PPI" interface (PP for both PPI and PP2000 stands for "Peugeot Planet"... the internet was new back then). Nowadays, there's "Diagbox" (diag software) and "XS Evolution" (the dongle). Technicians can also use "ServiceBox" (manuals and parts refernces) as well as "SEDRE" (schematics), but they don't communicate with the car.


## ECUs status (NOPE == No access to car that have this option)

| ECU                     | Network(s)    | Status | Notes                                |
|-------------------------|---------------|--------|--------------------------------------|
| BSI                     | IS, CAR, CONF | WIP    | Central controller                   |
| MED17.4                 | IS            | TODO   | Gasoline motor controller (VTI, THP) |
| DAE/GMP                 | IS            | TODO   | Power steering                       |
| BMVP/AM6/AL4/BVA        | IS            | TODO   | Gearbox controller                   |
| CAV                     | IS            | TODO   | Steering wheel sensor                |
| ABS/EHB/ESP             | IS            | TODO   | ABS and ESP controller               |
| DSG                     | IS            | TODO   | Tyre presure sensor                  |
| BCP                     | IS            | TODO   | Adaptative front lights              |         
| CMB                     | CONF          | WIP    | Instrument cluster                   |
| EMF (A+, C-)            | CONF          | WIP    | "Basic" screen (without navigation)  |
| RD4(5)                  | CONF          | WIP    | Head unit without navigation         |
| CD Charger              | CONF          | NOPE   | Multi-CD extension                   |
| CLIM                    | CONF          | WIP    | Bi-Zone auto climate control         |
| AAS                     | CONF          | TODO   | Parking radar                        |
| BTE                     | CONF          | WIP    | Roof controller, CC cars only        |
| EDP                     | CONF          | TODO   | Power windows                        |
| SAM                     | CONF          | NOPE   | Dead angle                           |
| RT3/RT4/RT5/RT6         | CONF          | TODO   | Head unit with navigation and phone  |
| SCU/TO                  | CONF          | NOPE   | Sunroof controller                   |
| MAE                     | CAR           | NOPE   | School controller                    |
| RBG                     | CAR           | TODO   | Airbag controller                    |
| CDPL                    | CAR           | TODO   | Rain and Sunlight sensor             |
| BSM                     | CAR           | TODO   | Power distribution                   |
| BSR                     | CAR           | TODO   | Trailer lights controller            |
| ALARM                   | CAR           | TODO   | Volumetric alarm                     |
| HDC/VMF/COM200X         | CAR           | TODO   | Steering wheel commands              |

There's plenty of controllers that aren't in this list yet, i'll update it when new controllers are confirmed in AEE2004


## What to do with this

You can help by providing dumps of your car if you can; The DBC files can be openned with vector's software (expensive) or SavvyCAN (open source); The rest is up to you, it's only a documentation repository.

## Thanks and references

* Wouter Bokslag for his awesome work on the [reverse engineering of the immobilizer](https://fahrplan.events.ccc.de/congress/2019/Fahrplan/events/11020.html)
* Alexandre Blin for his [tools](https://github.com/alexandreblin?tab=repositories), work on his 207 and for being a huge inspiration for this
* Peter Pinter for his huge work on his own [FullCAN to VAN bridge](https://github.com/morcibacsi?tab=repositories)
* Karaelyn and Kailokyra for their advices, especially on embedded dev
* All the people who leaked parts of PSA's designs all over the internet :)
