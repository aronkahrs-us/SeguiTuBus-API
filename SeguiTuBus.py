import requests

BASE_URL = "https://seguitubus.trescruces.com.uy/api/auth/app"
VERSION = '7.0'


class STB:
    def __init__(self) -> None:
        '''Initialize the class'''
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        pass

    def _make_request(self, path:str, headers=None, json={}):
        '''
        Handle server requests

                Parameters:
                        path (str): path of request
                        headers (dict): headers(optional)
                        json (dict): data(optional)

                Returns:
                        binary_sum (str): Binary string of the sum of a and b
        '''
        if headers == None:
            headers = self.headers
        return requests.post(f'{BASE_URL}/{path}', headers=headers, json=json)

    def _list_config(self):
        '''
        Retrive Config List

                Returns:
                        config (dict): config list
        '''
        return (self._make_request('WSlistconfig').json())

    def _version(self):
        '''
        Retrive version data

                Returns:
                        version (dict): version list
        '''
        headers = self.headers.copy()
        headers['X-Requested-With'] = 'XMLHttpRequest'
        return (self._make_request('WSversion', headers=headers, json={'version': VERSION}
                                   ).json())

    def list_serv(self, Empresa: str = None, HoraInicio: str = None, Origen: str = None,
                 Destino: str = None, NroServicio: str = None, VarianteServicio: str = None) -> dict:
        '''
        Retrives and filters buses
        
                Parameters:
                        Empresa (str): Buses Company
                        HoraInicio (str): Buses Departure Time
                        Origen (str): Buses Origin
                        Destino (str): Buses Destination
                        NroServicio (str): Bus Service Number
                        VarianteServicio (str): Bus variant (self.list_arrays()['response']['tipos'] to get variants list)

                Returns:
                        service list (dict): list of services
        '''
        t = {}
        if Empresa != None:
            t['Empresa'] = Empresa.upper()
        if HoraInicio != None:
            t['HoraInicioTeorica'] = HoraInicio.upper()
        if Origen != None:
            t['Origen'] = Origen.upper()
        if Destino != None:
            t['Destino'] = Destino.upper()
        if NroServicio != None:
            t['nroServicio'] = NroServicio.upper()
        if VarianteServicio != None:
            t['VarianteServicio'] = VarianteServicio.upper()
        return (self._make_request('WSlistserv', json={'filtros': t}).json())

    def info_bus(self, Bus: str):
        return (self._make_request('WSinfobus', json={'bus': Bus}).json())

    def list_serv_map(self, Empresa: str = None, HoraInicio: str = None, Origen: str = None,
                    Destino: str = None, NroServicio: str = None, VarianteServicio: str = None) -> dict:
        '''
        Retrives and filters buses
        
                Parameters:
                        Empresa (str): Buses Company (self.list_arrays()['response']['empresas'] to get company list)
                        HoraInicio (str): Buses Departure Time
                        Origen (str): Buses Origin (self.list_arrays()['response']['ciudades'] to get cities list)
                        Destino (str): Buses Destination (self.list_arrays()['response']['ciudades'] to get cities list)
                        NroServicio (str): Bus Service Number
                        VarianteServicio (str): Bus variant (self.list_arrays()['response']['tipos'] to get variants list)

                Returns:
                        service list (dict): list of services
        '''
        t = {}
        if Empresa != None:
            t['Empresa'] = Empresa.upper()
        if HoraInicio != None:
            t['HoraInicioTeorica'] = HoraInicio.upper()
        if Origen != None:
            t['Origen'] = Origen.upper()
        if Destino != None:
            t['Destino'] = Destino.upper()
        if NroServicio != None:
            t['nroServicio'] = NroServicio.upper()
        if VarianteServicio != None:
            t['VarianteServicio'] = VarianteServicio.upper()
        headers = self.headers.copy()
        headers['X-Requested-With'] = 'XMLHttpRequest'
        return (self._make_request('WSlistservmap', json={'filtros': t}).json())

    def location(self, Bus):
        headers = self.headers.copy()
        headers['X-Requested-With'] = 'XMLHttpRequest'
        return (self._make_request('WSlocation', json={'bus': Bus}).json())

    def list_arrays(self):
        headers = self.headers.copy()
        headers['X-Requested-With'] = 'XMLHttpRequest'
        return (self._make_request('WSlistarrays', json={}).json())
    