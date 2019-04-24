class APT(object):
    COUNTER = 0

    def __init__(self, name, description='', country=''):
        self.id = self.COUNTER
        self.COUNTER += 1
        self.name = name
        self.description = description
        self.country = country

    def get_details(self):
        return self.__dict__


class Tactic(object):
    COUNTER = 0

    def __init__(self, name, description='', url=''):
        self.id = self.COUNTER
        self.COUNTER += 1
        self.name = name
        self.description = description
        self.url = url

    def get_details(self):
        return self.__dict__


class Technique(object):
    COUNTER = 0

    def __init__(self, name, description='', references=None, mitre_technique_id=''):
        if references is None:
            references = []

        self.id = self.COUNTER
        self.COUNTER += 1
        self.name = name
        self.description = description
        self.references = references
        self.mitre_technique_id = mitre_technique_id

    def get_details(self):
        return self.__dict__


class TacticTechniqueMap(object):
    def __init__(self):
        self.tactics_to_techniques_map = {}
        self.techniques_to_tactics_map = {}

    def add_mapping(self, tactic, technique):
        self.tactics_to_techniques_map.setdefault(tactic.id, [])
        self.tactics_to_techniques_map[tactic.id].append(technique)

        self.techniques_to_tactics_map.setdefault(technique.id, [])
        self.tactics_to_techniques_map[technique.id].append(tactic)


class AttackNavigator(object):
    def __init__(self):
        self.apts = {}
        self.tactics = {}
        self.techniques = {}
        self.tactic_technique_map = None
        self.apt_technique_map = None

    def initialize(self):
        self._fetch_data()

    def get_tactics(self, search_param=None):
        if search_param is None:
            return [tactic.get_details() for tactic in self.tactics.values()]

    def _get_details(self, param_dict, key, raise_exception=False):
        instance = param_dict.get(key)
        if not instance:
            if raise_exception:
                raise Exception("Instance not found")
            else:
                return None

        return instance.get_details()

    def get_tactic(self, id_param, raise_exception=False):
        return self._get_details(self.tactics, id_param, raise_exception)

    def get_techniques(self, search_param=None):
        return

    def get_technique(self, id_param, raise_exception=False):
        return self._get_details(self.techniques, id_param, raise_exception)

    def get_apts(self, search_params=None):
        return

    def get_apt(self, id_param, raise_exception=False):
        return self._get_details(self.apts, id_param, raise_exception)

    def _fetch_data(self):
        a = Tactic('test tactics')
        self.tactics[a.id] = a

        b = Technique('test technique')
        self.techniques[b.id] = b

        c = APT('test apt')
        self.apts[c.id] = c



