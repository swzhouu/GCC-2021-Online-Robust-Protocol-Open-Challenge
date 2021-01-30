from enum import Enum

import general

# 4 bytes for scu header
# 32bits

# 8 bits for type needs 2 bits, 6 bits free
# 16 bits for id 11bitsあればよい, 5 bits free
# 8 bits for seq 256あれば十分、そのままやんけ

# 11 bits for free

# 0                   1                   2                   3
# 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# |      typ      |              id               |      seq      |    resendID   |
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#  
#               Custom Sequence Control on UDP Header
# - typ      :
# - id       : file number
# - seq      : 
# - resendID : enabled when 1-255. unabled when 0.

# 1 byte
class SCUPacketType(Enum):
    Data = 0 # data, fileID, seqno
    DataEnd = 1 # end of the data, fileID, seqno
    Rtr = 2 # retry request, fileID, null, resendID // list of seqs in body
    Fin = 3 # file完成したよ, fileID, null
    End = 4

class SCUHeader:
    def __init__(self, id=None, seq=None):
        self.id = id
        self.seq = seq
    def from_raw(self, raw):
        self.typ = int.from_bytes(raw[0:1], "big")
        self.id = int.from_bytes(raw[1:3], "big")
        self.seq = int.from_bytes(raw[3:4], "big")
        self.resendID = int.from_bytes(raw[4:5], "big")
        # print(int.from_bytes(raw, "big"))
        # print(raw, self.typ, self.id, self.seq)

    def raw(self):
        raw = self.typ.to_bytes(1, "big")
        raw += self.id.to_bytes(2, "big")
        raw += self.seq.to_bytes(1, "big")
        raw += self.resendID.to_bytes(1, "big")
        return raw

    def from_dict(self, dict):
        self.typ = dict["typ"]
        self.id = dict["id"]
        self.seq = dict["seq"]
        self.resendID = dict["resendID"]

class SCUPacket:
    def __init__(self, header=SCUHeader(), payload=b""):
        self.header = header
        self.payload = payload

    def from_raw(self, raw):
        header = SCUHeader()
        header.from_raw(raw[0:general.SCU_HEADER_LENGTH])
        self.header = header
        self.payload = raw[general.SCU_HEADER_LENGTH:]

    def raw(self):
        raw = self.header.raw()
        raw += self.payload
        return raw

    def from_dict(self, dict):
        self.header = dict["header"]
        self.payload = dict["payload"]
