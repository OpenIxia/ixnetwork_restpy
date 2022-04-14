# MIT LICENSE
#
# Copyright 1997 - 2020 by IXIA Keysight
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import sys
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files

if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class PassCriteria(Base):
    """This object, if true, enables IxNetwork to apply the Pass Criteria to each trial in the test and determines whether the trial passed or failed.
    The PassCriteria class encapsulates a required passCriteria resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "passCriteria"
    _SDM_ATT_MAP = {
        "DataErrorThresholdMode": "dataErrorThresholdMode",
        "DataErrorThresholdValue": "dataErrorThresholdValue",
        "EnableDataIntegrityPassFail": "enableDataIntegrityPassFail",
        "EnableFrameLossPassFail": "enableFrameLossPassFail",
        "EnableLatencyPassFail": "enableLatencyPassFail",
        "EnablePassFail": "enablePassFail",
        "EnableRatePassFail": "enableRatePassFail",
        "EnableSequenceErrorsPassFail": "enableSequenceErrorsPassFail",
        "EnableStandardDeviationPassFail": "enableStandardDeviationPassFail",
        "LatencyThresholdMode": "latencyThresholdMode",
        "LatencyThresholdScale": "latencyThresholdScale",
        "LatencyThresholdValue": "latencyThresholdValue",
        "LatencyVarThresholdMode": "latencyVarThresholdMode",
        "LatencyVariationThresholdScale": "latencyVariationThresholdScale",
        "LatencyVariationThresholdValue": "latencyVariationThresholdValue",
        "LossThresholdMode": "lossThresholdMode",
        "LossThresholdValue": "lossThresholdValue",
        "PassCriteriaLoadRateMode": "passCriteriaLoadRateMode",
        "PassCriteriaLoadRateScale": "passCriteriaLoadRateScale",
        "PassCriteriaLoadRateValue": "passCriteriaLoadRateValue",
        "PassFailFrequency": "passFailFrequency",
        "SeqErrorsThresholdMode": "seqErrorsThresholdMode",
        "SeqErrorsThresholdValue": "seqErrorsThresholdValue",
    }
    _SDM_ENUM_MAP = {
        "dataErrorThresholdMode": ["average", "maximum"],
        "latencyThresholdMode": ["average", "maximum"],
        "latencyThresholdScale": ["ms", "ns", "us"],
        "latencyVarThresholdMode": ["average", "maximum"],
        "latencyVariationThresholdScale": ["ms", "ns", "us"],
        "lossThresholdMode": ["average", "maximum"],
        "passCriteriaLoadRateMode": ["average", "minimum"],
        "passCriteriaLoadRateScale": ["fps", "gbps", "kbps", "mbps", "percent"],
        "passFailFrequency": ["framesizes", "trials"],
        "seqErrorsThresholdMode": ["average", "maximum"],
    }

    def __init__(self, parent, list_op=False):
        super(PassCriteria, self).__init__(parent, list_op)

    @property
    def DataErrorThresholdMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(average | maximum): The threshold mode for the data error.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DataErrorThresholdMode"])

    @DataErrorThresholdMode.setter
    def DataErrorThresholdMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DataErrorThresholdMode"], value)

    @property
    def DataErrorThresholdValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The data error threshold value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DataErrorThresholdValue"])

    @DataErrorThresholdValue.setter
    def DataErrorThresholdValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["DataErrorThresholdValue"], value)

    @property
    def EnableDataIntegrityPassFail(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables the checking of data integrity for the pass or fail of the trial.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableDataIntegrityPassFail"])

    @EnableDataIntegrityPassFail.setter
    def EnableDataIntegrityPassFail(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableDataIntegrityPassFail"], value)

    @property
    def EnableFrameLossPassFail(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables the checking of frame loss for the pass or fail of the trial.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableFrameLossPassFail"])

    @EnableFrameLossPassFail.setter
    def EnableFrameLossPassFail(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableFrameLossPassFail"], value)

    @property
    def EnableLatencyPassFail(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables latency at which trails pass or fail.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableLatencyPassFail"])

    @EnableLatencyPassFail.setter
    def EnableLatencyPassFail(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableLatencyPassFail"], value)

    @property
    def EnablePassFail(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, IxNetwork applies the Pass Criteria to each trial in the test and determines whether the trial passed or failed.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnablePassFail"])

    @EnablePassFail.setter
    def EnablePassFail(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnablePassFail"], value)

    @property
    def EnableRatePassFail(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables the rate of pass or failure of the trial.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableRatePassFail"])

    @EnableRatePassFail.setter
    def EnableRatePassFail(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableRatePassFail"], value)

    @property
    def EnableSequenceErrorsPassFail(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, sets the amount of time required by the DUT to forward frames and the sequence errors for the pass or fail of the trial.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableSequenceErrorsPassFail"])

    @EnableSequenceErrorsPassFail.setter
    def EnableSequenceErrorsPassFail(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableSequenceErrorsPassFail"], value)

    @property
    def EnableStandardDeviationPassFail(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables standard deviation in the pass or failure of the trial.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableStandardDeviationPassFail"])

    @EnableStandardDeviationPassFail.setter
    def EnableStandardDeviationPassFail(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableStandardDeviationPassFail"], value)

    @property
    def LatencyThresholdMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(average | maximum): The threshold latency mode value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LatencyThresholdMode"])

    @LatencyThresholdMode.setter
    def LatencyThresholdMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LatencyThresholdMode"], value)

    @property
    def LatencyThresholdScale(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ms | ns | us): The latency threshold scale value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LatencyThresholdScale"])

    @LatencyThresholdScale.setter
    def LatencyThresholdScale(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LatencyThresholdScale"], value)

    @property
    def LatencyThresholdValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The latency threshold value of the test.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LatencyThresholdValue"])

    @LatencyThresholdValue.setter
    def LatencyThresholdValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LatencyThresholdValue"], value)

    @property
    def LatencyVarThresholdMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(average | maximum): The threshold mode for the latency variation.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LatencyVarThresholdMode"])

    @LatencyVarThresholdMode.setter
    def LatencyVarThresholdMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LatencyVarThresholdMode"], value)

    @property
    def LatencyVariationThresholdScale(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ms | ns | us): signifies the latency variation in the threshold scale.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LatencyVariationThresholdScale"])

    @LatencyVariationThresholdScale.setter
    def LatencyVariationThresholdScale(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LatencyVariationThresholdScale"], value)

    @property
    def LatencyVariationThresholdValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: signifies the latency variation in the threshold value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LatencyVariationThresholdValue"])

    @LatencyVariationThresholdValue.setter
    def LatencyVariationThresholdValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LatencyVariationThresholdValue"], value)

    @property
    def LossThresholdMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(average | maximum): Signifies threshold mode of the frame loss.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LossThresholdMode"])

    @LossThresholdMode.setter
    def LossThresholdMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LossThresholdMode"], value)

    @property
    def LossThresholdValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Denotes the loss in threshold value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LossThresholdValue"])

    @LossThresholdValue.setter
    def LossThresholdValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LossThresholdValue"], value)

    @property
    def PassCriteriaLoadRateMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(average | minimum): The Pass Criteria per trial rate at which the DUT should be able to transmit and receive, expressed as a percentage of the maximum theoretical line speed or in terms of frames per second.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PassCriteriaLoadRateMode"])

    @PassCriteriaLoadRateMode.setter
    def PassCriteriaLoadRateMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PassCriteriaLoadRateMode"], value)

    @property
    def PassCriteriaLoadRateScale(self):
        # type: () -> str
        """
        Returns
        -------
        - str(fps | gbps | kbps | mbps | percent): The load rate scale for the Pass Criteria per trial.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PassCriteriaLoadRateScale"])

    @PassCriteriaLoadRateScale.setter
    def PassCriteriaLoadRateScale(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PassCriteriaLoadRateScale"], value)

    @property
    def PassCriteriaLoadRateValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The load rate value for the Pass Criteria per trial.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PassCriteriaLoadRateValue"])

    @PassCriteriaLoadRateValue.setter
    def PassCriteriaLoadRateValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["PassCriteriaLoadRateValue"], value)

    @property
    def PassFailFrequency(self):
        # type: () -> str
        """
        Returns
        -------
        - str(framesizes | trials): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["PassFailFrequency"])

    @PassFailFrequency.setter
    def PassFailFrequency(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PassFailFrequency"], value)

    @property
    def SeqErrorsThresholdMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(average | maximum): The sequence error value for the threshold mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SeqErrorsThresholdMode"])

    @SeqErrorsThresholdMode.setter
    def SeqErrorsThresholdMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["SeqErrorsThresholdMode"], value)

    @property
    def SeqErrorsThresholdValue(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The value for the sequence error threshold.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SeqErrorsThresholdValue"])

    @SeqErrorsThresholdValue.setter
    def SeqErrorsThresholdValue(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SeqErrorsThresholdValue"], value)

    def update(
        self,
        DataErrorThresholdMode=None,
        DataErrorThresholdValue=None,
        EnableDataIntegrityPassFail=None,
        EnableFrameLossPassFail=None,
        EnableLatencyPassFail=None,
        EnablePassFail=None,
        EnableRatePassFail=None,
        EnableSequenceErrorsPassFail=None,
        EnableStandardDeviationPassFail=None,
        LatencyThresholdMode=None,
        LatencyThresholdScale=None,
        LatencyThresholdValue=None,
        LatencyVarThresholdMode=None,
        LatencyVariationThresholdScale=None,
        LatencyVariationThresholdValue=None,
        LossThresholdMode=None,
        LossThresholdValue=None,
        PassCriteriaLoadRateMode=None,
        PassCriteriaLoadRateScale=None,
        PassCriteriaLoadRateValue=None,
        PassFailFrequency=None,
        SeqErrorsThresholdMode=None,
        SeqErrorsThresholdValue=None,
    ):
        # type: (str, int, bool, bool, bool, bool, bool, bool, bool, str, str, int, str, str, int, str, int, str, str, int, str, str, int) -> PassCriteria
        """Updates passCriteria resource on the server.

        Args
        ----
        - DataErrorThresholdMode (str(average | maximum)): The threshold mode for the data error.
        - DataErrorThresholdValue (number): The data error threshold value.
        - EnableDataIntegrityPassFail (bool): If true, enables the checking of data integrity for the pass or fail of the trial.
        - EnableFrameLossPassFail (bool): If true, enables the checking of frame loss for the pass or fail of the trial.
        - EnableLatencyPassFail (bool): If true, enables latency at which trails pass or fail.
        - EnablePassFail (bool): If true, IxNetwork applies the Pass Criteria to each trial in the test and determines whether the trial passed or failed.
        - EnableRatePassFail (bool): If true, enables the rate of pass or failure of the trial.
        - EnableSequenceErrorsPassFail (bool): If true, sets the amount of time required by the DUT to forward frames and the sequence errors for the pass or fail of the trial.
        - EnableStandardDeviationPassFail (bool): If true, enables standard deviation in the pass or failure of the trial.
        - LatencyThresholdMode (str(average | maximum)): The threshold latency mode value.
        - LatencyThresholdScale (str(ms | ns | us)): The latency threshold scale value.
        - LatencyThresholdValue (number): The latency threshold value of the test.
        - LatencyVarThresholdMode (str(average | maximum)): The threshold mode for the latency variation.
        - LatencyVariationThresholdScale (str(ms | ns | us)): signifies the latency variation in the threshold scale.
        - LatencyVariationThresholdValue (number): signifies the latency variation in the threshold value.
        - LossThresholdMode (str(average | maximum)): Signifies threshold mode of the frame loss.
        - LossThresholdValue (number): Denotes the loss in threshold value.
        - PassCriteriaLoadRateMode (str(average | minimum)): The Pass Criteria per trial rate at which the DUT should be able to transmit and receive, expressed as a percentage of the maximum theoretical line speed or in terms of frames per second.
        - PassCriteriaLoadRateScale (str(fps | gbps | kbps | mbps | percent)): The load rate scale for the Pass Criteria per trial.
        - PassCriteriaLoadRateValue (number): The load rate value for the Pass Criteria per trial.
        - PassFailFrequency (str(framesizes | trials)): NOT DEFINED
        - SeqErrorsThresholdMode (str(average | maximum)): The sequence error value for the threshold mode.
        - SeqErrorsThresholdValue (number): The value for the sequence error threshold.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        DataErrorThresholdMode=None,
        DataErrorThresholdValue=None,
        EnableDataIntegrityPassFail=None,
        EnableFrameLossPassFail=None,
        EnableLatencyPassFail=None,
        EnablePassFail=None,
        EnableRatePassFail=None,
        EnableSequenceErrorsPassFail=None,
        EnableStandardDeviationPassFail=None,
        LatencyThresholdMode=None,
        LatencyThresholdScale=None,
        LatencyThresholdValue=None,
        LatencyVarThresholdMode=None,
        LatencyVariationThresholdScale=None,
        LatencyVariationThresholdValue=None,
        LossThresholdMode=None,
        LossThresholdValue=None,
        PassCriteriaLoadRateMode=None,
        PassCriteriaLoadRateScale=None,
        PassCriteriaLoadRateValue=None,
        PassFailFrequency=None,
        SeqErrorsThresholdMode=None,
        SeqErrorsThresholdValue=None,
    ):
        # type: (str, int, bool, bool, bool, bool, bool, bool, bool, str, str, int, str, str, int, str, int, str, str, int, str, str, int) -> PassCriteria
        """Finds and retrieves passCriteria resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve passCriteria resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all passCriteria resources from the server.

        Args
        ----
        - DataErrorThresholdMode (str(average | maximum)): The threshold mode for the data error.
        - DataErrorThresholdValue (number): The data error threshold value.
        - EnableDataIntegrityPassFail (bool): If true, enables the checking of data integrity for the pass or fail of the trial.
        - EnableFrameLossPassFail (bool): If true, enables the checking of frame loss for the pass or fail of the trial.
        - EnableLatencyPassFail (bool): If true, enables latency at which trails pass or fail.
        - EnablePassFail (bool): If true, IxNetwork applies the Pass Criteria to each trial in the test and determines whether the trial passed or failed.
        - EnableRatePassFail (bool): If true, enables the rate of pass or failure of the trial.
        - EnableSequenceErrorsPassFail (bool): If true, sets the amount of time required by the DUT to forward frames and the sequence errors for the pass or fail of the trial.
        - EnableStandardDeviationPassFail (bool): If true, enables standard deviation in the pass or failure of the trial.
        - LatencyThresholdMode (str(average | maximum)): The threshold latency mode value.
        - LatencyThresholdScale (str(ms | ns | us)): The latency threshold scale value.
        - LatencyThresholdValue (number): The latency threshold value of the test.
        - LatencyVarThresholdMode (str(average | maximum)): The threshold mode for the latency variation.
        - LatencyVariationThresholdScale (str(ms | ns | us)): signifies the latency variation in the threshold scale.
        - LatencyVariationThresholdValue (number): signifies the latency variation in the threshold value.
        - LossThresholdMode (str(average | maximum)): Signifies threshold mode of the frame loss.
        - LossThresholdValue (number): Denotes the loss in threshold value.
        - PassCriteriaLoadRateMode (str(average | minimum)): The Pass Criteria per trial rate at which the DUT should be able to transmit and receive, expressed as a percentage of the maximum theoretical line speed or in terms of frames per second.
        - PassCriteriaLoadRateScale (str(fps | gbps | kbps | mbps | percent)): The load rate scale for the Pass Criteria per trial.
        - PassCriteriaLoadRateValue (number): The load rate value for the Pass Criteria per trial.
        - PassFailFrequency (str(framesizes | trials)): NOT DEFINED
        - SeqErrorsThresholdMode (str(average | maximum)): The sequence error value for the threshold mode.
        - SeqErrorsThresholdValue (number): The value for the sequence error threshold.

        Returns
        -------
        - self: This instance with matching passCriteria resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of passCriteria data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the passCriteria resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Apply(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the apply operation on the server.

        Applies the specified Quick Test.

        apply(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("apply", payload=payload, response_object=None)

    def ApplyAsync(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the applyAsync operation on the server.

        applyAsync(async_operation=bool)
        --------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("applyAsync", payload=payload, response_object=None)

    def ApplyAsyncResult(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the applyAsyncResult operation on the server.

        applyAsyncResult(async_operation=bool)bool
        ------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool:

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("applyAsyncResult", payload=payload, response_object=None)

    def ApplyITWizardConfiguration(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the applyITWizardConfiguration operation on the server.

        Applies the specified Quick Test.

        applyITWizardConfiguration(async_operation=bool)
        ------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "applyITWizardConfiguration", payload=payload, response_object=None
        )

    def GenerateReport(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the generateReport operation on the server.

        Generate a PDF report for the last succesfull test run.

        generateReport(async_operation=bool)string
        ------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: This method is asynchronous and has no return value.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("generateReport", payload=payload, response_object=None)

    def Run(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the run operation on the server.

        Starts the specified Quick Test and waits for its execution to finish.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        run(async_operation=bool)list
        -----------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This method is synchronous and returns the result of the test.

        run(InputParameters=string, async_operation=bool)list
        -----------------------------------------------------
        - InputParameters (str): The input arguments of the test.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This method is synchronous and returns the result of the test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("run", payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        Starts the specified Quick Test.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        start(InputParameters=string, async_operation=bool)
        ---------------------------------------------------
        - InputParameters (str): The input arguments of the test.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("start", payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stop operation on the server.

        Stops the currently running Quick Test.

        stop(async_operation=bool)
        --------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("stop", payload=payload, response_object=None)

    def WaitForTest(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the waitForTest operation on the server.

        Waits for the execution of the specified Quick Test to be completed.

        waitForTest(async_operation=bool)list
        -------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This method is synchronous and returns the result of the test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("waitForTest", payload=payload, response_object=None)
