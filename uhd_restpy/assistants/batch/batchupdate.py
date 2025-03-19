import time
import json
import inspect
from uhd_restpy.testplatform.sessions.ixnetwork.ixnetwork import Ixnetwork
from uhd_restpy.timer import Timer


class Batch(object):
    """Base batch functionality"""

    def __init__(self, ixnetwork):
        """hook Ixnetwork._connection._update method"""
        if isinstance(ixnetwork, Ixnetwork) is False:
            raise Exception("Must be an instance of the Ixnetwork class")
        self._ixnetwork = ixnetwork

    def _send_recv(self, method, url, payload):
        connection, url = self._ixnetwork._connection._normalize_url(url)
        headers = self._ixnetwork._connection._headers
        headers["Content-Type"] = "application/json"
        response = self._ixnetwork._connection._request(
            method=method,
            url=url,
            data=json.dumps(payload),
            headers=headers,
            verify=self._ixnetwork._connection._verify_cert,
            allow_redirects=False,
        )
        if method == "POST":
            return response.json()
        else:
            return None


class BatchUpdate(Batch):
    """Context manager for batching REST PATCH transactions"""

    def __init__(self, ixnetwork):
        """hook Ixnetwork._connection._update method"""
        super(BatchUpdate, self).__init__(ixnetwork)
        self._original_update = ixnetwork._connection._update
        self._ixnetwork._connection._update = self._batch_update
        self._updates = {}
        self._total_updates = 0

    def _batch_update(self, url, payload):
        """BULK PATCH REST API
        A node has a multiplicity of required if there is no id in the payload
        else it has a multiplicity of list/optional
        """
        self._total_updates += 1
        base = inspect.currentframe().f_back.f_locals["self"]
        if url not in self._updates:
            self._updates[url] = {}
        id = None if "id" not in payload else payload["id"]
        if id not in self._updates[url]:
            update = lambda: None
            update.id = id
            update.base = base
            update.payload = payload
            update.is_list = "find" in dir(base) and id is not None
            self._updates[url][id] = update
        else:
            self._updates[url][id].payload.update(payload)
        for key, value in payload.items():
            base._properties[key] = value

    def _process_batch_update(self):
        for url, batch in self._updates.items():
            payload = []
            for _, update in batch.items():
                if update.is_list:
                    payload.append(update.payload)
                else:
                    payload = update.payload
            response = self._send_recv("PATCH", url, payload)

    def __enter__(self):
        """On entry of the context manager"""
        return self

    def __exit__(self, *exc_info):
        """On exit of the context manager
        Commit all update transactions
        Restore hooks
        Log details
        """
        with Timer(self._ixnetwork) as t:
            self._process_batch_update()
            t.info("Batch commit of {} updates".format(self._total_updates))
        self._ixnetwork._connection._update = self._original_update


class BatchAdd(Batch):
    """Context manager for batching REST POST transactions"""

    def __init__(self, ixnetwork):
        """hook Ixnetwork._connection._add method"""
        super(BatchAdd, self).__init__(ixnetwork)
        self._original_add = ixnetwork._connection._create
        self._ixnetwork._connection._create = self._batch_add
        self._adds = {}
        self._total_adds = 0

    def _batch_add(self, url, payload):
        """BULK POST REST API"""
        self._total_adds += 1
        if url not in self._adds:
            base = inspect.currentframe().f_back.f_locals["self"]
            self._adds[url] = {"base": base, "payload": []}
        if payload is None:
            payload = {}
        self._adds[url]["payload"].append(payload)

    def _process_batch_add(self):
        for url, batch in self._adds.items():
            response = self._send_recv("POST", url, batch["payload"])
            responses = len(response["links"])
            for i in range(responses):
                batch["base"]._set_properties(
                    {"href": response["links"][responses - i - 1]["href"]}
                )
            batch["base"].refresh()

    def __enter__(self):
        """On entry of the context manager"""
        return self

    def __exit__(self, *exc_info):
        """On exit of the context manager
        Commit all add transactions
        Restore hooks
        Log details
        """
        start = time.time()
        self._process_batch_add()
        self._ixnetwork.info(
            "Batch commit of %s adds in %.3fs" % (self._total_adds, time.time() - start)
        )
        self._ixnetwork._connection._create = self._original_add


# class BatchCommit(object):
#     """Context manager for batching REST POST/PATCH/DELETE transactions
#     - POST operation and GET transactions are not batched
#     - Before dependencies are used in subsequent transactions execute a commit
#     - On error transactions will not be rolled back
#     """

#     def __init__(self, ixnetwork):
#         """
#         - hook _create, _update, _delete from the Connection class'"""
#         if isinstance(ixnetwork, Ixnetwork) is False:
#             raise Exception("Must be an instance of the Ixnetwork class")
#         self._ixnetwork = ixnetwork
#         self._original_create = ixnetwork._connection._create
#         self._original_update = ixnetwork._connection._update
#         self._original_delete = ixnetwork._connection._delete
#         self._ixnetwork._connection._create = self._create
#         self._ixnetwork._connection._update = self._update
#         self._ixnetwork._connection._delete = self._delete

#     def _clear(self):
#         self._count = 0
#         self._create = {}
#         self._update = {}
#         self._delete = {}

#     def _create(self, url, payload):
#         """BULK POST REST API
#         An id is None is a 1..1 node else it is a 0..n node
#         payload contains the id
#         Need to update the underlying base href/id with a GUID
#         After commit replace the GUID with a valid id/href
#         """
#         self._count += 1
#         if url not in self._create:
#             base = inspect.currentframe().f_back.f_locals["self"]
#             self._create[url] = {"base": base, "payload": []}
#         if payload is None:
#             payload = {}
#         self._create[url]["payload"].append(payload)

#     def _update(self, url, payload):
#         """BULK PATCH REST API
#         An id is None is a 1..1 node else it is a 0..n node
#         """
#         self._count += 1
#         base = inspect.currentframe().f_back.f_locals["self"]
#         if url not in self._update:
#             self._update[url] = {}
#         id = None if "id" not in payload else payload["id"]
#         if id not in self._update[url]:
#             update = lambda: None
#             update.id = id
#             update.base = base
#             update.payload = payload
#             self._update[url][id] = update
#         else:
#             self._update[url][id].payload.update(payload)

#     def _delete(self, url):
#         """BULK DELETE REST API
#         An id is None is a 1..1 node else it is a 0..n node
#         """
#         self._count += 1
#         try:
#             id = int(url.split("/")[-1])
#             url = "/".join(url.split("/")[0:-1])
#         except ValueError:
#             id = None
#         base = inspect.currentframe().f_back.f_locals["self"]
#         if url not in self._delete:
#             self._delete[url] = {}
#         delete = lambda: None
#         delete.id = id
#         delete.base = base
#         delete.payload = {"id": id}
#         self._delete[url][id] = delete

#     def _send_recv(self, method, url, payload):
#         connection, url = self._ixnetwork._connection._normalize_url(url)
#         headers = self._ixnetwork._connection._headers
#         headers["Content-Type"] = "application/json"
#         response = self._ixnetwork._connection._request(
#             method=method,
#             url=url,
#             data=json.dumps(payload),
#             headers=headers,
#             verify=self._ixnetwork._connection._verify_cert,
#             allow_redirects=False,
#         )
#         if method == "POST":
#             return response.json()
#         else:
#             return None

#     def _process_batch_create(self):
#         for url, create in self._create.items():
#             response = self._send_recv("POST", url, create["payload"])
#             for link in response["links"]:
#                 create["base"]._set_properties({"href": link["href"]})
#             create["base"].refresh()

#     def _process_batch_update(self):
#         for url, batch in self._update.items():
#             payload = []
#             for _, update in batch.items():
#                 payload.append(update.payload)
#             response = self._send_recv("PATCH", url, payload)
#             for _, update in batch.items():
#                 for key, value in update.payload.items():
#                     update.base._properties[key] = value

#     def _process_batch_delete(self):
#         for url, batch in self._delete.items():
#             payload = []
#             for _, delete in batch.items():
#                 payload.append(delete.payload)
#             response = self._send_recv("DELETE", url, payload)

#     def __enter__(self):
#         """Setup the context manager"""
#         self._clear()
#         return self

#     def __exit__(self, *exc_info):
#         """On exit of the context manager
#         Commit any outstanding transactions
#         Restore hooks
#         """
#         self.commit()
#         self._ixnetwork._connection._create = self._original_create
#         self._ixnetwork._connection._update = self._original_update
#         self._ixnetwork._connection._delete = self._original_delete

#     def commit(self):
#         start = time.time()
#         self._process_batch_create()
#         self._process_batch_update()
#         self._process_batch_delete()
#         self._ixnetwork.info("Committed %s REST transactions in %.3fs" % (self._count, time.time() - start))
#         self._clear()
