# Status for each frame ID
(OK = 100% done // WIP = partial infos // TODO = zero info)
Names starting with `x_` are the "non official" ones (eg we guessed the feature and named them ourselves)
Names in uppercase are the ones used at PSA
Frames without a name are currently unknown
Frames with a "?" at the end of the name are unvalidated guesses
Names are in french, for now (as PSA uses french intenally), sorry, our custom names as well, as we try to replicate PSA's way of naming things
If a frame is used in multiple networks, the BSI forwarded the message (if it isn't from the BSI itself)

## ECUs
(this is not a list of every ECU in AEE2004, for that see ECUS.md, this is a list of ECU we have and thus for which we  have dumps and can reverse engineer)
| Bus  | ECUs                                |
|------|-------------------------------------|
| IS   | BSI, BCP, HDC/CAV, CMM, ABS, DAE    |
| CAR  | BSI, BSM, BSR, AIRBAG, CDPL, HDC    |
| CONF | BSI, RADIO, CLIM, EMF, COMBINE, BTE |

## Frames

| ID    | Bus           | Status | Sending ECU | Name             |
|-------|---------------|--------|-------------|------------------|
| 0x007 | CAR           | TODO   |
| 0x018 | CAR, CONF     | TODO   | AIRBAG (?)  | `x_etat_airbags`
| 0x036 | CAR, CONF     | WIP    | BSI         | `COMMANDES_BSI`
| 0x046 | CAR           | TODO   | BSI         | `COMMANDES_CONDUCTEUR` 
| 0x058 | CAR           | TODO   |
| 0x05A | CAR           | TODO   |
| 0x072 | IS            | OK     | CMM         | `x_demande_antidem`
| 0x094 | CAR           | WIP    | HDC         | `ETAT_HDC` 
| 0x099 | CAR           | TODO   |
| 0x0A4 | CONF          | TODO   | RADIO       |
| 0x0A8 | IS            | OK     | BSI         | `x_reponse_antidem`
| 0x0B6 | CAR, CONF     | WIP    | BSI         | `DONNEES_BSI_RAPIDES`
| 0x0C2 | CAR           | TODO   |
| 0x0C6 | CAR           | TODO   |
| 0x0D6 | CONF          | WIP    | BTE         | `x_etat_bte`
| 0x0DF | CONF          | TODO   | 
| 0x0E6 | CONF          | WIP    | BSI
| 0x0F6 | CAR, CONF     | OK     | BSI         | `DONNEES_BSI_LENTES`
| 0x105 | IS            | TODO   | HDC/CAV (?) | `x_ecu_infos` (?)
| 0x108 | IS            | TODO   | CMM         | `x_ecu_infos` (?)
| 0x10A | CAR           | TODO   |
| 0x10B | CONF          | TODO   |
| 0x110 | CONF          | TODO   | CLIM
| 0x112 | IS            | TODO   | BSI         | `x_ecu_infos` (?)
| 0x114 | CAR           | TODO   |
| 0x117 | IS            | TODO   | BCP (?)     | `x_ecu_infos` (?)
| 0x119 | CAR           | TODO   |
| 0x120 | CONF          | WIP    | BSI         | `x_journal_erreurs`
| 0x125 | CONF          | TODO   |
| 0x128 | CONF          | WIP    | BSI         | `CDE_COMBINE_SIGNALISATION`
| 0x12B | CONF          | TODO   |
| 0x12D | CONF          | WIP    | BSI         | `x_commandes_clim`
| 0x131 | CONF          | WIP    | RADIO       | `x_commandes_chargeur_cd`
| 0x134 | CONF          | TODO   | 
| 0x142 | CAR           | TODO   |
| 0x14C | CONF          | TODO   | 
| 0x154 | CAR           | TODO   |
| 0x15B | CONF          | WIP    | EMF         | `EMF_COE_MODIF_PROFILS`
| 0x161 | CONF          | WIP    | BSI         | `ETAT_BSI_TEMP_NIVEAU`
| 0x165 | CONF          | WIP    | RADIO       | `ETAT_RADIO_GEN_GEN`
| 0x167 | CONF          | WIP    | EMF         | `COMMANDES_EMF`
| 0x168 | CONF          | WIP    | BSI         | `CDE_COMBINE_TEMOINS`
| 0x182 | CAR           | TODO   |
| 0x190 | CONF          | TODO   | CLIM
| 0x199 | CAR           | TODO   |
| 0x1A1 | CONF          | WIP    | BSI         | `BSI_CD_PTR_MESSAGE`
| 0x1A5 | CONF          | WIP    | RADIO       | `x_etat_radio_gen_vol`
| 0x1A8 | CONF          | WIP    | BSI         | `GESTION_VITESSE`
| 0x1C4 | CAR           | TODO   |
| 0x1D0 | CONF          | TODO   | CLIM        | `x_etat_clim`
| 0x1D9 | CAR           | TODO   |
| 0x1E0 | CONF          | WIP    | RADIO       | `x_etat_radio_conf_fm`
| 0x1E5 | CONF          | WIP    | RADIO       | `x_etat_radio_conf_audio`
| 0x208 | IS            | OK     | CMM         | `x_infos_moteur_dyn_1` (?)
| 0x217 | CONF          | WIP    | COMBINE     | `ETAT_COMBINE`
| 0x219 | CAR           | TODO   |
| 0x21F | CAR, CONF     | WIP    | HDC         | `x_commandes_volant`
| 0x220 | CONF          | WIP    | BSI         | `x_etat_ouvrants`
| 0x221 | CONF          | WIP    | BSI         | `INFOS_GEN_ODB`
| 0x225 | CONF          | WIP    | RADIO       | `x_etat_radio_fm_freq`
| 0x227 | CONF          | TODO   | BSI         |
| 0x257 | CONF          | TODO   | 
| 0x260 | CONF          | TODO   | BSI
| 0x261 | CONF          | WIP    | BSI         | `x_infos_odb_slot1`
| 0x265 | CONF          | WIP    | RADIO       | `x_etat_radio_fm_station`
| 0x29A | CAR           | TODO   |
| 0x2A0 | CONF          | TODO   | BSI
| 0x2A1 | CONF          | WIP    | BSI         | `x_infos_odb_slot2`
| 0x2A5 | CONF          | WIP    | RADIO       | `ETAT_RADIO_CD_CD`
| 0x2B6 | CONF          | WIP    | BSI         | `x_infos_vin_fin`
| 0x2E1 | CONF          | WIP    | BSI         | `ETAT_FONCTIONS`
| 0x305 | IS            | WIP    | HDC/CAV     | `x_infos_angle_volant`
| 0x30D | IS            | TODO   | ABS (?)     |
| 0x317 | CONF          | TODO   | COMBINE     |
| 0x325 | CONF          | WIP    | RADIO       | `x_etat_radio_cd_gen`
| 0x336 | CONF          | WIP    | BSI         | `x_infos_vin_debut`
| 0x348 | IS            | WIP    | CMM         | `x_infos_moteur_dyn_2` (?)
| 0x34D | IS            | TODO   | ABS (?)     | `x_etat_esp` (?)
| 0x359 | CAR           | TODO   |
| 0x361 | CONF          | TODO   | BSI         |
| 0x365 | CONF          | WIP    | RADIO       | `ETAT_RADIO_CD_DSK`
| 0x38D | IS            | WIP    | ABS         | `x_infos_dynamique` (?)
| 0x3A5 | CONF          | WIP    | RADIO       | `ETAT_RADIO_CD_TRK`
| 0x3A7 | CONF          | WIP    | BSI         | `INFOS_MAINTENANCE`
| 0x3B6 | CONF          | WIP    | BSI         | `x_infos_vin_millieu`
| 0x3CD | IS            | TODO   | ABS (?)     |
| 0x3E5 | CONF          | WIP    | RADIO       | `ETAT_CDT`
| 0x3F6 | CONF          | WIP    | EMF         | `x_etat_emf_conf_date`
| 0x40D | IS            | TODO   |
| 0x412 | CAR, CONF, IS | TODO   | BSI         | `x_bsi_infos_chassis` (?)
| 0x432 | IS            | TODO   | BSI         |
| 0x44D | IS            | OK     | ABS         | `x_infos_vitesse_roues`
| 0x468 | IS            | TODO   | CMM         | `x_infos_moteur_dyn_3` (?)
| 0x488 | IS            | OK     | CMM/BSI(?)  | `x_infos_moteur_gen` (?)
| 0x495 | IS            | TODO   | DAE(?)      |
| 0x4A0 | CONF          | TODO   |             |
| 0x502 | CAR           | WIP    | HDC         | `x_ecu_status`
| 0x504 | CAR           | WIP    | AIRBAG      | `x_ecu_status`
| 0x507 | CAR           | WIP    | BSM         | `x_ecu_status`
| 0x50A | CAR           | WIP    | CDPL        | `x_ecu_status`
| 0x50D | IS            | WIP    | ABS         | `x_ecu_status` (?)
| 0x50E | IS            | WIP    | CMM         | `x_ecu_status` (?)
| 0x512 | CAR, CONF     | WIP    | BSI         | `x_ecu_status` 
| 0x517 | IS            | WIP    | BCP(?)      | `x_ecu_status` (?)
| 0x51F | CONF          | WIP    | COMBINE     | `x_ecu_status`
| 0x520 | CONF          | WIP    | RADIO       | `x_ecu_status`
| 0x525 | CONF          | WIP    | EMF         | `x_ecu_status`
| 0x527 | CONF          | WIP    | BTE         | `x_ecu_status`
| 0x52D | CONF          | WIP    | CLIM        | `x_ecu_status`
| 0x552 | IS            | WIP    | BSI         |
| 0x588 | IS            | WIP    | CMM         |
| 0x592 | IS            | WIP    | CMM/BSI (?) |
| 0x5C2 | CAR           | WIP    | HDC         | `x_ecu_infos`
| 0x5C4 | CAR           | WIP    | AIRBAG      | `x_ecu_infos`
| 0x5C7 | CAR           | WIP    | BSM         | `x_ecu_infos`
| 0x5CA | CAR           | WIP    | CDPL        | `x_ecu_infos`
| 0x5D2 | CAR, CONF     | WIP    | BSI         | `x_ecu_infos` (?)
| 0x5DF | CONF          | WIP    | COMBINE     | `x_ecu_infos`
| 0x5E0 | CONF          | WIP    | RADIO       | `x_ecu_infos`
| 0x5E5 | CONF          | WIP    | EMF         | `x_ecu_infos`
| 0x5E7 | CONF          | WIP    | BTE         | `x_ecu_infos`
| 0x5ED | CONF          | WIP    | CLIM        | `x_ecu_infos`
| 0x608 | IS            | TODO   | CMM         | `x_eobd`
| 0x612 | IS            | TODO   | BSI         |
| 0x788 | IS            | TODO   | CMM         | `x_infos_cmm_supervision` (?)
| 0x78D | IS            | TODO   |
| 0x792 | IS            | TODO   | BSI         |
| 0x795 | IS            | TODO   |
| 0x797 | IS            | TODO   |
| 0x7E2 | IS            | TODO   |
| 0x7F2 | IS            | TODO   |

## Unknown frames
(frames for which we have zero info, neither the sending ECU, the content of the frame or even a name/function)
If you know anything about these, please create an issue!
| Bus  | Frames IDs                                                                                                                   |
|------|------------------------------------------------------------------------------------------------------------------------------|
| IS   | 0x40D, 0x78D, 0x795, 0x797, 0x7E2, 0x7F2                                                                                     |
| CAR  | 0x007, 0x058, 0x05A, 0x099, 0x0C2, 0x0C6, 0x10A, 0x114, 0x119, 0x142, 0x154, 0x182, 0x199, 0x1C4, 0x1D9, 0x219, 0x29A, 0x359 |
| CONF | 0x0DF, 0x10B, 0x125, 0x12B, 0x134, 0x14C, 0x257, 0x4A0                                                                       |
