from django.shortcuts import render
from django.http import HttpResponse
import xml.etree.ElementTree as ET
import zeep


def index(request):
    return render(request, 'uids/index.html')


class DataHolder(object):
    def __init__(self, title=None, time_period=None, obs_value=None):
        self.title = title
        self.time_period = time_period
        self.obs_value = obs_value


def international_reserves(request):
    wsdl = 'http://www.banxico.org.mx/DgieWSWeb/DgieWS?WSDL'
    client = zeep.Client(wsdl=wsdl)
    with client.settings():
        result = client.service.reservasInternacionalesBanxico()
        xml_tree = ET.fromstring(result)
        res = xml_tree.find('.//*[@IDSERIE="SF43707"]/*')
        data = res.attrib
    return render(request, 'uids/international_reserves.html', {"time_period": data["TIME_PERIOD"], "value": data["OBS_VALUE"]})


def interest_rates(request):
    ids = ['SF60633', 'SF61745', 'SF60648', 'SF60649']
    title = ["Valores gubernamentales, Resultados de la subasta semanal "
             "Cetes a 28 días - Tasa de rendimiento - Fecha subasta",
             "Tasa objetivo",
             "Tasas de Interés Interbancarias TIIE a 28 días - Fecha determinación",
             "Tasas de Interés Interbancarias TIIE a 91 días - Fecha determinación"]
    title_index = 0
    info = []
    wsdl = 'http://www.banxico.org.mx/DgieWSWeb/DgieWS?WSDL'
    client = zeep.Client(wsdl=wsdl)
    with client.settings():
        result = client.service.tasasDeInteresBanxico()
    xml_tree = ET.fromstring(result)
    for single_id in ids:
        res = xml_tree.find(".//*[@IDSERIE='{}']/*".format(single_id))
        data = res.attrib
        info.append(DataHolder(title[title_index], data["TIME_PERIOD"], data["OBS_VALUE"]))
        title_index += 1
    return render(request, 'uids/interest_rates.html', {"info": info})


def exchange_rate(request):
    ids = ['SF46410', 'SF60632', 'SF43718', 'SF46407', 'SF46406', 'SF60653']
    title = ["Cotización de las divisas que conforman la canasta del DEG Respecto al peso mexicano Euro",
             "Cotización de la divisa Respecto al peso mexicano Dólar Canadiense",
             "Tipo de cambio Pesos por dólar E.U.A.Tipo de cambio para solventar "
             "obligaciones denominadas en moneda extranjera Fecha de determinación(FIX)",
             "Cotización de las divisas que conforman la canasta del DEG Respecto al peso mexicano Libra esterlina",
             "Cotización de las divisas que conforman la canasta del DEG Respecto al peso mexicano Yen japonés",
             "Tipo de cambio pesos por dólar E.U.A. "
             "Tipo de cambio para solventar obligaciones denominadas en moneda extranjera Fecha de liquidación"]
    title_index = 0
    info = []
    wsdl = 'http://www.banxico.org.mx/DgieWSWeb/DgieWS?WSDL'
    client = zeep.Client(wsdl=wsdl)
    with client.settings():
        result = client.service.tiposDeCambioBanxico()
    xml_tree = ET.fromstring(result)
    for single_id in ids:
        res = xml_tree.find(".//*[@IDSERIE='{}']/*".format(single_id))
        data = res.attrib
        info.append(DataHolder(title[title_index], data["TIME_PERIOD"], data["OBS_VALUE"]))
        title_index += 1
    return render(request, 'uids/exchange_rate.html', {"info": info})


def udis(request):
    wsdl = 'http://www.banxico.org.mx/DgieWSWeb/DgieWS?WSDL'
    client = zeep.Client(wsdl=wsdl)
    with client.settings():
        result = client.service.udisBanxico()
        xml_tree = ET.fromstring(result)
        res = xml_tree.find('.//*[@IDSERIE="SP68257"]/*')
        data = res.attrib
    return render(request, 'uids/udis.html', {"time_period": data["TIME_PERIOD"], "value": data["OBS_VALUE"]})
