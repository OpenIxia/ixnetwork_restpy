import json
import re
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.timer import Timer


class BatchAdd(object):
    def __init__(self, ixnetwork):
        """Context manager for batching restPy calls

        Args
        ----
        - ixnetwork (ixnetwork_restpy.base.Base): the root ixnetwork object
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.ixnetwork import Ixnetwork

        assert isinstance(ixnetwork, Ixnetwork)
        self._ixnetwork = ixnetwork
        self._url = self._get_base_url()
        self._config = []
        if "xpath" not in self._ixnetwork._properties:
            self._ixnetwork._properties["xpath"] = "/"
        self._ixnetwork._mode[0] = "config"

    def __enter__(self):
        return self

    def __exit__(self, *exc_info):
        """
        this basically forms a json of the cached object and then forwards it to the
        """
        self._ixnetwork._mode[0] = "normal"
        self._commit()

    @property
    def config(self):
        """
        Returns
        -------
        - the config json formed by BatchAdd class

        Example
        -------
        with BatchAdd(ixnetwork) as batch:
            vp = ixnetwork.Vport.add(Name="vp1").add(Name="vp2")
        print(batch.config)

        Raises
        ------
        - Exception if the property is accessed within the BatchAdd scope
        """
        if self._ixnetwork._mode[0] == "config":
            raise Exception(
                "you are only allowed to access the config property after BatchAdd context is over"
            )
        return self._config

    def _get_xpath_reference(self, attribute_property):
        if "parent_xpath" in attribute_property:
            parent_xpath = attribute_property["parent_xpath"]
        else:
            if "href" in attribute_property["parent_property"]:
                response = self._get_select_response(
                    attribute_property["parent_property"]["href"],
                    attribute_property["sdm_name"],
                )
                for child in response[0][attribute_property["sdm_name"]]:
                    child_xpath = child["xpath"]
                    if child_xpath.split("/")[-1].isdigit():
                        if attribute_property["id"] == child_xpath.split("/")[-1]:
                            return child_xpath
                    else:
                        return child_xpath
            parent_xpath = attribute_property["parent_property"]["xpath"]
        return "%s/%s[%s]" % (
            parent_xpath,
            attribute_property["sdm_name"],
            attribute_property["id"],
        )

    def _process_cached_objects(self):
        config = []
        for ixn_object in self._ixnetwork._children.keys():
            child_list = self._ixnetwork._children[ixn_object]
            for property_value in ixn_object._properties.values():
                if (
                    isinstance(property_value, Base)
                    and property_value._SDM_NAME in child_list
                ):
                    self._get_xpaths(property_value, ixn_object)
            ixn_object._rootNode = None
            self._make_xpath_json(ixn_object, config, child_list)
        if len(self._ixnetwork._dirty_objs) > 0:
            for dirt_object, dirty_value in self._ixnetwork._dirty_objs.items():
                self._handle_dirty_objects(dirt_object, dirty_value, config)
        self._config = config.copy()

    def _make_xpath_json(self, node, config, child_list):
        node._rootNode = None
        for index, item in enumerate(node._object_properties):
            temp_dict = {}
            if ("xpath" in item and item["xpath"] != "") or "href" in item:
                for value in item.values():
                    if (
                        isinstance(value, Base) and value._SDM_NAME in child_list
                    ) or "stack_index" in item:
                        self._make_xpath_json(value, config, child_list)
                continue

            for attribute_key, attribute_value in item.items():
                if (
                    attribute_key
                    in [
                        "self",
                        "id",
                        "href",
                        "parent_xpath",
                        "parent_property",
                        "no_indexing",
                        "stack_index",
                        "sdm_name",
                    ]
                    or attribute_value is None
                ):
                    continue
                elif isinstance(item[attribute_key], Base) and (
                    item[attribute_key]._SDM_NAME in child_list
                    or node._SDM_NAME == "stack"
                ):
                    # self.make_xpath_json(attribute_value, config, child_list)
                    continue
                elif attribute_key == "xpath" and item[attribute_key] != "/":
                    if "xpath" in node.parent._properties:
                        parent_xpath = item["parent_property"]["xpath"]
                    else:
                        parent_xpath = node._object_properties[index]["parent_xpath"]
                    if (
                        "no_indexing" in item and item["no_indexing"]
                    ) or node._SDM_NAME in ["protocols", "stack"]:
                        xpath = "%s/%s" % (parent_xpath, node._SDM_NAME)
                    elif "stack_index" in item:
                        xpath = "%s[@alias = '%s-%s']" % (
                            parent_xpath,
                            node._SDM_NAME,
                            item["stack_index"],
                        )
                    else:
                        xpath = "%s/%s[%s]" % (
                            parent_xpath,
                            node._SDM_NAME,
                            str(index + 1),
                        )
                    xpath = xpath.replace("//", "/")
                    node._object_properties[index][attribute_key] = xpath
                    if node._SDM_NAME != "stack":
                        temp_dict[attribute_key] = xpath
                elif attribute_key == "multiValue":
                    config += self._handle_multivalue_xpath(
                        attribute_value, item["xpath"]
                    )
                elif isinstance(attribute_value, list) or isinstance(
                    attribute_value, dict
                ):
                    if isinstance(attribute_value, dict) and "xpath" in attribute_value:
                        reference_xpath = (
                            attribute_value["xpath"]
                            if attribute_value["xpath"] != ""
                            else self._get_xpath_reference(attribute_value)
                        )
                        temp_dict[attribute_key] = reference_xpath
                        item[attribute_key] = reference_xpath
                    elif (
                        isinstance(attribute_value, dict) and "href" in attribute_value
                    ):
                        xpath = self._get_select_response(attribute_value["href"])[0][
                            "xpath"
                        ]
                        temp_dict[attribute_key] = xpath
                        item[attribute_key] = xpath
                    elif isinstance(attribute_value, list):
                        temp_list = []
                        for element in attribute_value:
                            if isinstance(element, dict) and "xpath" in element:
                                reference_xpath = (
                                    element["xpath"]
                                    if element["xpath"] != ""
                                    else self._get_xpath_reference(element)
                                )
                                temp_list.append(reference_xpath)
                            elif isinstance(element, dict) and "href" in element:
                                xpath_for_href = self._get_select_response(
                                    element["href"]
                                )[0]["xpath"]
                                temp_list.append(xpath_for_href)
                                element["xpath"] = xpath_for_href
                            elif "arg1" in element and isinstance(
                                element["arg1"], Base
                            ):
                                if "href" in element["arg1"]._properties:
                                    element["arg1"] = self._get_select_response(
                                        element["arg1"]._properties["href"]
                                    )[0]["xpath"]
                                elif "xpath" in element["arg1"]._properties:
                                    element["arg1"] = element["arg1"]._properties[
                                        "xpath"
                                    ]
                                else:
                                    raise Exception(
                                        "neither xpath nor href present, something went wrong!"
                                    )
                                temp_list.append(element)
                            else:
                                temp_list.append(element)
                        temp_dict[attribute_key] = temp_list
                        item[attribute_key] = temp_list
                else:
                    temp_dict[attribute_key] = attribute_value

            if len(temp_dict) > 0:
                config.append(temp_dict)

            for attribute_key, attribute_value in item.items():
                if isinstance(item[attribute_key], Base) and (
                    item[attribute_key]._SDM_NAME in child_list
                    or node._SDM_NAME == "stack"
                ):
                    self._make_xpath_json(attribute_value, config, child_list)

    def _handle_multivalue_xpath(self, value, xpath):
        xpath_list = []
        for multivalue in value:
            xpath_dict = {}
            for attribute, pattern in multivalue.items():
                packet_field = False
                if pattern[0] == "field":
                    packet_field = True
                    pattern.pop(0)
                    multivalue_name = pattern[0]
                    multivalue_xpath = "%s/field[@alias = '%s']" % (xpath, attribute)
                    xpath_dict["xpath"] = multivalue_xpath
                    xpath_dict["auto"] = False
                    xpath_dict["optionalEnabled"] = True
                    xpath_dict["activeFieldChoice"] = True
                else:
                    multivalue_name = pattern[0]

                    if multivalue_name == "custom":
                        multivalue_xpath = "/multivalue[@source = '%s %s']/" % (
                            xpath,
                            attribute,
                        )
                        xpath_dict["xpath"] = multivalue_xpath + "custom"
                    else:
                        multivalue_xpath = "/multivalue[@source = '%s %s']/%s" % (
                            xpath,
                            attribute,
                            multivalue_name,
                        )
                        xpath_dict["xpath"] = multivalue_xpath

                if multivalue_name == "singleValue" or multivalue_name == "alternate":
                    if packet_field:
                        xpath_dict[multivalue_name] = pattern[1]
                        xpath_dict["valueType"] = multivalue_name
                    else:
                        xpath_dict["value"] = pattern[1]
                elif multivalue_name == "string":
                    xpath_dict["pattern"] = pattern[1]
                elif multivalue_name == "valueList":
                    if packet_field:
                        xpath_dict["valueType"] = multivalue_name
                        xpath_dict[multivalue_name] = pattern[1]
                    else:
                        xpath_dict["values"] = pattern[1]
                elif multivalue_name == "counter":
                    if packet_field:
                        xpath_dict["valueType"] = pattern[1]
                    else:
                        xpath_dict["direction"] = pattern[1]
                    if pattern[2] is not None:
                        if packet_field:
                            xpath_dict["startValue"] = pattern[2]
                        else:
                            xpath_dict["start"] = pattern[2]
                    if pattern[3] is not None:
                        if packet_field:
                            xpath_dict["stepValue"] = pattern[3]
                        else:
                            xpath_dict["step"] = pattern[3]
                elif multivalue_name == "repeatableRandomRange":
                    if pattern[1] is not None:
                        xpath_dict["min"] = pattern[1]
                    if pattern[2] is not None:
                        xpath_dict["max"] = pattern[2]
                    if pattern[3] is not None:
                        xpath_dict["seed"] = pattern[3]
                    if pattern[4] is not None:
                        xpath_dict["step"] = pattern[4]
                elif multivalue_name == "repeatableRandom":
                    if pattern[1] is not None:
                        xpath_dict["fixed"] = pattern[1]
                    if pattern[2] is not None:
                        xpath_dict["mask"] = pattern[2]
                    if pattern[3] is not None:
                        xpath_dict["seed"] = pattern[3]
                    if pattern[4] is not None:
                        xpath_dict["count"] = pattern[4]
                elif multivalue_name == "customDistributed":
                    if pattern[1] is not None:
                        xpath_dict["algorithm"] = pattern[1]
                    if pattern[2] is not None:
                        xpath_dict["mode"] = pattern[2]
                    if len(pattern[3]) > 0:
                        xpath_dict["values"] = pattern[3]
                elif multivalue_name == "custom":
                    if pattern[1] is not None:
                        xpath_dict["start"] = pattern[1]
                    if pattern[1] is not None:
                        xpath_dict["step"] = pattern[1]
                    if len(pattern[3]) > 0:
                        increments = pattern[3]
                        for increment in increments:
                            increment["xpath"] = "%s%s" % (
                                multivalue_xpath,
                                increment["xpath"],
                            )
                        xpath_dict["increment"] = increments

                if "overlay" in pattern:
                    overlay_index = pattern.index("overlay")
                    multivalue_xpath = "/multivalue[@source = '%s %s']/overlay" % (
                        xpath,
                        attribute,
                    )
                    overlay_list = []
                    for index, overlays in enumerate(pattern[overlay_index + 1]):
                        overlay_xpath = multivalue_xpath + "[%s]" % (index + 1)
                        overlay_list.append(
                            {
                                "count": 1,
                                "index": overlays[0],
                                "indexStep": 1,
                                "value": overlays[1],
                                "xpath": overlay_xpath,
                            }
                        )
                    xpath_list += overlay_list
            if len(xpath_dict) > 0:
                xpath_list.append(xpath_dict)
        return xpath_list

    def _handle_dirty_objects(self, dirty_Obj, dirty_value, config):
        for dirty_child in dirty_value:
            if "multiValue" in dirty_child:
                mult_xpath = self._get_xpaths(
                    "multiValue", dirty_Obj, dirty_operation=True
                )
                config += self._handle_multivalue_xpath(
                    dirty_child["multiValue"], mult_xpath
                )
                continue
            else:
                self._get_xpaths(dirty_child, dirty_Obj, dirty_operation=True)
            for dirty_property in dirty_child[list(dirty_child.keys())[0]]:
                xpath_present = False
                for xpath_dict in config:
                    if xpath_dict["xpath"] == dirty_property["xpath"]:
                        self._insert_dirty_properties(dirty_property, xpath_dict)
                        xpath_present = True
                        break

                if not xpath_present:
                    temp_dict = {}
                    temp_dict["xpath"] = dirty_property["xpath"]
                    self._insert_dirty_properties(dirty_property, temp_dict)
                    config.append(temp_dict)

    def _insert_dirty_properties(self, dirty_values, xpath_dict):
        for value in dirty_values:
            if value == "href":
                continue
            xpath_dict[value] = dirty_values[value]

    def _commit(self):
        with Timer(self._ixnetwork) as timer:
            self._process_cached_objects()
            errs = self._ixnetwork.ResourceManager.ImportConfig(
                json.dumps(self._config), False
            )
            if len(errs) > 0:
                print(errs)
                raise Exception("import json has issues " + str(errs))
            self.__get_hrefs()
            timer.info("Batch Add Completed")

        self._ixnetwork._children.clear()
        self._ixnetwork._dirty_objs.clear()
        return self

    def _get_base_url(self):
        end = len(self._ixnetwork.href)
        if "ixnetwork" in self._ixnetwork.href:
            end = self._ixnetwork.href.index("ixnetwork") + len("ixnetwork")
        url = "%s/operations/select?xpath=true" % self._ixnetwork.href[0:end]
        return url

    def __form_payload(self, parent, child=None):
        if child is None:
            child = ""
        payload = {
            "from": parent,
            "properties": [],
            "children": [{"child": child, "properties": [], "filters": []}],
            "inlines": [],
        }
        return payload

    def _get_select_response(self, specific_obj=None, child=None):
        selects = []
        if specific_obj is not None:
            if isinstance(specific_obj, str):
                if child is None:
                    payload = self.__form_payload(specific_obj)
                else:
                    payload = self.__form_payload(specific_obj, "^%s$" % child)
            elif child is not None:
                payload = self.__form_payload(specific_obj.href, "^%s$" % child)
            else:
                payload = self.__form_payload(
                    specific_obj.href,
                    "^%s$" % self._ixnetwork._children[specific_obj][0],
                )
            selects.append(payload)
        else:
            for obj, child_str in self._ixnetwork._children.items():
                payload = self.__form_payload(obj.href, "^%s$" % "|".join(child_str))
                selects.append(payload)
        final_payload = {"selects": selects}
        responses = self._ixnetwork._connection._execute(self._url, final_payload)
        return responses

    def _get_xpaths(self, restpy_obj, parent, dirty_operation=False):
        if dirty_operation:
            if str(restpy_obj) == "multiValue":
                responses = self._get_select_response(parent)
            else:
                responses = self._get_select_response(
                    parent, list(restpy_obj.keys())[0]
                )
        else:
            responses = self._get_select_response(parent)
        for response_obj in responses:
            if dirty_operation:
                if str(restpy_obj) == "multiValue":
                    return response_obj["xpath"]
                else:
                    node_name = list(restpy_obj.keys())[0]
                    for response in response_obj[node_name]:
                        for item in restpy_obj[node_name]:
                            if "href" in item and response["href"] == item["href"]:
                                item["xpath"] = response["xpath"]
                    return
            else:
                if restpy_obj._SDM_NAME in response_obj:
                    already_configured = []
                    index_count = -1
                    if isinstance(response_obj[restpy_obj._SDM_NAME], dict):
                        restpy_obj._properties["xpath"] = response_obj[
                            restpy_obj._SDM_NAME
                        ]["xpath"]
                    else:
                        for response in response_obj[restpy_obj._SDM_NAME]:
                            href_present = False
                            for item in restpy_obj._object_properties:
                                if "href" in item and response["href"] == item["href"]:
                                    item["xpath"] = response["xpath"]
                                    index_count += 1
                                    href_present = True
                                    break
                            if not href_present:
                                already_configured.append({"xpath": response["xpath"]})
                        if len(already_configured) > 0 and (
                            re.search(
                                r"\d", already_configured[0]["xpath"].split("/")[-1]
                            )
                            is None
                            or restpy_obj._SDM_NAME not in ["configElement", "stack"]
                        ):
                            if index_count != -1:
                                restpy_obj._object_properties = (
                                    restpy_obj._object_properties[0 : index_count + 1]
                                    + already_configured
                                    + restpy_obj._object_properties[index_count + 1 :]
                                )
                            else:
                                restpy_obj._object_properties = (
                                    already_configured + restpy_obj._object_properties
                                )
                        restpy_obj._index = len(restpy_obj._object_properties) - 1
            for index, item in enumerate(restpy_obj._object_properties):
                item["parent_xpath"] = response_obj["xpath"]

    def __get_hrefs(self):
        responses = self._get_select_response()
        href_dict = {}
        ignore_list = ["id", "href", "xpath"]
        self.__recursively_create_href_map(href_dict, responses, ignore_list)
        for ixn_object in self._ixnetwork._children.keys():
            self.__recursively_fill_hrefs(href_dict, ixn_object, ignore_list)

    def __recursively_create_href_map(self, href_dict, href_response, ignore_list):
        for obj in href_response:
            href_dict[obj["xpath"]] = obj["href"]
            for key in obj.keys():
                if key not in ignore_list:
                    if not isinstance(obj[key], list):
                        obj[key] = [obj[key]]
                    self.__recursively_create_href_map(href_dict, obj[key], ignore_list)

    def __recursively_fill_hrefs(self, href_dict, ixn_object, ignore_list):
        for obj in ixn_object._object_properties:
            if "xpath" not in obj:
                pass
            else:
                if obj["xpath"] not in href_dict:
                    pass
                else:
                    obj["href"] = href_dict[obj["xpath"]]
            for key in obj.keys():
                if isinstance(obj[key], Base):
                    self.__recursively_fill_hrefs(href_dict, obj[key], ignore_list)
