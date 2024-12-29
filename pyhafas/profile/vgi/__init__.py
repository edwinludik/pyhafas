import pytz

from pyhafas.profile.base import BaseProfile


class INVGProfile(BaseProfile):
    """
    Profile of the HaFAS of Verkehrsverbund Großraum Ingolstadt, previously known as Ingolstädter Verkehrsgesellschaft (INVG)
    """
    baseUrl = "https://fpa.invg.de/bin/mgate.exe"
    defaultUserAgent = "pyhafas/0.6.0 (iPhone; iOS 13.1.2; Scale/2.00)"

    addMicMac = False
    addChecksum = False

    locale = 'de-DE'
    timezone = pytz.timezone('Europe/Berlin')

    requestBody = {
        'client': {
            'id': 'INVG',
            'v': '1040000',
            'type': 'IPH',
            'name': 'invgPROD-APPSTORE-LIVE'
        },
        'ext': 'DB.R21.12.a',
        'ver': '2.0.4 (26)',
        'auth': {
            'type': 'AID',
            'aid': 'GITvwi3BGOmTQ2a5'
        }
    }

    availableProducts = {
        'bus': [1, 16],
        'express_train': [2],
        'regional_train': [4],
        'local_train': [8],
        'ferry': [32],
        'subway': [64],
        'tram': [128],
        'on_demand': [256]
    }

    defaultProducts = [
        'bus',
        'express_train',
        'regional_train',
        'local_train',
        'ferry',
        'subway',
        'tram',
        'on_demand'
    ]
