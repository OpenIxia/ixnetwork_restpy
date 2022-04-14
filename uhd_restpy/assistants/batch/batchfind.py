import ixnetwork_restpy
import copy


class BatchFind:
    _OBJECTS = {}

    def __init__(self, root):
        """Context manager for batching .find() transactions.

        Normally chained .find() method calls are submitted individually to
        the server. This class batches all .find() method calls
        executed within the context scope and submits a single select operation
        to the server.  The returned results are then available as attributes of
        the .results property.

        ```
        # example that demonstrates finding all vlans where vlanid is 1
        with BatchFind(ixnetwork) as ctx:
            ixnetwork.Vport.find().Interface.find().Vlan.find(VlanId="^1$")
        print(ctx.results.vlan)
        ```

        Args
        ----
        - root (ixnetwork_restpy.base.Base): An ixnetwork_restpy object that is the
          starting point in the hierarchy of the nested find statements.
        """
        assert isinstance(root, ixnetwork_restpy.base.Base)
        self._select_payload = {
            "from": root.href,
            "properties": [],
            "children": [],
            "inlines": [],
        }
        self._root = root
        self._original_select = self._root.__class__._select
        self._root.__class__.__base__._select = BatchFind._select
        self._results = type("results", (), {})()

    @staticmethod
    def _select(self, filters=dict(), properties=["*"]):
        if self._SDM_NAME not in BatchFind._OBJECTS:
            BatchFind._OBJECTS[self._SDM_NAME] = {"base": self, "select": None}
        valid_filters = []
        for key, value in filters.items():
            if value is not None:
                valid_filters.append({"property": key, "regex": value})
        BatchFind._OBJECTS[self._SDM_NAME]["select"] = {
            "child": self._SDM_NAME,
            "properties": properties,
            "filters": valid_filters,
        }
        return self

    def __enter__(self):
        return self

    def __exit__(self, *exc_info):
        """Execute the select operation.

        Restore the original select method that was hooked.
        If the select is successful add returned objects to the results object.
        The results object contains one array attribute for every child name
        in the select payload.
        """
        self._root.__class__.__base__._select = self._original_select
        selects = []
        for obj in self._root:
            select = copy.deepcopy(self._select_payload)
            select["from"] = obj.href
            for _, value in BatchFind._OBJECTS.items():
                select["children"].append(value["select"])
            selects.append(select)
        selects_payload = {"selects": selects}
        self._root.debug(
            "{} select operation payload: {}".format(
                self.__class__.__name__, selects_payload
            )
        )
        end = self._root.href.index("ixnetwork") + len("ixnetwork")
        url = self._root.href[0:end] + "/operations/select"
        with ixnetwork_restpy.Timer(self._root) as t:
            results = self._root._connection._execute(url, selects_payload)
            for result in results:
                self._process_results(self._root, result)
            count = []
            for key, value in self._results.__dict__.items():
                count.append(".{} {}".format(key, len(value)))
            t.info("{}.results: {}".format(self.__class__.__name__, ", ".join(count)))

    def _process_results(self, parent, results):
        for key, value in results.items():
            if key in BatchFind._OBJECTS:
                self._copy_results(parent, key, value)

    def _get_obj(self, key):
        obj = copy.copy(BatchFind._OBJECTS[key]["base"])
        obj._clear()
        if key not in self._results.__dict__:
            self._results.__dict__[key] = []
        self._results.__dict__[key].append(obj)
        return obj

    def _copy_results(self, parent, key, value):
        if isinstance(value, list):
            for item in value:
                self._copy_results(parent, key, item)
        else:
            obj = self._get_obj(key)
            obj._parent = parent
            obj_values = {}
            for attr_name, attr_value in value.items():
                if attr_name == "href" or attr_name in obj._SDM_ATT_MAP.values():
                    obj_values[attr_name] = attr_value
                elif attr_name in BatchFind._OBJECTS:
                    self._process_results(obj, {attr_name: attr_value})
            obj._object_properties.append(obj_values)

    @property
    def results(self):
        return self._results
