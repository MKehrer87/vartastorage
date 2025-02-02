from dataclasses import dataclass
from typing import List as list

@dataclass
class InfoData:
    # /cgi/info.js data
    charger_serial: list[str]
    charger_mac: list[str]
    sw_id_charger: list[int]
    hw_id_charger: list[int]
    sw_version_charger: list[str]
    bl_version_charger: list[str]
    battery_sw: list[str]
    battery_hw: list[str]
    battery_serial: list[str]
    bm_update: list[str]
    bm_update_sw: list[str]
    bm_production: list[str]
    lg_battery_serial: list[str]
    device_description: str = None
    display_serial: str = None
    sw_id_ems: int = None
    hw_id_ems: int = None
    countrycode: int = None
    sw_version_ems: str = None
    anz_charger: int = None
    soll_charger: int = None
    serial_emeter: str = None
    mac_emeter: str = None
    sw_version_emeter: str = None
    bl_version_emeter: str = None
    hw_id_emeter: int = None
    serial_wr: str = None
    mac_wr: int = None
    sw_id_wr: int = None
    hw_id_wr: int = None
    sw_version_wr: str = None
    bl_version_wr: str = None
    serial_ens: str = None
    mac_ens: int = None
    sw_id_ens: int = None
    hw_id_ens: int = None
    sw_version_ens: str = None
    bl_version_ens: str = None
    p_ems_max: int = None
    p_ems_maxdisc: int = None

    @classmethod
    def from_dict(cls, info: dict) -> "InfoData":
        return cls(
            device_description=info.get("Device_Description"),
            display_serial=info.get("Display_Serial"),
            sw_id_ems=info.get("SW_ID_EMS"),
            hw_id_ems=info.get("HW_ID_EMS"),
            countrycode=info.get("countrycode"),
            sw_version_ems=info.get("SW_Version_EMS"),
            anz_charger=info.get("Anz_Charger"),
            soll_charger=info.get("Soll_Charger"),
            serial_emeter=info.get("Serial_EMeter"),
            mac_emeter=info.get("MAC_EMeter"),
            sw_version_emeter=info.get("SW_Version_EMeter"),
            bl_version_emeter=info.get("BL_Version_EMeter"),
            hw_id_emeter=info.get("HW_ID_EMeter"),
            serial_wr=info.get("Serial_WR"),
            mac_wr=info.get("MAC_WR"),
            sw_id_wr=info.get("SW_ID_WR"),
            hw_id_wr=info.get("HW_ID_WR"),
            sw_version_wr=info.get("SW_Version_WR"),
            bl_version_wr=info.get("BL_Version_WR"),
            serial_ens=info.get("Serial_ENS"),
            mac_ens=info.get("MAC_ENS"),
            sw_id_ens=info.get("SW_ID_ENS"),
            hw_id_ens=info.get("HW_ID_ENS"),
            sw_version_ens=info.get("SW_Version_ENS"),
            bl_version_ens=info.get("BL_Version_ENS"),
            charger_serial=info.get("Charger_Serial", []),
            charger_mac=info.get("Charger_MAC", []),
            sw_id_charger=info.get("SW_ID_Charger", []),
            hw_id_charger=info.get("HW_ID_Charger", []),
            sw_version_charger=info.get("SW_Version_Charger", []),
            bl_version_charger=info.get("BL_Version_Charger", []),
            p_ems_max=info.get("P_EMS_Max"),
            p_ems_maxdisc=info.get("P_EMS_MaxDisc"),
            battery_sw=info.get("BatterySW", []),
            battery_hw=info.get("BatteryHW", []),
            battery_serial=info.get("BatterySerial", []),
            bm_update=info.get("BM_Update", []),
            bm_update_sw=info.get("BM_UpdateSW", []),
            bm_production=info.get("BM_Production", []),
            lg_battery_serial=info.get("LG_Battery_Serial", []),
        )


@dataclass
class EnergyData:
    # /cgi/energy.js data
    total_charge_cycles: list[int]
    total_grid_ac_dc: int = None  # Wh
    total_grid_dc_ac: int = None  # Wh
    total_inverter_ac_dc: int = None  # Wh
    total_inverter_dc_ac: int = None  # Wh

    @classmethod
    def from_dict(cls, energy: dict) -> "EnergyData":
        return cls(
            total_grid_ac_dc=energy.get("EGrid_AC_DC"),
            total_grid_dc_ac=energy.get("EGrid_DC_AC"),
            total_inverter_ac_dc=energy.get("EWr_AC_DC"),
            total_inverter_dc_ac=energy.get("EWr_DC_AC"),
            total_charge_cycles=energy.get("Chrg_LoadCycles", []),
        )


@dataclass
class ServiceData:
    # /cgi/user_serv.js data
    hours_until_filter_maintenance: int = None  # Hours
    status_fan: int = None
    status_main: int = None

    @classmethod
    def from_dict(cls, service: dict) -> "ServiceData":
        return cls(
            hours_until_filter_maintenance=service.get("FilterZeit"),
            status_fan=service.get("Fan"),
            status_main=service.get("Main"),
        )


@dataclass
class WrData:
    nominal_power: int = None  # W
    u_verbund_l1: int = None  # V
    u_verbund_l2: int = None  # V
    u_verbund_l3: int = None  # V
    i_verbund_l1: int = None  # A
    i_verbund_l2: int = None  # A
    i_verbund_l3: int = None  # A
    u_insel_l1: int = None  # V
    u_insel_l2: int = None  # V
    u_insel_l3: int = None  # V
    i_insel_l1: int = None  # A
    i_insel_l2: int = None  # A
    i_insel_l3: int = None  # A
    temp_l1: int = None  # Celcius
    temp_l2: int = None  # Celcius
    temp_l3: int = None  # Celcius
    temp_board: int = None  # Celcius
    frequency_grid: int = None  # Hz
    online_status: int = None  # 0=Offline, 1=Online
    fan_speed: int = None  # percentage

    @classmethod
    def from_dict(cls, wr: dict) -> "WrData":
        return cls(
            nominal_power=wr.get("PSoll"),
            u_verbund_l1=wr.get("U Verbund L1"),
            u_verbund_l2=wr.get("U Verbund L2"),
            u_verbund_l3=wr.get("U Verbund L3"),
            i_verbund_l1=wr.get("I Verbund L1")/100.0,
            i_verbund_l2=wr.get("I Verbund L2")/100.0,
            i_verbund_l3=wr.get("I Verbund L3")/100.0,
            u_insel_l1=wr.get("U Insel L1"),
            u_insel_l2=wr.get("U Insel L2"),
            u_insel_l3=wr.get("U Insel L3"),
            i_insel_l1=wr.get("I Insel L1")/100.0,
            i_insel_l2=wr.get("I Insel L2")/100.0,
            i_insel_l3=wr.get("I Insel L3")/100.0,
            temp_l1=wr.get("Temp L1"),
            temp_l2=wr.get("Temp L2"),
            temp_l3=wr.get("Temp L3"),
            temp_board=wr.get("TBoard"),
            frequency_grid=wr.get("FNetz")/10.0,
            online_status=wr.get("OnlineStatus"),
            fan_speed=wr.get("Luefter"),
        )


@dataclass
class EMeterData:
    f_netz: int = None
    sens_state: int = None
    u_v_l1: int = None
    u_v_l2: int = None
    u_v_l3: int = None
    iw_v_l1: int = None
    iw_v_l2: int = None
    iw_v_l3: int = None
    ib_v_l1: int = None
    ib_v_l2: int = None
    ib_v_l3: int = None
    is_v_l1: int = None
    is_v_l2: int = None
    is_v_l3: int = None
    iw_pv_l1: int = None
    iw_pv_l2: int = None
    iw_pv_l3: int = None
    ib_pv_l1: int = None
    ib_pv_l2: int = None
    ib_pv_l3: int = None
    is_pv_l1: int = None
    is_pv_l2: int = None
    is_pv_l3: int = None

    @classmethod
    def from_dict(cls, emeter: dict) -> "EMeterData":
        return cls(
            f_netz=emeter.get("FNetz"),
            sens_state=emeter.get("SensState"),
            u_v_l1=emeter.get("U_V_L1"),
            u_v_l2=emeter.get("U_V_L2"),
            u_v_l3=emeter.get("U_V_L3"),
            iw_v_l1=emeter.get("Iw_V_L1"),
            iw_v_l2=emeter.get("Iw_V_L2"),
            iw_v_l3=emeter.get("Iw_V_L3"),
            ib_v_l1=emeter.get("Ib_V_L1"),
            ib_v_l2=emeter.get("Ib_V_L2"),
            ib_v_l3=emeter.get("Ib_V_L3"),
            is_v_l1=emeter.get("Is_V_L1"),
            is_v_l2=emeter.get("Is_V_L2"),
            is_v_l3=emeter.get("Is_V_L3"),
            iw_pv_l1=emeter.get("Iw_PV_L1"),
            iw_pv_l2=emeter.get("Iw_PV_L2"),
            iw_pv_l3=emeter.get("Iw_PV_L3"),
            ib_pv_l1=emeter.get("Ib_PV_L1"),
            ib_pv_l2=emeter.get("Ib_PV_L2"),
            ib_pv_l3=emeter.get("Ib_PV_L3"),
            is_pv_l1=emeter.get("Is_PV_L1"),
            is_pv_l2=emeter.get("Is_PV_L2"),
            is_pv_l3=emeter.get("Is_PV_L3"),
        )


@dataclass
class EnsData:
    f_netz: int = None
    u_v_l1: int = None
    u_v_l2: int = None
    u_v_l3: int = None

    @classmethod
    def from_dict(cls, ens: dict) -> "EnsData":
        return cls(
            f_netz=ens.get("FNetz"),
            u_v_l1=ens.get("U_V_L1"),
            u_v_l2=ens.get("U_V_L2"),
            u_v_l3=ens.get("U_V_L3"),
        )


@dataclass
class ChargerData:
    # TODO
    pass


@dataclass
class BattData:
    # TODO
    index: int = None
    enabled: int = None
    soc_GS: int = None
    state: int = None
    u: float = None
    i: float = None
    u_Out: int = None
    u_Cool: int = None
    u_Vcc: int = None
    t_ht: int = None
    t_tr: int = None
    t_Board: int = None
    p_Soll: int = None
    soh_CMax: int = None
    soh_Cuxtime: int = None
    soh_DMax: int = None
    soh_Duxtime: int = None
    errorFlags: int = None
    helperFlags: int = None
    betrFlags: int = None
    steuerFlags: int = None
    battState: int = None
    SVDFflags: int = None
    RSOCmin: int = None
    RSOCmax: int = None
    SOCcut: int = None
    DSOC_Thr1: int = None
    DSOC_Thr2: int = None
    SVDFtime: int = None
    SVDFcnt1s: int = None
    battName: str = None
    battType: int = None
    battAlarmsRack: int = None
    battWarningsRack: int = None
    battWarningsRack: int = None
    battURack: int = None
    battIRack: int = None
    battSOCRack: int = None
    battSOHRack: int = None
    battUmaxRack: int = None
    battIchargemaxRack: int = None
    battIdischargemaxRack: int = None
    battTempRack: int = None
    moduleState: int = None
    moduleAlarms: int = None
    moduleWarnings: int = None
    moduleFaults1: int = None
    moduleFaults2: int = None
    moduleIntErrors: int = None
    moduleSOC: int = None
    moduleSOH: int = None
    moduleU: int = None
    moduleI: int = None
    moduleUmin: int = None
    moduleUmax: int = None
    moduleUavg: int = None
    moduleIchargemax: int = None
    moduleIdischargemax: int = None
    modulePchargemax: int = None
    modulePdischargemax: int = None
    moduleTemp1: int = None
    moduleTemp2: int = None
    moduleTempAbg: int = None
    moduleBalTarg: int = None
    moduleAnzCycles: int = None
    moduleCapDesign: int = None
    moduleCapUsable: int = None
    moduleCapRemain: int = None
    moduleSVDStat: int = None
    modulePackSerNr: int = None
    moduleLifeEnergy: int = None
    moduleRackSOCmax: int = None
    moduleRackSOCmin: int = None
    moduleSwVersFull: str = None
    moduleCellVolt1: int = None
    moduleCellVolt2: int = None
    moduleCellVolt3: int = None
    moduleCellVolt4: int = None
    moduleCellVolt5: int = None
    moduleCellVolt6: int = None
    moduleCellVolt7: int = None
    moduleCellVolt8: int = None
    moduleCellVolt9: int = None
    moduleCellVolt10: int = None
    moduleCellVolt11: int = None
    moduleCellVolt12: int = None
    moduleCellVolt13: int = None
    moduleCellVolt14: int = None
	
    @classmethod
    def from_dict(cls, charger: dict) -> "ChargerData":
      #print(charger);
      #print(charger.get('BattData')[12][0])
      return cls(
        index = charger.get('Index'),
        enabled = charger.get('Enabled'),
        soc_GS = charger.get('SOC_GS'),
        state = charger.get('State'),
        u = charger.get('U')/100,
        u_Out = charger.get('UOut'),
        u_Cool = charger.get('UCool'),
        u_Vcc = charger.get('UVcc'),
        t_ht = charger.get('THT'),
        t_tr = charger.get('TTR'),
        t_Board = charger.get('TBoard'),
        p_Soll = charger.get('PSoll'),
        soh_CMax = charger.get('SOHCmax'),
        soh_Cuxtime = charger.get('SOHCuxtime'),
        soh_DMax = charger.get('SOHDmax'),
        soh_Duxtime = charger.get('SOHDuxtime'),
        errorFlags = charger.get('ErrorFlags'),
        helperFlags = charger.get('HelperFlags'),
        betrFlags = charger.get('BetrFlags'),
        steuerFlags = charger.get('SteuerFlags'),
        battState = charger.get('BattState'),
        SVDFflags = charger.get('SVDFflags'),
        RSOCmin = charger.get('RSOCmin'),
        RSOCmax = charger.get('RSOCmax'),
        SOCcut = charger.get('SOCcut'),
        DSOC_Thr1 = charger.get('DSOC_Thr1'),
        DSOC_Thr2 = charger.get('DSOC_Thr2'),
        SVDFtime = charger.get('SVDFtime'),
        SVDFcnt1s = charger.get('SVDFcnt1s'),
        battName = charger.get('BattData')[0],
        battType = charger.get('BattData')[1],
        battAlarmsRack = charger.get('BattData')[2],
        battWarningsRack = charger.get('BattData')[3],
        battURack = charger.get('BattData')[4]/100.0,
        battIRack = charger.get('BattData')[5],
        battSOCRack = charger.get('BattData')[6],
        battSOHRack = charger.get('BattData')[7]/10.0,
        battUmaxRack = charger.get('BattData')[8]/10.0,
        battIchargemaxRack = charger.get('BattData')[9],
        battIdischargemaxRack = charger.get('BattData')[10],
        battTempRack = charger.get('BattData')[11]/10.0,
        moduleState = charger.get('BattData')[12][0][0],
        moduleAlarms = charger.get('BattData')[12][0][1],
        moduleWarnings = charger.get('BattData')[12][0][2],
        moduleFaults1 = charger.get('BattData')[12][0][3],
        moduleFaults2 = charger.get('BattData')[12][0][4],
        moduleIntErrors = charger.get('BattData')[12][0][5],
        moduleSOC = charger.get('BattData')[12][0][6]/10.0,
        moduleSOH = charger.get('BattData')[12][0][7]/10.0,
        moduleU = charger.get('BattData')[12][0][8]/10.0,
        moduleI = charger.get('BattData')[12][0][9]/10.0,
        moduleUmin = charger.get('BattData')[12][0][10]/1000.0,
        moduleUmax = charger.get('BattData')[12][0][11]/1000.0,
        moduleUavg = charger.get('BattData')[12][0][12]/1000.0,
        moduleIchargemax = charger.get('BattData')[12][0][13],
        moduleIdischargemax = charger.get('BattData')[12][0][14],
        modulePchargemax = charger.get('BattData')[12][0][15],
        modulePdischargemax = charger.get('BattData')[12][0][16],
        moduleTemp1 = charger.get('BattData')[12][0][17]/10.0,
        moduleTemp2 = charger.get('BattData')[12][0][18]/10.0,
        moduleTempAbg = charger.get('BattData')[12][0][19]/10.0,
        moduleBalTarg = charger.get('BattData')[12][0][20],
        moduleAnzCycles = charger.get('BattData')[12][0][21],
        moduleCapDesign = charger.get('BattData')[12][0][22],
        moduleCapUsable = charger.get('BattData')[12][0][23],
        moduleCapRemain = charger.get('BattData')[12][0][24],
        moduleSVDStat = charger.get('BattData')[12][0][25],
        modulePackSerNr = charger.get('BattData')[12][0][26],
        moduleLifeEnergy = charger.get('BattData')[12][0][27],
        moduleRackSOCmax = charger.get('BattData')[12][0][28],
        moduleRackSOCmin = charger.get('BattData')[12][0][29],
        moduleSwVersFull = charger.get('BattData')[12][0][30],
        moduleCellVolt1 = charger.get('BattData')[12][0][31]/1000.0,
        moduleCellVolt2 = charger.get('BattData')[12][0][32]/1000.0,
        moduleCellVolt3 = charger.get('BattData')[12][0][33]/1000.0,
        moduleCellVolt4 = charger.get('BattData')[12][0][34]/1000.0,
        moduleCellVolt5 = charger.get('BattData')[12][0][35]/1000.0,
        moduleCellVolt6 = charger.get('BattData')[12][0][36]/1000.0,
        moduleCellVolt7 = charger.get('BattData')[12][0][37]/1000.0,
        moduleCellVolt8 = charger.get('BattData')[12][0][38]/1000.0,
        moduleCellVolt9 = charger.get('BattData')[12][0][39]/1000.0,
        moduleCellVolt10 = charger.get('BattData')[12][0][40]/1000.0,
        moduleCellVolt11 = charger.get('BattData')[12][0][41]/1000.0,
        moduleCellVolt12 = charger.get('BattData')[12][0][42]/1000.0,
        moduleCellVolt13 = charger.get('BattData')[12][0][43]/1000.0,
        moduleCellVolt14 = charger.get('BattData')[12][0][44]/1000.0,
      )
