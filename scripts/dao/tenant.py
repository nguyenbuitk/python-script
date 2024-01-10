import collections
import os.path
import pickle
import yaml


class Tenant:
    def __init__(self, tenant_id="", tenant_fn="", tenant_db_pwd=""):
        self.tenant_id = tenant_id
        self.tenant_fn = tenant_fn
        self.tenant_db_pwd = tenant_db_pwd

    def __repr__(self):
        return "{\"tenant_id\":\"%s\",\"tenant_fn\":\"%s\",\"tenant_db_pwd\":\"%s\"}" % (self.tenant_id, self.tenant_fn, self.tenant_db_pwd)

    def __str__(self):
        return "{\"tenant_id\":\"%s\",\"tenant_fn\":\"%s\",\"tenant_db_pwd\":\"%s\"}" % (self.tenant_id, self.tenant_fn, self.tenant_db_pwd)


class TenantDAO:
    def __init__(self, path="/opt/ovcloud/tenants/.tenants"):
        self.__tenants = collections.OrderedDict()
        self.__path = path

        self.migrate()

        if os.path.isfile(path):
            with open(path) as myfile:
                self.__tenants = yaml.load(myfile.read())
        else:
            for i in range(1, 9):
                self.__tenants["TENANT_SLOT_" + str(i)] = None

            self.save()

        print self.__tenants

    def get(self):
        return self.__tenants

    def save(self):
        with open(self.__path, "w") as myfile:
            myfile.write(yaml.dump(self.__tenants))

    def is_exist(self, tenant_id):
        slot = 0
        for t in self.__tenants.values():
            slot += 1
            if not t:
                continue

            if t.tenant_id == tenant_id:
                return slot

        return 0

    def add_tenant(self, tenant_id, tenant_fn, tenant_db_pwd):
        tenant_id = str(tenant_id).strip()
        slot = self.is_exist(tenant_id)

        if slot > 0:
            return slot

        tenant_fn = str(tenant_fn).strip()
        tenant_db_pwd = str(tenant_db_pwd).strip()

        for key in self.__tenants:
            slot += 1
            if self.__tenants[key] is None:
                self.__tenants[key] = Tenant(tenant_id=tenant_id, tenant_fn=tenant_fn, tenant_db_pwd=tenant_db_pwd)
                break

        if slot < 1:
            raise Exception("Out of slot")

        return slot

    def remove_tenant(self, tenant_id):
        tenant_id = tenant_id.strip()

        for t in self.__tenants:
            if self.__tenants[t] is None:
                continue

            if self.__tenants[t].tenant_id == tenant_id:
                self.__tenants[t] = None

    def migrate(self):
        old_file = "/home/ubuntu/.tenants_v2"

        if os.path.isfile(old_file):
            with open(old_file) as myfile:
                self.__tenants = pickle.loads(myfile.read())

            if self.__tenants:
                self.save()

            os.remove(old_file)
