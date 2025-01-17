from .exceptions import TDAAPIError
from .enums import DURATION

# from .enums import DURATION, ORDER_TYPE, COMPLEX_ORDER_STRATEGY_TYPE, LEG_TYPE


class OrderBuilder(object):
    def __init__(
        self,
        quantity,
        price,
        duration="DAY",
        orderType="MARKET",
        orderStrategyType="SINGLE",
        complexOrderStrategyType="NONE",
        session="NORMAL",
        specialInstruction=None,
        requestedDestination="AUTO",
        priceLinkBasis=None,
        priceLinkType=None,
        stopPrice=None,
        stopPriceLinkBasis=None,
        stopPriceLinkType=None,
        stopType=None,
        taxLotMethod=None,
    ):
        if duration not in DURATION:
            raise TDAAPIError("Duration must be in {}".format(duration))

        self._rep = {
            "complexOrderStrategyType": complexOrderStrategyType,
            "orderType": orderType,
            "session": session,
            "price": str(price),
            "duration": duration,
            "orderStrategyType": orderStrategyType,
            "orderLegCollection": [],
            # "requestedDestination": requestedDestination,
            # "stopPrice": 0,
            # "stopPriceLinkBasis": stopPriceLinkBasis,
            # "stopPriceLinkType": stopPriceLinkType,
            # "stopPriceOffset": 0,
            # "stopType": stopType,
            # "priceLinkBasis": priceLinkBasis,
            # "priceLinkType": priceLinkType,
            #
            # "taxLotMethod": taxLotMethod,

            # "specialInstruction": specialInstruction,
        }

    def addLeg(
        self,
        assetType,
        symbol,
        instruction,
        positionEffect,
        quantity,
        quantityType,
        type=None,
        putCall=None,
    ):
        leg = {
            "orderLegType": assetType,
            "instrument": {
                "assetType": assetType,
                "symbol": symbol,
            },
            "instruction": instruction,
            "positionEffect": positionEffect,
            "quantity": quantity,
            "quantityType": quantityType,
        }

        # if assetType == 'OPTION':
        #     leg['instrument']['type'] = type
        #     leg['instrument']['putCall'] = putCall
        # elif assetType == 'MUTUAL_FUND':
        #     leg['instrument']['type'] = type
        # elif assetType == 'CASH_EQUIVALENT':
        #     leg['instrument']['type'] = type
        # elif assetType == 'FIXED_INCOME':
        #     leg['instrument']['maturityDate'] = maturityDate
        #     leg['instrument']['variableRate'] = variableRate
        #     leg['instrument']['factor'] = factor
        self._rep["orderLegCollection"].append(leg)

    def addOptionLeg(self, symbol, instruction, quantity):
        leg = {
            "instruction": instruction,
            "quantity": quantity,
            "instrument": {
                "symbol": symbol,
                "assetType": 'OPTION',
            }
        }

        self._rep["orderLegCollection"].append(leg)

    def to_json(self):
        return self._rep
