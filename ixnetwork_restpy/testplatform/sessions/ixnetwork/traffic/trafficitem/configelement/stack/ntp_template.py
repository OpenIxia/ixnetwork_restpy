from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Ntp(Base):
    __slots__ = ()
    _SDM_NAME = "ntp"
    _SDM_ATT_MAP = {
        "Leapindicator": "ntp.header.leapindicator-1",
        "Version": "ntp.header.version-2",
        "Mode": "ntp.header.mode-3",
        "Stratum": "ntp.header.stratum-4",
        "Pollinterval": "ntp.header.pollinterval-5",
        "Precision": "ntp.header.precision-6",
        "Rootdelay": "ntp.header.rootdelay-7",
        "Rootdispersion": "ntp.header.rootdispersion-8",
        "Referenceclockidentifier": "ntp.header.referenceclockidentifier-9",
        "Referencetimestamp": "ntp.header.referencetimestamp-10",
        "Originatetimestamp": "ntp.header.originatetimestamp-11",
        "Receivetimestamp": "ntp.header.receivetimestamp-12",
        "Transmittimestamp": "ntp.header.transmittimestamp-13",
        "ExtensionFieldtype": "ntp.header.extension.fieldtype-14",
        "ExtensionLength": "ntp.header.extension.length-15",
        "ExtensionValue": "ntp.header.extension.value-16",
        "ExtensionPad": "ntp.header.extension.pad-17",
        "AuthenticationKeyID": "ntp.header.authentication.keyID-18",
        "AuthenticationMessegeauthenticationcode": "ntp.header.authentication.messegeauthenticationcode-19",
    }

    def __init__(self, parent, list_op=False):
        super(Ntp, self).__init__(parent, list_op)

    @property
    def Leapindicator(self):
        """
        Display Name: NTP-Leap-Indicator
        Default Value: 0
        Value Format: decimal
        Available enum values: No warning, 0, Last minute has 61 seconds, 1, Last minute has 59 seconds, 2, Alarm condition, clock not synchronized, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Leapindicator"]))

    @property
    def Version(self):
        """
        Display Name: NTP-Version
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Version"]))

    @property
    def Mode(self):
        """
        Display Name: NTP-Mode
        Default Value: 5
        Value Format: decimal
        Available enum values: reserved, 0, Symmetric active, 1, Symmetric passive, 2, Client, 3, Server, 4, Broadcast, 5, NTP control message, 6, private use, 7
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mode"]))

    @property
    def Stratum(self):
        """
        Display Name: NTP-Stratum
        Default Value: 2
        Value Format: decimal
        Available enum values: unspecified, 0, Primary Server, 1, secondary server, 2, secondary server, 3, secondary server, 4, secondary server, 5, secondary server, 6, secondary server, 7, secondary server, 8, secondary server, 9, secondary server, 10, secondary server, 11, secondary server, 12, secondary server, 13, secondary server, 14, secondary server, 15, unsynchronized, 16, reserved, 17, reserved, 18, reserved, 19, reserved, 20, reserved, 21, reserved, 22, reserved, 23, reserved, 24, reserved, 25, reserved, 26, reserved, 27, reserved, 28, reserved, 29, reserved, 30, reserved, 31, reserved, 32, reserved, 33, reserved, 34, reserved, 35, reserved, 36, reserved, 37, reserved, 38, reserved, 39, reserved, 40, reserved, 41, reserved, 42, reserved, 43, reserved, 44, reserved, 45, reserved, 46, reserved, 47, reserved, 48, reserved, 49, reserved, 50, reserved, 51, reserved, 52, reserved, 53, reserved, 54, reserved, 55, reserved, 56, reserved, 57, reserved, 58, reserved, 59, reserved, 60, reserved, 61, reserved, 62, reserved, 63, reserved, 64, reserved, 65, reserved, 66, reserved, 67, reserved, 68, reserved, 69, reserved, 70, reserved, 71, reserved, 72, reserved, 73, reserved, 74, reserved, 75, reserved, 76, reserved, 77, reserved, 78, reserved, 79, reserved, 80, reserved, 81, reserved, 82, reserved, 83, reserved, 84, reserved, 85, reserved, 86, reserved, 87, reserved, 88, reserved, 89, reserved, 90, reserved, 91, reserved, 92, reserved, 93, reserved, 94, reserved, 95, reserved, 96, reserved, 97, reserved, 98, reserved, 99, reserved, 100, reserved, 101, reserved, 102, reserved, 103, reserved, 104, reserved, 105, reserved, 106, reserved, 107, reserved, 108, reserved, 109, reserved, 110, reserved, 111, reserved, 112, reserved, 113, reserved, 114, reserved, 115, reserved, 116, reserved, 117, reserved, 118, reserved, 119, reserved, 120, reserved, 121, reserved, 122, reserved, 123, reserved, 124, reserved, 125, reserved, 126, reserved, 127, reserved, 128, reserved, 129, reserved, 130, reserved, 131, reserved, 132, reserved, 133, reserved, 134, reserved, 135, reserved, 136, reserved, 137, reserved, 138, reserved, 139, reserved, 140, reserved, 141, reserved, 142, reserved, 143, reserved, 144, reserved, 145, reserved, 146, reserved, 147, reserved, 148, reserved, 149, reserved, 150, reserved, 151, reserved, 152, reserved, 153, reserved, 154, reserved, 155, reserved, 156, reserved, 157, reserved, 158, reserved, 159, reserved, 160, reserved, 161, reserved, 162, reserved, 163, reserved, 164, reserved, 165, reserved, 166, reserved, 167, reserved, 168, reserved, 169, reserved, 170, reserved, 171, reserved, 172, reserved, 173, reserved, 174, reserved, 175, reserved, 176, reserved, 177, reserved, 178, reserved, 179, reserved, 180, reserved, 181, reserved, 182, reserved, 183, reserved, 184, reserved, 185, reserved, 186, reserved, 187, reserved, 188, reserved, 189, reserved, 190, reserved, 191, reserved, 192, reserved, 193, reserved, 194, reserved, 195, reserved, 196, reserved, 197, reserved, 198, reserved, 199, reserved, 200, reserved, 201, reserved, 202, reserved, 203, reserved, 204, reserved, 205, reserved, 206, reserved, 207, reserved, 208, reserved, 209, reserved, 210, reserved, 211, reserved, 212, reserved, 213, reserved, 214, reserved, 215, reserved, 216, reserved, 217, reserved, 218, reserved, 219, reserved, 220, reserved, 221, reserved, 222, reserved, 223, reserved, 224, reserved, 225, reserved, 226, reserved, 227, reserved, 228, reserved, 229, reserved, 230, reserved, 231, reserved, 232, reserved, 233, reserved, 234, reserved, 235, reserved, 236, reserved, 237, reserved, 238, reserved, 239, reserved, 240, reserved, 241, reserved, 242, reserved, 243, reserved, 244, reserved, 245, reserved, 246, reserved, 247, reserved, 248, reserved, 249, reserved, 250, reserved, 251, reserved, 252, reserved, 253, reserved, 254, reserved, 255
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Stratum"]))

    @property
    def Pollinterval(self):
        """
        Display Name: NTP-Poll-interval
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Pollinterval"]))

    @property
    def Precision(self):
        """
        Display Name: NTP-Precision
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Precision"]))

    @property
    def Rootdelay(self):
        """
        Display Name: NTP-Root-delay
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Rootdelay"]))

    @property
    def Rootdispersion(self):
        """
        Display Name: NTP-Root-dispersion
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Rootdispersion"])
        )

    @property
    def Referenceclockidentifier(self):
        """
        Display Name: NTP-Reference-clock-identifier
        Default Value: 66.129.255.62
        Value Format: iPv4
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Referenceclockidentifier"])
        )

    @property
    def Referencetimestamp(self):
        """
        Display Name: NTP-Reference-timestamp
        Default Value: dcf600cdcc0bb5e3
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Referencetimestamp"])
        )

    @property
    def Originatetimestamp(self):
        """
        Display Name: NTP-Originate-timestamp
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Originatetimestamp"])
        )

    @property
    def Receivetimestamp(self):
        """
        Display Name: NTP-Receive-timestamp
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Receivetimestamp"])
        )

    @property
    def Transmittimestamp(self):
        """
        Display Name: NTP-Transmit-timestamp
        Default Value: dcf6018392f23852
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Transmittimestamp"])
        )

    @property
    def ExtensionFieldtype(self):
        """
        Display Name: Field-Type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExtensionFieldtype"])
        )

    @property
    def ExtensionLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExtensionLength"])
        )

    @property
    def ExtensionValue(self):
        """
        Display Name: Value
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExtensionValue"])
        )

    @property
    def ExtensionPad(self):
        """
        Display Name: Padding
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ExtensionPad"]))

    @property
    def AuthenticationKeyID(self):
        """
        Display Name: NTP-Key-ID
        Default Value: 00000001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AuthenticationKeyID"])
        )

    @property
    def AuthenticationMessegeauthenticationcode(self):
        """
        Display Name: Messege Authentication Code
        Default Value: baba36aa86177599595cecceb1d17367
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["AuthenticationMessegeauthenticationcode"]
            ),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
