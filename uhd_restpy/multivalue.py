# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
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
from uhd_restpy.base import Base


class Multivalue(Base):
    """Multivalue class
    Significant changes has been done in this class to accommodate code for config assistant.
    Each multivalue pattern has code for protocols and traffic side in its function
    """

    def __init__(self, parent, href):
        """Multivalue constructor

        Encapsulates a multivalue property.
        """
        super(Multivalue, self).__init__(parent)
        self._href = href
        self._pattern = None
        self._pattern_type = ""
        self._dirty = False
        self.parent_href = ""
        self._multiValueObj = {"multiValue": []}
        if self._mode[0] == "config":
            if "href" in parent._properties:
                self._dirty = True
                self.parent_href = parent._properties["href"]
                if self.parent_href not in self._dirty_objs:
                    self._dirty_objs[self.parent_href] = []
                    self._dirty_objs[self.parent_href].append(self._multiValueObj)
                else:
                    multivalue_present = False
                    for dirty_child in self._dirty_objs[self.parent_href]:
                        if "multiValue" in dirty_child.keys():
                            multivalue_present = True
                            self._multiValueObj = dirty_child

                    if not multivalue_present:
                        self._dirty_objs[self.parent_href].append(self._multiValueObj)

            elif "multiValue" not in parent._properties:
                parent._properties["multiValue"] = []
        # this over lay index is used by config assistant
        self._overlay_index = 0

    def _format_value(self, value):
        if self._properties["format"] == "bool":
            return "%s%s" % (value[0].upper(), value[1:])
        return value

    @property
    def Pattern(self):
        """
        Returns
        -------
        - str: the current pattern
        """
        if self._pattern is None:
            self._custom_select()
        if self._properties["pattern"] not in self._properties:
            self._custom_select()
        if self._properties["pattern"] == "singleValue":
            self._pattern = self._format_value(self._properties["singleValue"]["value"])
            self._pattern_type = "Single"
        elif self._properties["pattern"] == "counter":
            start = self._format_value(self._properties["counter"]["start"])
            step = self._format_value(self._properties["counter"]["step"])
            if self._properties["counter"]["direction"] == "decrement":
                self._pattern = "Dec: %s, %s" % (start, step)
                self._pattern_type = "Decrement"
            else:
                self._pattern = "Inc: %s, %s" % (start, step)
                self._pattern_type = "Increment"
        elif self._properties["pattern"] == "valueList":
            self._pattern = "List: %s" % (
                ", ".join(self._properties["valueList"]["values"])
            )
            self._pattern_type = "ValueList"
        elif self._properties["pattern"] == "repeatableRandomRange":
            min_value = self._properties["repeatableRandomRange"]["min"]
            max_value = self._properties["repeatableRandomRange"]["max"]
            step_value = self._properties["repeatableRandomRange"]["step"]
            seed = self._properties["repeatableRandomRange"]["seed"]
            self._pattern = "Randr: %s, %s, %s, %s" % (
                min_value,
                max_value,
                step_value,
                seed,
            )
            self._pattern_type = "RandomRange"
        elif self._properties["pattern"] == "repeatableRandom":
            fixed_value = self._properties["repeatableRandom"]["fixed"]
            mask_value = self._properties["repeatableRandom"]["mask"]
            seed = self._properties["repeatableRandom"]["seed"]
            count = self._properties["repeatableRandom"]["count"]
            self._pattern = "Randb: %s, %s, %s, %s" % (
                fixed_value,
                mask_value,
                seed,
                count,
            )
            self._pattern_type = "RandomMask"
        elif self._properties["pattern"] == "random":
            self._pattern = "Rand"
            self._pattern_type = "Random"
        elif self._properties["pattern"] == "alternate":
            self._pattern = "Alt: %s" % self._format_value(
                self._properties["alternate"]["value"]
            )
            self._pattern_type = "Alternate"
        elif self._properties["pattern"] == "customDistributed":
            values = []
            for value_pair in self._properties["customDistributed"]["values"]:
                values.append(
                    "(%s, %s)"
                    % (self._format_value(value_pair["arg1"]), value_pair["arg2"])
                )
            algorithm = self._properties["customDistributed"]["algorithm"]
            mode = self._properties["customDistributed"]["mode"]
            self._pattern = "Dist: %s, %s, [%s]" % (algorithm, mode, ",".join(values))
            self._pattern_type = "Distributed"
        elif self._properties["pattern"] == "custom":
            increments = []
            if "increment" in self._properties["custom"].keys():
                self._add_increments(
                    increments, self._properties["custom"]["increment"]
                )
            start = self._properties["custom"]["start"]
            step = self._properties["custom"]["step"]
            self._pattern = "Custom: %s, %s, [%s]" % (start, step, ",".join(increments))
            self._pattern_type = "Custom"
        elif self._properties["pattern"] == "string":
            self._pattern = self._properties["string"]["pattern"]
            self._pattern_type = "String"

        if self._pattern_type == "":
            raise Exception(
                "Could not retrieve Pattern type for the multivalue Instance"
            )

        return self._pattern

    def _add_increments(self, increments, increment):
        for item in increment:
            child_increments = []
            if "increment" in item.keys():
                self._add_increments(child_increments, item["increment"])
            increments.append(
                "(%s, %s, [%s])"
                % (item["value"], item["count"], ",".join(child_increments))
            )

    def __str__(self):
        return self.Pattern

    def __repr__(self):
        return self.Pattern

    def __eq__(self, other):
        return self.Pattern == other

    @property
    def PatternType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: a string containing information about the type for this Multivalue.
               possible return values (Alternate, Custom, Decrement, Distributed, Increment, Random, RandomRange,
               RandomMask, Single, String, ValueList)
        """
        self.Pattern
        return self._pattern_type

    @property
    def Info(self):
        """
        Returns
        -------
        - str: a formatted string of information for this multivalue
        """
        info = "Multivalue: %s\n" % self.Source
        info += "\tFormat: %s\n" % self.Format
        info += "\tCount: %s\n" % self.Count
        info += "\tValid Patterns: %s\n" % " ".join(self.AvailablePatterns)
        return info

    @property
    def Format(self):
        """
        Returns
        -------
        - str: the format of any values that are inputs to other multivalue methods
        """
        self.Pattern
        return self._properties["format"]

    @property
    def Source(self):
        """
        Returns
        -------
        - str: the source property the multivalue encapsulates
        """
        self.Pattern
        return self._properties["source"]

    @property
    def Count(self):
        """
        Returns
        -------
        - number: the number of values that the multivalue encapsulates
        """
        self.Pattern
        return self._properties["count"]

    @property
    def AvailablePatterns(self):
        """
        Returns
        -------
        - list(str): a list of patterns that indicate what methods can be used for this multivalue
        """
        self.Pattern
        for unsupported in ["shared", "subset"]:
            self._properties["availablePatterns"].remove(unsupported)
        return self._properties["availablePatterns"]

    @property
    def AvailableEnums(self):
        """
        Returns
        -------
        - list(str): if the format of the multivalue is enum this will return a list of possible enum choices that can be used when setting patterns
        """
        self.Pattern
        return self._properties["enums"]

    @property
    def Values(self):
        """
        Returns
        -------
        - list(str): a list of the str values which is dictated by the pattern, format and count properties
        """
        payload = {"arg1": self._href, "arg2": 0, "arg3": self.Count}
        return self._execute("getValues", payload=payload)

    def Single(self, value):
        """Sets the multivalue to a single value pattern

        Args
        ----
        - value (str): The single value according to the format property
        """
        if self._parent._mode[0] == "config":
            # multivalue_dict = dict()
            # if 'stack' in self._parent._properties['xpath']:
            #     multivalue_dict['xpath'] = self._get_field_multivalue_xpath(self._href)
            #     multivalue_dict['singleValue'] = value
            #     multivalue_dict['valueType'] = 'singleValue'
            #     multivalue_dict['auto'] = False
            #     multivalue_dict['optionalEnabled'] = True
            # else:
            #     multivalue_dict['xpath'] = self._get_multivalue_xpath(self._href, 'singleValue')
            #     multivalue_dict['value'] = value
            #
            # self._xpathObj._config.append(multivalue_dict)
            attr_list = ["singleValue", value]
            if "stack_index" in self._parent._properties:
                attr_list = ["field"] + attr_list
            if self._dirty:
                self._multiValueObj["multiValue"].append({self._href: attr_list})
            else:
                self._parent._properties["multiValue"].append({self._href: attr_list})
        else:
            self._set_pattern("singleValue", {"value": value})

    def Alternate(self, alternating_value):
        """Sets the multivalue pattern to an alternating pattern

        Args
        ----
        - alternating_value (str): An alternating pattern can only be a boolean.
        """
        if self._parent._mode[0] == "config":
            # multivalue_dict = dict()
            # multivalue_dict['xpath'] = self._get_multivalue_xpath(self._href, 'alternate')
            # multivalue_dict['value'] = alternating_value
            # self._xpathObj._config.append(multivalue_dict)
            self._parent._properties["multiValue"].append(
                {self._href: ["alternate", alternating_value]}
            )
        else:
            self._set_pattern("alternate", {"value": alternating_value})

    def Increment(self, start_value=None, step_value=None):
        """Sets the multivalue to an incrementing pattern

        Args
        ----
        - start_value (str): The value at which to begin incrementing
        - step_value (str): The value to increment by
        """
        if self._parent._mode[0] == "config":
            # multivalue_dict = dict()
            # if 'stack' in self._parent._properties['xpath']:
            #     multivalue_dict['xpath'] = self._get_field_multivalue_xpath(self._href)
            #     multivalue_dict['valueType'] = 'increment'
            #     multivalue_dict['auto'] = False
            #     multivalue_dict['optionalEnabled'] = True
            #     if start_value is not None:
            #         multivalue_dict['startValue'] = start_value
            #     if step_value is not None:
            #         multivalue_dict['stepValue'] = step_value
            # else:
            #     multivalue_dict['xpath'] = self._get_multivalue_xpath(self._href, 'counter')
            #     multivalue_dict['direction'] = 'increment'
            #     if start_value is not None:
            #         multivalue_dict['start'] = start_value
            #     if step_value is not None:
            #         multivalue_dict['step'] = step_value
            #
            # self._xpathObj._config.append(multivalue_dict)
            attr_list = ["counter", "increment", start_value, step_value]
            if "stack_index" in self._parent._properties:
                attr_list = ["field"] + attr_list
            if self._dirty:
                self._multiValueObj["multiValue"].append({self._href: attr_list})
            else:
                self._parent._properties["multiValue"].append({self._href: attr_list})
        else:
            payload = {"direction": "increment"}
            if start_value is not None:
                payload["start"] = start_value
            if step_value is not None:
                payload["step"] = step_value
            self._set_pattern("counter", payload)

    def Decrement(self, start_value=None, step_value=None):
        """Sets the multivalue to a decrementing pattern

        Args
        ----
        - start_value (str): The value at which to begin decrementing
        - step_value (str): The value to decrement by
        """
        if self._parent._mode[0] == "config":
            # multivalue_dict = dict()
            # if 'stack' in self._parent._properties['xpath']:
            #     multivalue_dict['xpath'] = self._get_field_multivalue_xpath(self._href)
            #     multivalue_dict['valueType'] = 'decrement'
            #     multivalue_dict['auto'] = False
            #     multivalue_dict['optionalEnabled'] = True
            #     if start_value is not None:
            #         multivalue_dict['startValue'] = start_value
            #     if step_value is not None:
            #         multivalue_dict['stepValue'] = step_value
            # else:
            #     multivalue_dict['xpath'] = self._get_multivalue_xpath(self._href, 'counter')
            #     multivalue_dict['direction'] = 'decrement'
            #     if start_value is not None:
            #         multivalue_dict['start'] = start_value
            #     if step_value is not None:
            #         multivalue_dict['step'] = step_value
            #
            # self._xpathObj._config.append(multivalue_dict)
            attr_list = ["counter", "decrement", start_value, step_value]
            if "stack_index" in self._parent._properties:
                attr_list = ["field"] + attr_list
            self._parent._properties["multiValue"].append({self._href: attr_list})
        else:
            payload = {"direction": "decrement"}
            if start_value is not None:
                payload["start"] = start_value
            if step_value is not None:
                payload["step"] = step_value
            self._set_pattern("counter", payload)

    def ValueList(self, values):
        """Sets the multivalue to a value list pattern

        Args
        ----
        - values (Union[list(str), str, IOBase]): Value list values.
            Each value in the value list must adhere to the format property of
            this object.

            If the type(values) is a list then it will be directly assigned
            to the valueList.

            If the type(values) is a str then it is assumed to be a filename
            and the file will be opened and the contents will be read from that
            file and assigned to the valueList.

            If the type(values) is an IOBase object then the contents will be
            read from that file object and the file object will not be closed.

            See the pytest_tests/multivalue_tests/test_multivalue_valuelist.py
            file in the package installation for an example of how to set the
            value list using the different methods.
        """
        if isinstance(values, list) is True:
            pass
        elif self._is_str(values) is True:
            with open(values, "r") as fp:
                values = [line.strip() for line in fp if line.strip()]
        else:
            values = [line.strip() for line in values if line.strip()]

        if self._parent._mode[0] == "config":
            # multivalue_dict = dict()
            # if 'stack' in self._parent._properties['xpath']:
            #     multivalue_dict['xpath'] = self._get_field_multivalue_xpath(self._href)
            #     multivalue_dict['valueType'] = 'valueList'
            #     multivalue_dict['valueList'] = values
            #     multivalue_dict['auto'] = False
            #     multivalue_dict['optionalEnabled'] = True
            # else:
            #     multivalue_dict['xpath'] = self._get_multivalue_xpath(self._href, 'valueList')
            #     multivalue_dict['values'] = values
            # self._xpathObj._config.append(multivalue_dict)

            attr_list = ["valueList", values]
            if "stack_index" in self._parent._properties:
                attr_list = ["field"] + attr_list
            self._parent._properties["multiValue"].append({self._href: attr_list})
        else:
            self._set_pattern("valueList", {"values": values})

    def RandomRange(self, min_value=None, max_value=None, step_value=None, seed=None):
        """Sets the multivalue to a repeatable random range pattern

        Args
        ----
        - min_value (str): Minimum value according to the format property
        - max_value (str): Maximum value according to the format property
        - step_value (str): Step value accoroding to the format property
        - seed (int): Seed value
        """
        if self._parent._mode[0] == "config":
            # multivalue_dict = dict()
            # if 'stack' in self._parent._properties['xpath']:
            #     multivalue_dict['xpath'] = self._get_field_multivalue_xpath(self._href)
            #     multivalue_dict['valueType'] = 'repeatableRandomRange'
            #     multivalue_dict['auto'] = False
            #     multivalue_dict['optionalEnabled'] = True
            #     if min_value is not None:
            #         multivalue_dict['minValue'] = min_value
            #     if max_value is not None:
            #         multivalue_dict['maxValue'] = max_value
            #     if seed is not None:
            #         multivalue_dict['seed'] = seed
            #     if step_value is not None:
            #         multivalue_dict['stepValue'] = step_value
            # else:
            #     multivalue_dict['xpath'] = self._get_multivalue_xpath(self._href, 'repeatableRandomRange')
            #     if min_value is not None:
            #         multivalue_dict['min'] = min_value
            #     if max_value is not None:
            #         multivalue_dict['max'] = max_value
            #     if seed is not None:
            #         multivalue_dict['seed'] = seed
            #     if step_value is not None:
            #         multivalue_dict['step'] = step_value
            # self._xpathObj._config.append(multivalue_dict)
            self._parent._properties["multiValue"].append(
                {
                    self._href: [
                        "repeatableRandomRange",
                        min_value,
                        max_value,
                        seed,
                        step_value,
                    ]
                }
            )
        else:
            payload = {
                "min": min_value,
                "max": max_value,
                "step": step_value,
                "seed": seed,
            }
            self._set_pattern("repeatableRandomRange", payload)

    def RandomMask(self, fixed_value=None, mask_value=None, seed=None, count=None):
        """Sets the multivalue to a repeatable random pattern

        Args
        ----
        - fixed_value (str): Minimum value according to the format property
        - mask_value (str): Maximum value according to the format property
        - seed (int): Seed value
        - count (int): Count value
        """
        if self._parent._mode[0] == "config":
            # multivalue_dict = dict()
            # if 'stack' in self._parent._properties['xpath']:
            #     multivalue_dict['xpath'] = self._get_field_multivalue_xpath(self._href)
            #     multivalue_dict['valueType'] = 'random'
            #     multivalue_dict['auto'] = False
            #     multivalue_dict['optionalEnabled'] = True
            #     if fixed_value is not None:
            #         multivalue_dict['fixedBits'] = fixed_value
            #     if mask_value is not None:
            #         multivalue_dict['randomMask'] = mask_value
            #     if seed is not None:
            #         multivalue_dict['seed'] = seed
            #     if count is not None:
            #         multivalue_dict['countValue'] = count
            # else:
            #     multivalue_dict['xpath'] = self._get_multivalue_xpath(self._href, 'repeatableRandom')
            #     if fixed_value is not None:
            #         multivalue_dict['fixed'] = fixed_value
            #     if mask_value is not None:
            #         multivalue_dict['mask'] = mask_value
            #     if seed is not None:
            #         multivalue_dict['seed'] = seed
            #     if count is not None:
            #         multivalue_dict['count'] = count
            # self._xpathObj._config.append(multivalue_dict)
            self._parent._properties["multiValue"].append(
                {self._href: ["repeatableRandom", fixed_value, mask_value, seed, count]}
            )
        else:
            payload = {
                "fixed": fixed_value,
                "mask": mask_value,
                "seed": seed,
                "count": count,
            }
            self._set_pattern("repeatableRandom", payload)

    def Random(self):
        """Sets the multivalue to a non-repeatable random pattern"""
        if self._parent._mode[0] == "config":
            # multivalue_dict = dict()
            # multivalue_dict['xpath'] = self._get_multivalue_xpath(self._href, 'random')
            # self._xpathObj._config.append(multivalue_dict)
            self._parent._properties["multiValue"].append({self._href: ["random"]})
        else:
            self._set_pattern("random")

    def Distributed(self, algorithm=None, mode=None, values=None):
        """Sets the multivalue to a custom distributed pattern

        Args
        ----
        - algorithm (str[percentage | weighted | autoEven | autoGeometric]): The algorithm of the distribution
        - mode (str[perDevice | perTopology | perPort]): The mode indicates across what the the distribution is allocated
        - values (list[tuple(value, weight)]): A list of tuples. Each tuple is a value and and it's corresponding weight in the distribution
        """
        if self._parent._mode[0] == "config":
            # multivalue_dict = dict()
            # multivalue_dict['xpath'] = self._get_multivalue_xpath(self._href, 'customDistributed')
            # if algorithm is not None:
            #     multivalue_dict['algorithm'] = algorithm
            # if mode is not None:
            #     multivalue_dict['mode'] = mode
            formatted_values = []
            if values is not None and len(values) > 0:
                for value in values:
                    formatted_values.append({"arg1": value[0], "arg2": value[1]})
            #     multivalue_dict['values'] = formatted_values
            # self._xpathObj._config.append(multivalue_dict)
            self._parent._properties["multiValue"].append(
                {self._href: ["customDistributed", algorithm, mode, formatted_values]}
            )
        else:
            formatted_values = None
            if values is not None:
                formatted_values = []
                for value in values:
                    formatted_values.append({"arg1": value[0], "arg2": value[1]})
            payload = {"algorithm": algorithm, "mode": mode, "values": formatted_values}
            self._set_pattern("customDistributed", payload)

    def String(self, string_pattern=None):
        """Sets the multivalue to a string pattern

        Args
        ----
        - string_pattern (str): A string pattern

        Examples
        --------
        - Test-{Inc:1,1}
        - Test-{"A", "B", "C"}
        - hex_{Dec:0xFFFF}
        - Test-{Inc:100}-{"A", "B"}-{Dec:3, 1, 3}
        """
        if self._parent._mode[0] == "config":
            # multivalue_dict = dict()
            # multivalue_dict['xpath'] = self._get_multivalue_xpath(self._href, 'string')
            # multivalue_dict['pattern'] = string_pattern
            # self._xpathObj._config.append(multivalue_dict)
            self._parent._properties["multiValue"].append(
                {self._href: ["string", string_pattern]}
            )
        else:
            payload = {"pattern": string_pattern}
            self._set_pattern("string", payload)

    def Custom(self, start_value=None, step_value=None, increments=None):
        """Sets the mutivalue to a custom pattern

        Args
        ----
        - start_value (str): A start value according to the format
        - step_value (str):: A step value according to the format
        - increments (list[tuple(value, count, list[increments])]): The structure of increments is such that after creating a custom multivalue with an initial start_value and step_value further sibling and/or nested child counters can be added using the increments parameter. Each value in increments is a tuple that consists of a value according to the multivalue format, a count and a list of any child increments.

        Examples
        --------
        - two siblings, no children:
          increment=[('1.1.1.1', 10, []), ('1.1.2.1', 5, [])]
        - two siblings, one child per each sibling:
          increment=[('1.1.1.1', 10, [('1.1.3.1', 3, [])]), ('1.1.2.1', 5, [('1.1.4.1', 4, [])])]

        Raises
        ------
        - ValueError: if increments is incorrectly formatted or if start_value, step_value are in the incorrect format
        """
        if self._parent._mode[0] == "config":
            # multivalue_dict = dict()
            # multivalue_dict['xpath'] = self._get_multivalue_xpath(self._href, 'custom')
            # if start_value is not None:
            #     multivalue_dict['start'] = start_value
            # if step_value is not None:
            #     multivalue_dict['step'] = step_value
            # if increments is not None:
            #     multivalue_dict['increment'] = self._get_custom_increments(increments)
            # self._xpathObj._config.append(multivalue_dict)
            self._parent._properties["multiValue"].append(
                {
                    self._href: [
                        "custom",
                        step_value,
                        step_value,
                        self._get_custom_increments(increments),
                    ]
                }
            )
        else:
            payload = {"start": start_value, "step": step_value}
            self._set_pattern("custom", payload)
            self._connection._delete("%s/custom/increment" % self._properties["href"])
            self._add_custom_increments(
                "%s/custom" % self._properties["href"], increments
            )
            self._custom_select()

    def _add_custom_increments(self, href, increments):
        if increments is not None:
            href = "%s/increment" % href
            for increment in increments:
                if len(increment) == 3:
                    payload = {"value": increment[0], "count": increment[1]}
                    response = self._connection._create(href, payload)
                    self._add_custom_increments(
                        response["links"][0]["href"], increment[2]
                    )
                else:
                    raise ValueError(
                        "increment value `%s` must be a tuple of 3 values (value, count, list[increment])"
                        % increment
                    )

    @property
    def Steps(self):
        """Get the Step resources for this multivalue.

        A Steps class provides the ability to enable/disable multivalue steps and provide a step value.
        The most common step is the port step which 'steps' the multivalue pattern by a value across each port.

        Returns
        -------
        - obj(uhd_restpy.steps.Steps): A multivalue step object
        """
        self.Pattern
        from uhd_restpy.steps import Steps

        return Steps(self)._custom_select()

    def _set_pattern(self, pattern, payload=None):
        self.Pattern
        href = "%s/%s" % (self._href, pattern)
        if payload is not None:
            for key in payload.copy():
                if payload[key] is None:
                    payload.pop(key)
        if bool(payload) is False:
            payload = None
        if pattern == self._properties["pattern"]:
            self._connection._update(href, payload)
        elif payload is not None:
            self._connection._create(href, payload)
        else:
            self._connection._update(self._href, {"pattern": pattern})
        self._custom_select()

    def _custom_select(self):
        payload = {
            "selects": [
                {
                    "from": self._href,
                    "properties": [
                        "count",
                        "format",
                        "source",
                        "pattern",
                        "availablePatterns",
                        "enums",
                    ],
                    "children": [
                        {
                            "child": "^(singleValue|alternate|random|repeatableRandom|repeatableRandomRange|counter|valueList|custom|increment|customDistributed|string)$",
                            "properties": ["*"],
                            "filters": [],
                        }
                    ],
                    "inlines": [],
                }
            ]
        }
        end = self._href.index("ixnetwork") + len("ixnetwork")
        url = "%s/operations/select" % self._href[0:end]
        self._set_properties(self._connection._execute(url, payload)[0], clear=True)
        return self

    def Overlay(self, index, value, count=1):
        """Add an overlay at a specific device index in a pattern.

        This is meant to overwrite an existing pattern with a few non-contiguous, random values.
        If the intent is to overwrite an entire pattern or most of a pattern with random values consider
        using the more performant random or valueList patterns.

        Args
        ----
        - index (int): 1 based device index
        - value (str): the overlay value
        - count (int): the number of indices to update with the overlay value starting from index attribute, default: 1
        """
        if self._parent._mode[0] == "config":
            attribute_present = False
            for multivaute_attr in self.parent._properties["multiValue"]:
                if self._href in multivaute_attr:
                    if "overlay" in multivaute_attr[self._href]:
                        overlay_index = multivaute_attr[self._href].index("overlay")
                        multivaute_attr[self._href][overlay_index + 1].append(
                            [index, value]
                        )
                    else:
                        multivaute_attr[self._href] += ["overlay", [[index, value]]]
                    attribute_present = True
                    break

            if not attribute_present:
                self.parent._properties["multiValue"].append(
                    {self._href: ["overlay", [[index, value]]]}
                )
        else:
            href = "%s/overlay" % (self._href)
            payload = {"count": count, "index": index, "indexStep": 1, "value": value}
            self._connection._create(href, payload)

    def ClearOverlays(self):
        """Clears all overlays that have been added."""
        self._connection._update(self._href, {"clearOverlays": True})
        self._connection._update(self._href, {"clearOverlays": False})

    def _get_multivalue_xpath(self, name, pattern):
        """
        This function is basically use to form the xpath for multivalue of nodes which are not related to traffic
        """
        source = (
            "[@source = "
            + "'"
            + str(self.parent._properties["xpath"])
            + " "
            + name
            + "']"
        )
        xpath = "/multivalue" + source + "/" + pattern
        return xpath

    def _get_field_multivalue_xpath(self, name):
        """
        This function basically provides us with xpath for traffic fields
        """
        field_name = name
        xpath = (
            self.parent._properties["xpath"] + "/field[@alias = '" + field_name + "']"
        )
        return xpath

    def _get_custom_increments(self, increments):
        """
        This function is related to custom multivalue, it basically refactors the increment list and prepares
        it in the right format of xpath to be added to json
        """
        increment_list = []
        self._rec_fill_increment_dict(increments, increment_list)
        return increment_list

    def _rec_fill_increment_dict(self, increments, increment_list, pattern=""):
        """
        This is a recursive utility function basically used by custom multivalue for formatting increments
        in a proper fashion
        """
        for i, inc in enumerate(increments):
            temp_dict = {}
            if pattern == "":
                pattern = "custom/increment[" + str(i + 1) + "]"
            elif i == 0:
                pattern = pattern + "/increment[" + str(i + 1) + "]"
            else:
                pattern = (
                    "/".join(pattern.split("/")[:-1]) + "/increment[" + str(i + 1) + "]"
                )

            temp_dict["xpath"] = pattern
            inc_len = len(inc)
            if inc_len >= 1:
                temp_dict["value"] = inc[0]
            if inc_len >= 2:
                temp_dict["count"] = inc[1]
            increment_list.append(temp_dict)
            if inc_len == 3:
                if len(inc[2]) != 0:
                    self._rec_fill_increment_dict(
                        inc[2], increment_list, pattern=pattern
                    )
