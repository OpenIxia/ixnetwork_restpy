import json
import copy
from ixnetwork_restpy.xpath import Xpath
from ixnetwork_restpy.base import Base


class ConfigAssistant(object):
    def __init__(self, ixnetwork):
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.ixnetwork import Ixnetwork

        assert isinstance(ixnetwork, Ixnetwork)
        self._ixnetwork = copy.copy(ixnetwork)
        self._ixnetwork._xpathObj = Xpath()
        self._ixnetwork._xpath = "/"
        self._ixnetwork._xpathObj._mode = "config"

    @property
    def config(self):
        return self._ixnetwork

    @property
    def config_json(self):
        return self._ixnetwork._xpathObj._config

    def clear_config(self):
        self._ixnetwork._xpathObj._config = []

    def commit(self):
        config = self._ixnetwork._xpathObj._config
        self._ixnetwork._xpathObj._mode = "normal"
        errs = self._ixnetwork.ResourceManager.ImportConfig(json.dumps(config), False)
        self.__get_hrefs()
        self.clear_config()
        return errs

    def __form_payload(self, parent, child=None):
        if child is None:
            child = ""
        payload = {"from": parent, "properties": [], "children": [{"child": child, "properties": [], "filters": []}], "inlines": []}
        return payload

    def __get_hrefs(self):
        end = len(self._ixnetwork.href)
        if "ixnetwork" in self._ixnetwork.href:
            end = self._ixnetwork.href.index("ixnetwork") + len("ixnetwork")
        url = "%s/operations/select?xpath=true" % self._ixnetwork.href[0:end]
        selects = []
        for child_str in self._ixnetwork._xpathObj._children:
            payload = self.__form_payload(self._ixnetwork.href, "^%s$" % child_str)
            selects.append(payload)
        final_payload = {"selects": selects}
        responses = self._ixnetwork._connection._execute(url, final_payload)
        href_dict = {}
        ignore_list = ["id", "href", "xpath"]
        self.__recursively_create_href_map(href_dict, responses, ignore_list)
        # print(href_dict)
        self.__recursively_fill_hrefs(href_dict, self._ixnetwork, ignore_list)

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
                # print(str(ixn_object.__class__.__name__) + ' has no xpath')
            else:
                if obj["xpath"] not in href_dict:
                    pass
                    # print(str(ixn_object.__class__.__name__) + ' has no matching xpath')
                else:
                    obj["href"] = href_dict[obj["xpath"]]
            for key in obj.keys():
                if isinstance(obj[key], Base):
                    self.__recursively_fill_hrefs(href_dict, obj[key], ignore_list)
