# Python bindings for the v4l2-dvb API

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# see linux/dvb/frontend.h
import fcntl
import ctypes
from v4l2 import _IOW, _IOR, _IO, enum

FE_QPSK = 0
FE_QAM = 1
FE_OFDM = 2
FE_ATSC = 3

FE_IS_STUPID = 0
FE_CAN_INVERSION_AUTO = 0x1
FE_CAN_FEC_1_2 = 0x2
FE_CAN_FEC_2_3 = 0x4
FE_CAN_FEC_3_4 = 0x8
FE_CAN_FEC_4_5 = 0x10
FE_CAN_FEC_5_6 = 0x20
FE_CAN_FEC_6_7 = 0x40
FE_CAN_FEC_7_8 = 0x80
FE_CAN_FEC_8_9 = 0x100
FE_CAN_FEC_AUTO = 0x200
FE_CAN_QPSK = 0x400
FE_CAN_QAM_16 = 0x800
FE_CAN_QAM_32 = 0x1000
FE_CAN_QAM_64 = 0x2000
FE_CAN_QAM_128 = 0x4000
FE_CAN_QAM_256 = 0x8000
FE_CAN_QAM_AUTO = 0x10000
FE_CAN_TRANSMISSION_MODE_AUTO = 0x20000
FE_CAN_BANDWIDTH_AUTO = 0x40000
FE_CAN_GUARD_INTERVAL_AUTO = 0x80000
FE_CAN_HIERARCHY_AUTO = 0x100000
FE_CAN_8VSB = 0x200000
FE_CAN_16VSB = 0x400000
FE_HAS_EXTENDED_CAPS = 0x800000
FE_CAN_TURBO_FEC = 0x8000000
FE_CAN_2G_MODULATION = 0x10000000
FE_NEEDS_BENDING = 0x20000000
FE_CAN_RECOVER = 0x40000000
FE_CAN_MUTE_TS = 0x80000000

class dvb_frontend_info(ctypes.Structure):
    _fields_ = [
        ('name', ctypes.c_char * 128),
        ('type', enum),
        ('frequency_min', ctypes.c_uint32),
        ('frequency_max', ctypes.c_uint32),
        ('frequency_stepsize', ctypes.c_uint32),
        ('frequency_tolerance', ctypes.c_uint32),
        ('symbol_rate_min', ctypes.c_uint32),
        ('symbol_rate_max', ctypes.c_uint32),
        ('symbol_rate_tolerance', ctypes.c_uint32),
        ('notifier_delay', ctypes.c_uint32),
        ('caps', enum),
    ]

class dvb_diseqc_master_cmd(ctypes.Structure):
    _fields_ = [
        ('msg', ctypes.c_uint8 * 6),
        ('msg_len', ctypes.c_uint8),
    ]

class dvb_diseqc_slave_reply(ctypes.Structure):
    _fields_ = [
        ('msg', ctypes.c_uint8 * 4),
        ('msg_len', ctypes.c_uint8),
        ('timeout', ctypes.c_int),
    ]

SEC_VOLTAGE_13 = 0
SEC_VOLTAGE_18 = 1
SEC_VOLTAGE_OFF = 2

SEC_TONE_ON = 0
SEC_TONE_OFF = 1

SEC_MINI_A = 0
SEC_MINI_B = 1

fe_status_t = enum
FE_HAS_SIGNAL = 0x01
FE_HAS_CARRIER = 0x02
FE_HAS_VITERBI = 0x04
FE_HAS_SYNC = 0x08
FE_HAS_LOCK = 0x10
FE_TIMEDOUT = 0x20
FE_REINIT = 0x40

INVERSION_OFF = 0
INVERSION_ON = 1
INVERSION_AUTO = 2

FEC_NONE = 0
FEC_1_2 = 1
FEC_2_3 = 2
FEC_3_4 = 3
FEC_4_5 = 4
FEC_5_6 = 5
FEC_6_7 = 6
FEC_7_8 = 7
FEC_8_9 = 8
FEC_AUTO = 9
FEC_3_5 = 10
FEC_9_10 = 11

QPSK = 0
QAM_16 = 1
QAM_32 = 2
QAM_64 = 3
QAM_128 = 4
QAM_256 = 5
QAM_AUTO = 6
VSB_8 = 7
VSB_16 = 8
PSK_8 = 9
APSK_16 = 10
APSK_32 = 11
DQPSK = 12

TRANSMISSION_MODE_2K = 0
TRANSMISSION_MODE_8K = 1
TRANSMISSION_MODE_AUTO = 2
TRANSMISSION_MODE_4K = 3

BANDWIDTH_8_MHZ = 0
BANDWIDTH_7_MHZ = 1
BANDWIDTH_6_MHZ = 2
BANDWIDTH_AUTO = 3

GUARD_INTERVAL_1_32 = 0
GUARD_INTERVAL_1_16 = 1
GUARD_INTERVAL_1_8 = 2
GUARD_INTERVAL_1_4 = 3
GUARD_INTERVAL_AUTO = 4

HIERARCHY_NONE = 0
HIERARCHY_1 = 1
HIERARCHY_2 = 2
HIERARCHY_4 = 3
HIERARCHY_AUTO = 4

class dvb_qpsk_parameters(ctypes.Structure):
    _fields_ = [
        ('symbol_rate', ctypes.c_uint32),
        ('fec_inner', enum),
    ]

class dvb_qam_parameters(ctypes.Structure):
    _fields_ = [
        ('symbol_rate', ctypes.c_uint32),
        ('fec_inner', enum),
        ('modulation', enum),
    ]

class dvb_vsb_parameters(ctypes.Structure):
    _fields_ = [
        ('modulation', enum),
    ]

class dvb_ofdm_parameters(ctypes.Structure):
    _fields_ = [
        ('bandwidth', enum),
        ('code_rate_HP', enum),
        ('code_rate_LP', enum),
        ('constellation', enum),
        ('transmission_mode', enum),
        ('guard_interval', enum),
        ('hierarchy_information', enum),
    ]

class _dvb_frontend_parameters_u(ctypes.Union):
    _fields_ = [
        ('qpsk', dvb_qpsk_parameters),
        ('qam', dvb_qam_parameters),
        ('vsb', dvb_vsb_parameters),
        ('ofdm', dvb_ofdm_parameters),
    ]

class dvb_frontend_parameters(ctypes.Structure):
    _fields_ = [
        ('frequency', ctypes.c_uint32),
        ('inversion', enum),
        ('u', _dvb_frontend_parameters_u),
    ]

class dvb_frontend_event(ctypes.Structure):
    _fields_ = [
        ('status', fe_status_t),
        ('parameters', dvb_frontend_parameters),
    ]

DTV_UNDEFINED = 0
DTV_TUNE = 1
DTV_CLEAR = 2
DTV_FREQUENCY = 3
DTV_MODULATION = 4
DTV_BANDWIDTH_HZ = 5
DTV_INVERSION = 6
DTV_DISEQC_MASTER = 7
DTV_SYMBOL_RATE = 8
DTV_INNER_FEC = 9
DTV_VOLTAGE = 10
DTV_TONE = 11
DTV_PILOT = 12
DTV_ROLLOFF = 13
DTV_DISEQC_SLAVE_REPLY = 14

DTV_FE_CAPABILITY_COUNT = 15
DTV_FE_CAPABILITY = 16
DTV_DELIVERY_SYSTEM = 17

DTV_ISDBT_PARTIAL_RECEPTION = 18
DTV_ISDBT_SOUND_BROADCASTING = 19

DTV_ISDBT_SB_SUBCHANNEL_ID = 20
DTV_ISDBT_SB_SEGMENT_IDX = 21
DTV_ISDBT_SB_SEGMENT_COUNT = 22

DTV_ISDBT_LAYERA_FEC = 23
DTV_ISDBT_LAYERA_MODULATION = 24
DTV_ISDBT_LAYERA_SEGMENT_COUNT = 25
DTV_ISDBT_LAYERA_TIME_INTERLEAVING = 26

DTV_ISDBT_LAYERB_FEC = 27
DTV_ISDBT_LAYERB_MODULATION = 28
DTV_ISDBT_LAYERB_SEGMENT_COUNT = 29
DTV_ISDBT_LAYERB_TIME_INTERLEAVING = 30

DTV_ISDBT_LAYERC_FEC = 31
DTV_ISDBT_LAYERC_MODULATION = 32
DTV_ISDBT_LAYERC_SEGMENT_COUNT = 33
DTV_ISDBT_LAYERC_TIME_INTERLEAVING = 34

DTV_API_VERSION = 35

DTV_CODE_RATE_HP = 36
DTV_CODE_RATE_LP = 37
DTV_GUARD_INTERVAL = 38
DTV_TRANSMISSION_MODE = 39
DTV_HIERARCHY = 40

DTV_ISDBT_LAYER_ENABLED = 41

DTV_ISDBS_TS_ID = 42

DTV_MAX_COMMAND = DTV_ISDBS_TS_ID

PILOT_ON = 0
PILOT_OFF = 1
PILOT_AUTO = 2

ROLLOFF_35 = 0
ROLLOFF_20 = 1
ROLLOFF_25 = 2
ROLLOFF_AUTO = 3

SYS_UNDEFINED = 0
SYS_DVBC_ANNEX_AC = 1
SYS_DVBC_ANNEX_B = 2
SYS_DVBT = 3
SYS_DSS = 4
SYS_DVBS = 5
SYS_DVBS2 = 6
SYS_DVBH = 7
SYS_ISDBT = 8
SYS_ISDBS = 9
SYS_ISDBC = 10
SYS_ATSC = 11
SYS_ATSCMH = 12
SYS_DMBTH = 13
SYS_CMMB = 14
SYS_DAB = 15

class dtv_cmds_h(ctypes.Structure):
    _fields_ = [
        ('name', ctypes.c_char_p),
        ('cmp', ctypes.c_uint32),
        ('set', ctypes.c_uint32, 1),
        ('buffer', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 30),
    ]

class _dtv_property_u_buffer(ctypes.Structure):
    _fields_ = [
        ('data', ctypes.c_uint8),
        ('len', ctypes.c_uint32),
        ('reserved1', ctypes.c_uint32 * 3),
        ('reserved2', ctypes.c_void_p),
    ]

class _dtv_property_u(ctypes.Union):
    _fields_ = [
        ('data', ctypes.c_uint32),
        ('buffer', _dtv_property_u_buffer),
    ]

class dtv_property(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
        ('cmd', ctypes.c_uint32),
        ('reserved', ctypes.c_uint32 * 3),
        ('u', _dtv_property_u),
        ('result', ctypes.c_int),
    ]

DTV_IOCTL_MAX_MSGS = 64

class dtv_properties(ctypes.Structure):
    _fields_ = [
        ('num', ctypes.c_uint32),
        ('props', ctypes.POINTER(dtv_property)),
    ]

FE_SET_PROPERTY	= _IOW('o', 82, dtv_properties)
FE_GET_PROPERTY = _IOR('o', 83, dtv_properties)

FE_TUNE_MODE_ONESHOT = 0x01

FE_GET_INFO = _IOR('o', 61, dvb_frontend_info)

FE_DISEQC_RESET_OVERLOAD = _IO('o', 62)
FE_DISEQC_SEND_MASTER_CMD = _IOW('o', 63, dvb_diseqc_master_cmd)
FE_DISEQC_RECV_SLAVE_REPLY = _IOR('o', 64, dvb_diseqc_slave_reply)
FE_DISEQC_SEND_BURST = _IO('o', 65)

FE_SET_TONE = _IO('o', 66)
FE_SET_VOLTAGE = _IO('o', 67)
FE_ENABLE_HIGH_LNB_VOLTAGE = _IO('o', 68)

FE_READ_STATUS = _IOR('o', 69, fe_status_t)
FE_READ_BER = _IOR('o', 70, ctypes.c_uint32)
FE_READ_SIGNAL_STRENGTH = _IOR('o', 71, ctypes.c_uint16)
FE_READ_SNR = _IOR('o', 72, ctypes.c_uint16)
FE_READ_UNCORRECTED_BLOCKS = _IOR('o', 73, ctypes.c_uint32)

FE_SET_FRONTEND = _IOW('o', 76, dvb_frontend_parameters)
FE_GET_FRONTEND = _IOR('o', 77, dvb_frontend_parameters)
FE_SET_FRONTEND_TUNE_MODE = _IO('o', 81)
FE_GET_EVENT = _IOR('o', 78, dvb_frontend_event)

FE_DISHNETWORK_SEND_LEGACY_CMD = _IO('o', 80)

# End of "raw" wrapper

class Frontend(object):
    # XXX: uses the 3.x API, should use 5.x (FE_[GS]ET_PROPERTY ioctl)
    def __init__(self, fd):
        self._fd = fd

    def _ioctlGet(self, query, c_type):
        result = c_type()
        fcntl.ioctl(self._fd, query, result)
        return result

    def getStatus(self):
        return self._ioctlGet(FE_READ_STATUS, fe_status_t).value

    def getBitErrorRate(self):
        return self._ioctlGet(FE_READ_BER, ctypes.c_uint32).value

    def getSignalNoiseRatio(self):
        return self._ioctlGet(FE_READ_SNR, ctypes.c_uint16).value

    def getSignalStrength(self):
        return self._ioctlGet(FE_READ_SIGNAL_STRENGTH, ctypes.c_uint16).value

    def getUncorrectedBlockCount(self):
        return self._ioctlGet(FE_READ_UNCORRECTED_BLOCKS, ctypes.c_uint32).value

    def getInfo(self):
        info = self._ioctlGet(FE_GET_INFO, dvb_frontend_info)
        return {
            'name': info.name,
            'frequency_min': info.frequency_min,
            'frequency_max': info.frequency_max,
            'frequency_stepsize': info.frequency_stepsize,
            'frequency_tolerance': info.frequency_tolerance,
            'symbol_rate_min': info.symbol_rate_min,
            'symbol_rate_max': info.symbol_rate_max,
            'symbol_rate_tolerance': info.symbol_rate_tolerance,
            'notifier_delay': info.notifier_delay,
            'caps': info.caps,
        }

    def _decodeBaseParameters(self, params):
        return {
            'frequency': params.frequency,
            'inversion': params.inversion,
        }

    def _decodeParameters(self, params):
        """
        Subclass to return more details.
        """
        return self._decodeBaseParameters(params)

    def _getTuning(self):
        return self._ioctlGet(FE_GET_FRONTEND, dvb_frontend_parameters)

    def _getEvent(self):
        event = self._ioctlGet(FE_GET_EVENT, dvb_frontend_event)
        return (event.status, event.parameters)

    def _tune(self, params):
        fcntl.ioctl(self._fd, FE_SET_FRONTEND, params)

    def getTuning(self):
        return self._decodeParameters(self._getTuning())

    def getEvent(self):
        raise NotImplementedError

    def tune(self, frequency, inversion=INVERSION_AUTO, **kw):
        raise NotImplementedError

class TerrestrialFrontend(Frontend):
    def _decodeParameters(self, params):
        result = self._decodeBaseParameters(params)
        u = params.u.ofdm
        result['bandwidth'] = u.bandwidth
        result['code_rate_hp'] = u.code_rate_HP
        result['code_rate_lp'] = u.code_rate_LP
        result['constellaton'] = u.constellation
        result['transmition_mode'] = u.transmission_mode
        result['guard_interval'] = u.guard_interval
        result['hierarchy'] = u.hierarchy_information
        return result

    def getEvent(self):
        status, params = self._getEvent()
        return status, self._decodeParameters(params)

    def tune(self, frequency, inversion=INVERSION_AUTO,
            bandwidth=BANDWIDTH_AUTO, code_rate_hp=FEC_AUTO,
            code_rate_lp=FEC_AUTO, constellaton=QAM_AUTO,
            transmition_mode=TRANSMISSION_MODE_AUTO,
            guard_interval=GUARD_INTERVAL_AUTO,
            hierarchy=HIERARCHY_AUTO):
        params = dvb_frontend_parameters()
        params.frequency = frequency
        params.inversion = inversion
        u = params.u.ofdm
        u.bandwidth = bandwidth
        u.code_rate_HP = code_rate_hp
        u.code_rate_LP = code_rate_lp
        u.constellation = constellaton
        u.transmission_mode = transmition_mode
        u.guard_interval = guard_interval
        u.hierarchy_information = hierarchy
        self._tune(params)

